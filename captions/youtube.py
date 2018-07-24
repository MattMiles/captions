import re

import youtube_authentication

from googleapiclient.errors import HttpError

def download_caption_track(client, caption_id, **kwargs):
    return client.captions().download(
        id=caption_id,
        **kwargs
    ).execute()

def get_caption_data(client, tlang, videoId, **kwargs):
    res = client.captions().list(
        part=kwargs.get('part', 'snippet'),
        videoId=videoId,
        **kwargs
    ).execute()

    for caption in res['items']:
        if re.match(r'^{}(-.*)*$'.format(tlang), caption['snippet']['language']):
            return caption

    raise ValueError(f'No track found for {videoId} with the specified language {tlang}.')

if __name__ == '__main__':
    client = youtube_authentication.get_authenticated_service()

    caption_id = get_caption_data(client, 'en', 'CfW845LNObM')['id']

    print(download_caption_track(client, caption_id))