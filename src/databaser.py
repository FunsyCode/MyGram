import sqlite3


class Databaser:

    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Videos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            description TEXT,
                            likes INTEGER,
                            comments INTEGER,
                            author TEXT)''')
        
    def add_video(self, description, author):
        self.cursor.execute('''INSERT INTO Videos (description, likes, comments, author) VALUES (?, 0, 0, ?)''', (description, author))
        self.connection.commit()
 
    def get_videos(self):
        self.cursor.execute('''SELECT * FROM Videos''')
        res = self.cursor.fetchall()
        
        res = list(map(dict, res))
        res = sorted(res, key=lambda val: val['likes'], reverse=True)

        return res
    
    def like_video(self, video_id):
        self.cursor.execute('''UPDATE Videos SET likes = likes + 1 WHERE id = ?''', (video_id))
        self.connection.commit()
    
if __name__ == '__main__':
    db = Databaser()
    
    db.add_video('гав мяу', 'funsy') # 1 видео
    db.add_video('не знаю что писать', 'funsy') # 2 видео
    db.add_video('трясем телефон', 'funsy') # 3 видео

    db.like_video('3')
    db.like_video('3')

    db.like_video('1')

    print(db.get_videos())