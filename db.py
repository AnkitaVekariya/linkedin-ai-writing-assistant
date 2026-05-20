import sqlite3
import json


DB_PATH = "database/linkedin_posts.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    return conn


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        text TEXT,

        engagement INTEGER,

        line_count INTEGER,

        language TEXT,

        length TEXT,

        tags TEXT
    )
    """)

    conn.commit()

    conn.close()


def insert_posts(json_path):

    conn = get_connection()

    cursor = conn.cursor()

    with open(json_path, encoding="utf-8") as f:

        posts = json.load(f)

        for post in posts:

            cursor.execute("""
            INSERT INTO posts (

                text,
                engagement,
                line_count,
                language,
                length,
                tags

            )

            VALUES (?, ?, ?, ?, ?, ?)
            """, (

                post.get("text"),

                post.get("engagement"),

                post.get("line_count"),

                post.get("language"),

                post.get("length"),

                ",".join(post.get("tags", []))
            ))

    conn.commit()

    conn.close()


def view_posts():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")

    rows = cursor.fetchall()

    for row in rows:

        print(row)

    conn.close()


if __name__ == "__main__":

    create_table()

    insert_posts("data/processed_posts.json")

    view_posts()