from contextlib import contextmanager
import sqlite3


class Database:

    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER
            )
        """)

    def get_all(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def get(self, id: int):
        self.cur.execute("SELECT * FROM books WHERE id = ?", (id,))
        row = self.cur.fetchone()
        return self._row_to_dict(row) if row else None

    def create(self, item):
        self.cur.execute("SELECT MAX(id) FROM books")
        result = self.cur.fetchone()
        new_id = (result[0] or 0) + 1

        self.cur.execute("""
            INSERT INTO books VALUES (:id, :title, :author, :year)
        """, {"id": new_id, **item.model_dump()})

        self.conn.commit()
        return new_id

    def update(self, id: int, item):
        self.cur.execute("""
            UPDATE books
            SET title = :title, author = :author, year = :year
            WHERE id = :id
        """, {"id": id, **item.model_dump()})

        self.conn.commit()
        return self.get(id)

    def delete(self, id: int):
        self.cur.execute("DELETE FROM books WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def _row_to_dict(self, row):
        return {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "year": row[3]
        }


@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()
    db.create_table()
    try:
        yield db
    finally:
        db.close()