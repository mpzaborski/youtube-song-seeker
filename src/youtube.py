from googleapiclient.discovery import build
import re
import time


def print_song_db(api_key):
    service = build('youtube', 'v3', developerKey= api_key)

    request = service.playlists().list(part='contentDetails', channelId='UCj0txYsfVr71bkXAjVWb6NQ', maxResults=50)
    response = request.execute()

    for item in response['items']:
        print(item)
        print()

    nextPageToken = None
    while True:
        request = service.playlistItems().list(part='contentDetails, snippet', playlistId='PLFpQINKjT9QfB-d5NaDjiiC5amxQuDiFq', maxResults=50, pageToken=nextPageToken)
        response = request.execute()

        for item in response['items']:
            desc = item['snippet']['description']
            url = item['contentDetails']['videoId']
            res_list = re.findall('(🎵+ )([\w&\' ]*)', desc)
            if res_list != None:
                for res in res_list:
                    song = res[1]
                    print(song + " https://www.youtube.com/watch?v=" + url)
        
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break
        time.sleep(1)

    service.close()
