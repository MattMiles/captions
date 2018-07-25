import unittest

from googleapiclient.errors import HttpError

import youtube
import youtube_authentication

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT = youtube_authentication.get_authenticated_service()

class TestYouTubeHelpers(unittest.TestCase):
    def test_get_caption_data(self):
        # valid ID, language
        self.assertEqual(
            youtube.get_caption_data(CLIENT, 'en', 'CfW845LNObM')['id'],
            'Y4cNahXxFX7EJdhVKn9QNafunsWE3co00MOOuXqwYvE='
        )

        # invalid language
        self.assertRaises(
            ValueError, 
            youtube.get_caption_data, CLIENT, 'invalid-lang', 'CfW845LNObM'
        )

        # invalid video ID
        self.assertRaises(
            HttpError,
            youtube.get_caption_data, CLIENT, 'en-US', 'invalid-id'
        )
    
    def test_download_caption_track(self):
        # valid caption id
        res = youtube.download_caption_track(CLIENT, 'Y4cNahXxFX7EJdhVKn9QNafunsWE3co00MOOuXqwYvE=')
        self.assertTrue(
                res.startswith(r'b"0:00:03.620,0:00:07.859\npicture yourself as an early calculus')
        )

        # invalid caption id
        self.assertRaises(
            HttpError,
            youtube.download_caption_track, CLIENT, 'invalid-id'
        )

        # 403 Forbidden (user disallows on video)
        self.assertRaises(
            HttpError,
            youtube.download_caption_track, CLIENT, 'mW6hFttt_KE'
        )

if __name__ == '__main__':
    unittest.main()
