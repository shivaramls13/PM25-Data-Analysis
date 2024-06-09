import sqlite3
from contextlib import closing

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with closing(sqlite3.connect(self.db_path)) as conn, closing(conn.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pm25_data (
                    device_id TEXT,
                    timestamp TEXT,
                    pm25 REAL,
                    PRIMARY KEY (device_id, timestamp)
                )
            ''')
            conn.commit()

    def insert_data(self, data):
        with closing(sqlite3.connect(self.db_path)) as conn, closing(conn.cursor()) as cursor:
            feeds = data['feeds'][0]['AirBox']
            for entry in feeds:
                for timestamp, record in entry.items():
                    cursor.execute('''
                        INSERT OR IGNORE INTO pm25_data (device_id, timestamp, pm25)
                        VALUES (?, ?, ?)
                    ''', (record['device_id'], timestamp, record['s_d0']))
            conn.commit()

    def fetch_all_data(self):
        with closing(sqlite3.connect(self.db_path)) as conn, closing(conn.cursor()) as cursor:
            cursor.execute('SELECT * FROM pm25_data')
            return cursor.fetchall()
