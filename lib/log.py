import sqlite3
from datetime import datetime
import logging


class Log:

    def __init__(self):

        self.db = sqlite3.connect('event.db')

        c = self.db.cursor()

        try:
            c.execute("""
                CREATE TABLE event(id INTEGER PRIMARY KEY NOT NULL,
                    date DATE,
                    class TEXT NOT NULL,
                    message TEXT NOT NULL);
            """)
            c.execute("""create index event_date ON event (date);""")
            c.execute("""create index event_class ON event (class);""")

        except sqlite3.OperationalError:
            pass

    def event(self, cls, message):

        c = self.db.cursor()
        c.execute("""
            INSERT INTO event(date, class, message) VALUES (?, ?, ?)
        """, [datetime.now(), cls, message])

        self.db.commit()

        logging.info("event: %s: %s" % (cls, message))

    def get_events(self, count=30, page=0):

        offset = page * count

        c = self.db.cursor()
        c.execute("""
            select id, date, class, message from event order by date desc limit {count} offset {offset}
        """.format(count=count,
                   offset=offset))

        return [{"id": id, "date": date, "class": cls, "message": message} for id, date, cls, message in c.fetchall()]


log = Log()
