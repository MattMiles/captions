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
    reddit = praw.Reddit('captions', user_agent='reddit-captions-bot')

main()