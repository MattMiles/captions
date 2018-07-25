import unittest

from main import is_youtube_url

class TestMain(unittest.TestCase):
    def test_is_youtube_url(self):
        # base URLs
        self.assertTrue(is_youtube_url('https://www.youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('https://youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('http://www.youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('http://youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('www.youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('youtube.com/watch?v=mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('https://youtu.be/mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('http://youtu.be/mW6hFttt_KE'))
        self.assertTrue(is_youtube_url('youtu.be/mW6hFttt_KE'))

        # with params
        self.assertTrue(is_youtube_url('https://www.youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('https://youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('http://www.youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('http://youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('www.youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('youtube.com/watch?v=mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('https://youtu.be/mW6hFttt_KE?t=23'))
        self.assertTrue(is_youtube_url('http://youtu.be/mW6hFttt_KE&t=23'))
        self.assertTrue(is_youtube_url('youtu.be/mW6hFttt_KE&t=23'))

        # invalid URLs
        self.assertFalse(is_youtube_url('https://youtube.com'))
        self.assertFalse(is_youtube_url('https://youtube.com/watch'))
        self.assertFalse(is_youtube_url('https://google.com'))
        
if __name__ == '__main__':
    unittest.main()
    