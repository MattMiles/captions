import re
import sys
import praw

def get_subreddits_from_config():
    with open('praw.ini') as config:
        try:
            return re.search(r'\nsubreddits=(([\w]+,?)+)', config.read()) \
                .group(1).split(',')
        except AttributeError:
            print('Error: missing subreddits in praw.ini. See README.md for more details.')
            sys.exit(1)

def is_youtube_url(url):
    # compatible YouTube URL formats:
    # https://www.youtube.com/watch?v=###########
    # https://youtu.be/###########
    YOUTUBE_PATTERN = re.compile(
        r'^(https?:\/\/)?(((www\.|m\.)?youtube.com\/watch(\?v=(?P<id>.{11}))|(\?.+=.+))|((www\.)?youtu\.be\/(?P<shortened_id>.{11})(.+=.+)?))$'
    )
    return re.match(YOUTUBE_PATTERN, url)

def get_youtube_video_id(url_match):
    return url_match.group('id') or url_match.group('shortened_id')

def initialize_praw():
    reddit = praw.Reddit('captions-reddit', user_agent='reddit-captions-bot')

    subreddits_from_config = get_subreddits_from_config()
    subreddits = reddit.subreddit('+'.join(subreddits_from_config))

    return reddit, subreddits

if __name__ == '__main__':
    reddit, subreddits = initialize_praw()

    for submission in subreddits.stream.submissions():
        try:
            match = is_youtube_url(submission.url)

            if match:
                video_id = get_youtube_video_id(match)
                
        except praw.exceptions.PRAWException as e:
            print(e)
