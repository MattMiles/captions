import praw
import requests

def main():
    reddit = praw.Reddit('captions', user_agent='reddit-captions-bot')

main()