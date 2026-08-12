import sqlite3
from datetime import datetime
import threading

DB_NAME = "progress.db"
_db_local = threading.local()


def get_connection():
    if not hasattr(_db_local, "connection"):
        _db_local.connection = sqlite3.connect(DB_NAME, check_same_thread=False)
        _db_local.connection.row_factory = sqlite3.Row
    return _db_local.connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        level INTEGER DEFAULT 1,
        last_notification DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        program TEXT,
        day TEXT,
        exercise_id TEXT,
        weight REAL,
        reps INTEGER,
        approaches INTEGER,
        date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_status (
        user_id INTEGER,
        day TEXT,
        exercise_id TEXT,
        completed BOOLEAN DEFAULT 0,
        approaches_done INTEGER DEFAULT 0,
        PRIMARY KEY (user_id, day, exercise_id)
    )
    """)

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_user_date ON history(user_id, date DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_user_program_day ON history(user_id, program, day)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_daily_status_user_day ON daily_status(user_id, day)")

    conn.commit()
    print("✅ База данных инициализирована")


def get_user_level(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT level FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result["level"] if result else 1


def set_user_level(user_id, level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO users (user_id, level, last_notification) VALUES (?, ?, ?)",
                   (user_id, level, datetime.now().date()))
    conn.commit()


def get_completed_exercises(user_id, day):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT exercise_id FROM daily_status WHERE user_id=? AND day=? AND completed=1", (user_id, day))
    return [row["exercise_id"] for row in cursor.fetchall()]


def reset_daily_status(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM daily_status WHERE user_id=?", (user_id,))
    conn.commit()


def get_today_exercise_details(user_id, program, day, exercise_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT weight, reps, date FROM history 
        WHERE user_id=? AND program=? AND day=? AND exercise_id=?
        AND date LIKE ?
        ORDER BY date ASC
    """, (user_id, program, day, exercise_id, datetime.now().strftime("%Y-%m-%d") + "%"))
    results = cursor.fetchall()
    conn.close()
    return [{"weight": row["weight"], "reps": row["reps"], "date": row["date"]} for row in results]


def get_exercise_history(user_id, program, day, exercise_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT weight, reps, approaches, date FROM history 
        WHERE user_id=? AND program=? AND day=? AND exercise_id=?
        ORDER BY date DESC LIMIT 1
    """, (user_id, program, day, exercise_id))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"weight": result["weight"], "reps": result["reps"], "approaches": result["approaches"],
                "date": result["date"]}
    else:
        return {"weight": 0, "reps": 0, "approaches": 0, "date": "—"}


def save_exercise_result(user_id, program, day, exercise_id, weight, reps, approaches):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history WHERE user_id=? AND program=? AND day=? AND exercise_id=? AND date LIKE ?",
                   (user_id, program, day, exercise_id, datetime.now().strftime("%Y-%m-%d") + "%"))
    cursor.execute("""
        INSERT INTO history (user_id, program, day, exercise_id, weight, reps, approaches, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, program, day, exercise_id, weight, reps, approaches, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()


def mark_exercise_completed(user_id, day, exercise_id, total_sets):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO daily_status (user_id, day, exercise_id, completed, approaches_done)
        VALUES (?, ?, ?, 1, ?)
        ON CONFLICT(user_id, day, exercise_id) DO UPDATE SET 
            completed = 1,
            approaches_done = excluded.approaches_done
    """, (user_id, day, exercise_id, total_sets))
    conn.commit()


# ============= ЭТА ФУНКЦИЯ БЫЛА ОТСУТСТВОВАЛА =============
def get_recent_history(user_id, limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT program, day, exercise_id, weight, reps, approaches, date 
        FROM history 
        WHERE user_id=? 
        ORDER BY date DESC LIMIT ?
    """, (user_id, limit))
    results = cursor.fetchall()
    conn.close()

    return [{
        "program": row["program"],
        "day": row["day"],
        "exercise": row["exercise_id"],
        "weight": row["weight"],
        "reps": row["reps"],
        "approaches": row["approaches"],
        "date": row["date"]
    } for row in results]