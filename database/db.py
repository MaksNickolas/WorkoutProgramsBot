import sqlite3
from datetime import datetime

DB_NAME = "progress.db"


def get_connection():
    """Создает подключение к БД"""
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn


def init_db():
    """Создает таблицы при первом запуске"""
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
        exercise TEXT,
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
        exercise TEXT,
        completed BOOLEAN DEFAULT 0,
        approaches_done INTEGER DEFAULT 0,
        PRIMARY KEY (user_id, day, exercise)
    )
    """)

    conn.commit()
    conn.close()


# === РАБОТА С ПОЛЬЗОВАТЕЛЯМИ ===
def get_user_level(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT level FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 1


def set_user_level(user_id, level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO users (user_id, level, last_notification) VALUES (?, ?, ?)",
                   (user_id, level, datetime.now().date()))
    conn.commit()
    conn.close()


def get_last_notification(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT last_notification FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def update_last_notification(user_id, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET last_notification = ? WHERE user_id = ?", (date, user_id))
    conn.commit()
    conn.close()


# === РАБОТА С ИСТОРИЕЙ ===
def save_history(user_id, program, day, exercise, weight, reps, approaches):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO history (user_id, program, day, exercise, weight, reps, approaches, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, program, day, exercise, weight, reps, approaches, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()


def get_last_history(user_id, program, day, exercise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT weight, reps, approaches FROM history 
        WHERE user_id=? AND program=? AND day=? AND exercise=?
        ORDER BY date DESC LIMIT 1
    """, (user_id, program, day, exercise))
    result = cursor.fetchone()
    conn.close()
    return result


def get_recent_history(user_id, limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT program, day, exercise, weight, reps, approaches, date 
        FROM history 
        WHERE user_id=? 
        ORDER BY date DESC LIMIT ?
    """, (user_id, limit))
    result = cursor.fetchall()
    conn.close()
    return result


# === РАБОТА СО СТАТУСОМ ДНЯ ===
def get_daily_status(user_id, day, exercise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT completed, approaches_done FROM daily_status 
        WHERE user_id=? AND day=? AND exercise=?
    """, (user_id, day, exercise))
    result = cursor.fetchone()
    conn.close()
    return result


def update_daily_status(user_id, day, exercise, approaches_done=None, completed=None):
    conn = get_connection()
    cursor = conn.cursor()

    if approaches_done is not None:
        cursor.execute("""
            INSERT INTO daily_status (user_id, day, exercise, approaches_done, completed)
            VALUES (?, ?, ?, ?, 0)
            ON CONFLICT(user_id, day, exercise) DO UPDATE SET approaches_done = approaches_done + 1
        """, (user_id, day, exercise))

    if completed is not None:
        cursor.execute("""
            UPDATE daily_status SET completed = ? WHERE user_id=? AND day=? AND exercise=?
        """, (completed, user_id, day, exercise))

    conn.commit()
    conn.close()


def reset_daily_status(user_id):
    """Очищает статус для нового дня"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM daily_status WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()