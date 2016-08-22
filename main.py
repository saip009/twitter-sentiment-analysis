import re

def processTweet (tweet):

    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')

    return tweet

    #end

stopwords = []

def replaceTwoOrMore(tweet):
    pattern = re.compile

tweets_file = open('data/sampleTweets.txt', 'r')
line = tweets_file.readline()

while line:
    preprocessedTweet = processTweet(line)
    print preprocessedTweet
    line = tweets_file.readline()

tweets_file.close()