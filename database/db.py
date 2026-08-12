import sqlite3
from datetime import datetime
import threading

DB_NAME = "progress.db"
_db_local = threading.local()


# === ПОДКЛЮЧЕНИЕ К БД ===
def get_connection():
    """Одно подключение на поток (для скорости)"""
    if not hasattr(_db_local, "connection"):
        _db_local.connection = sqlite3.connect(DB_NAME, check_same_thread=False)
        _db_local.connection.row_factory = sqlite3.Row
    return _db_local.connection


# === ИНИЦИАЛИЗАЦИЯ ТАБЛИЦ ===
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        level INTEGER DEFAULT 1,
        last_notification DATE
    )
    """)

    # Таблица истории тренировок
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

    # Таблица статуса текущего дня
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

    # Индексы для ускорения запросов
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_user_date ON history(user_id, date DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_user_program_day ON history(user_id, program, day)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_daily_status_user_day ON daily_status(user_id, day)")

    conn.commit()
    print("✅ База данных инициализирована")


# === ПОЛЬЗОВАТЕЛИ ===
def get_user_level(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT level FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result["level"] if result else 1


def set_user_level(user_id, level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, level, last_notification) 
        VALUES (?, ?, ?)
    """, (user_id, level, datetime.now().date()))
    conn.commit()


def get_last_notification(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT last_notification FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result["last_notification"] if result else None


def update_last_notification(user_id, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET last_notification = ? WHERE user_id = ?", (date, user_id))
    conn.commit()


# === ИСТОРИЯ ===
def save_history(user_id, program, day, exercise, weight, reps, approaches):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO history (user_id, program, day, exercise, weight, reps, approaches, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, program, day, exercise, weight, reps, approaches, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()


def get_last_history(user_id, program, day, exercise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT weight, reps, approaches FROM history 
        WHERE user_id=? AND program=? AND day=? AND exercise=?
        ORDER BY date DESC LIMIT 1
    """, (user_id, program, day, exercise))
    result = cursor.fetchone()
    return result if result else None


def get_recent_history(user_id, limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT program, day, exercise, weight, reps, approaches, date 
        FROM history 
        WHERE user_id=? 
        ORDER BY date DESC LIMIT ?
    """, (user_id, limit))
    return cursor.fetchall()


# === СТАТУС ДНЯ ===
def get_daily_status(user_id, day, exercise):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT completed, approaches_done FROM daily_status 
        WHERE user_id=? AND day=? AND exercise=?
    """, (user_id, day, exercise))
    result = cursor.fetchone()
    return result if result else None


def update_daily_status(user_id, day, exercise, approaches_done=None, completed=None):
    conn = get_connection()
    cursor = conn.cursor()

    if approaches_done is not None:
        cursor.execute("""
            INSERT INTO daily_status (user_id, day, exercise, approaches_done, completed)
            VALUES (?, ?, ?, 1, 0)
            ON CONFLICT(user_id, day, exercise) DO UPDATE SET approaches_done = approaches_done + 1
        """, (user_id, day, exercise))

    if completed is not None:
        cursor.execute("""
            UPDATE daily_status SET completed = ? 
            WHERE user_id=? AND day=? AND exercise=?
        """, (completed, user_id, day, exercise))

    conn.commit()


def reset_daily_status(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM daily_status WHERE user_id=?", (user_id,))
    conn.commit()


# === ПРОВЕРКА ВСЕХ УПРАЖНЕНИЙ ДНЯ ===
def get_day_completion(user_id, program, day):
    """Возвращает список упражнений с их статусом"""
    from data.programs import PROGRAMS  # импорт внутри, чтобы избежать циклических ссылок

    conn = get_connection()
    cursor = conn.cursor()
    exercises = PROGRAMS.get(program, {}).get(day, [])

    result = []
    for ex in exercises:
        if ex['sets'] > 0:
            cursor.execute("""
                SELECT completed FROM daily_status 
                WHERE user_id=? AND day=? AND exercise=?
            """, (user_id, day, ex['name']))
            status = cursor.fetchone()
            result.append({
                "name": ex['name'],
                "completed": status["completed"] if status else False
            })
    return result


def is_day_complete(user_id, program, day):
    """Проверяет, все ли упражнения дня выполнены"""
    for item in get_day_completion(user_id, program, day):
        if not item["completed"]:
            return False
    return True