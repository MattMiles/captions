import unittest

import main

class TestMain(unittest.TestCase):
    def test_is_youtube_url(self):
        # base URLs
        self.assertTrue(
            main.is_youtube_url('https://www.youtube.com/watch?v=mW6hFttt_KE') and
            main.is_youtube_url('https://youtube.com/watch?v=mW6hFttt_KE') and
            main.is_youtube_url('http://www.youtube.com/watch?v=mW6hFttt_KE') and
            main.is_youtube_url('http://youtube.com/watch?v=v=mW6hFttt_KE') and
            main.is_youtube_url('www.youtube.com/watch?v=mW6hFttt_KE') and
            main.is_youtube_url('youtube.com/watch?v=v=mW6hFttt_KE') and
            main.is_youtube_url('https://youtu.be/mW6hFttt_KE') and
            main.is_youtube_url('http://youtu.be/mW6hFttt_KE') and
            main.is_youtube_url('youtu.be/mW6hFttt_KE')
        )

        # with params
        self.assertTrue(
            main.is_youtube_url('https://www.youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('https://youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('http://www.youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('http://youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('www.youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('youtube.com/watch?v=mW6hFttt_KE&t=23') and
            main.is_youtube_url('https://youtu.be/mW6hFttt_KE?t=23') and
            main.is_youtube_url('http://youtu.be/mW6hFttt_KE&t=23') and
            main.is_youtube_url('youtu.be/mW6hFttt_KE&t=23')
        )

if __name__ == '__main__':
    unittest.main()