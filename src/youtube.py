from googleapiclient.discovery import build
import re
from src.db import DB


def save_songs_to_db(api_key, db_name):
    db = DB(db_name)
    service = build('youtube', 'v3', developerKey= api_key)

    request = service.playlists().list(part='contentDetails', channelId='UCj0txYsfVr71bkXAjVWb6NQ', maxResults=50)
    response = request.execute()

    for item in response['items']:
        nextPageToken = None
        while True:
            request = service.playlistItems().list(part='contentDetails, snippet', playlistId=item['id'], maxResults=50, pageToken=nextPageToken)
            try:
                response = request.execute()
            except:
                break

            for item in response['items']:
                desc = item['snippet']['description']
                url = item['contentDetails']['videoId']
                res_list = re.findall('(🎵+ )([\w&\' ]*)', desc)
                if res_list != None:
                    for res in res_list:
                        song = res[1]
                        if song == '':
                            continue
                        db.insert(title=song, url="https://www.youtube.com/watch?v=" + url)
                        print(song + " https://www.youtube.com/watch?v=" + url)
            
            nextPageToken = response.get('nextPageToken')
            if not nextPageToken:
                break

    service.close()
