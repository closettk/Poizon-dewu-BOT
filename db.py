#здесь все что связано с бд. tg.db создается сама при первом запуске
import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('handlers/tg.db')
    cur = db.cursor()

    # Добавляем колонку bot_id с автоинкрементом
    cur.execute("""
    CREATE TABLE IF NOT EXISTS profiles(
        bot_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id TEXT UNIQUE)
    """)
    cur.execute("CREATE TABLE IF NOT EXISTS yuan_rate (id INTEGER PRIMARY KEY, rate REAL)")
    db.commit()

async def create_profile(user_id):
    global db, cur
    user = cur.execute("SELECT 1 FROM profiles WHERE user_id = ?", (user_id,)).fetchone()
    if not user:
        # Вставляем только user_id, bot_id будет автоматически увеличиваться
        cur.execute("INSERT INTO profiles (user_id) VALUES (?)", (user_id,))
        db.commit()
        return False  # Пользователь был добавлен
    else:
        return True  # Пользователь уже существует

async def update_yuan_rate(new_rate):
    global db, cur
    db = sq.connect('handlers/tg.db')
    cur = db.cursor()
    cur.execute("INSERT OR REPLACE INTO yuan_rate (id, rate) VALUES (1, ?)", (new_rate,))
    db.commit()
