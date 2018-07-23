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

def main():
    reddit = praw.Reddit('captions-reddit', user_agent='reddit-captions-bot')

    subreddits = get_subreddits_from_config()
    subreddit = reddit.subreddit('+'.join(subreddits))

    # compatible YouTube URL formats:
    # https://www.youtube.com/watch?v=###########
    # https://youtu.be/###########
    youtube_pattern = re.compile(
        r'^(https?:\/\/)?(((www\.|m\.)?youtube.com\/watch(\?v=(?P<id>.{11}))|(\?.+=.+))|((www\.)?youtu\.be\/(?P<shortened_id>.{11})(.+=.+)?))$'
    )

    for submission in subreddit.stream.submissions():
        try:
            match = re.match(youtube_pattern, submission.url)

            if match:
                video_id = match.group('id') or match.group('shortened_id')
                
        except praw.exceptions.PRAWException as e:
            print(e)

main()
