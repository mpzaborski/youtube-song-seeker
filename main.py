from src.youtube import save_songs_to_db
from src.db import DB
import os

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    save_songs_to_db(api_key, "songs.db")
    
    # db = DB("songs.db")
    # db.select("I like You")