import re

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

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
    client = get_authenticated_service()

    caption_id = get_caption_data(client, 'en', 'CfW845LNObM')['id']

    print(download_caption_track(client, caption_id))