from src.youtube import print_song_db
import os

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    print_song_db(api_key)