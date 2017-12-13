"""
A utility to analyze aspects of a given tweet using supplied sentiment data
"""

import SentimentData as sdc

def isApplicable(tweet, data, limit):
    """
    Determines if a tweet should be factored into calculations about the sentiment surrounding a search term
    :param tweet: Text of a tweet
    :param data: An object of type SentimentData
    :param limit: The number of words inside the tweet which must also be accounted for in data
    :return: A bool on if the word should be factored into overall calculations or not
    """
    count = 0
    for word in tweet.split():
        if data.containsEntry(word):
            count += 1
    return count >= 2

def parseSearchResultsForText(results):
    ret_list = []
    for tweet in results:
        ret_list.append(tweet._json['text'])
    return ret_list

def calculateTweetValence(tweet, data):
    """
    Calculates the mean valence of a given tweet
    :param tweet: The text of a tweet
    :param data: A SentimentData object containing information about the sentiment surrounding a group of words
    :return:
    """
    tweet = tweet.lower()
    applicable_words = []
    tweet_word_arr = tweet.split()

    for word in tweet_word_arr:
        if data.containsEntry(word):
            applicable_words.append(word)

    total_valence = 0

    #TODO: Implement mean calculations that take standard deviation into account
    for word in applicable_words:
        total_valence += float(data.getEntry(word)['valence_mean'])

    return round(total_valence / len(applicable_words), 2)

def calculateTweetArousal(tweet, data):
    """
    Calculates the mean arousal of a tweet
    :param tweet: The text of a tweet
    :param data: A SentimentData object containing information about the sentiment surrounding a group of words
    :return:
    """
    tweet = tweet.lower()
    applicable_words = []
    tweet_word_arr = tweet.split()

    for word in tweet_word_arr:
        if data.containsEntry(word):
            applicable_words.append(word)

    if len(applicable_words) < 2:
        return -1

    total_arousal = 0

    # TODO: Implement mean calculations that take standard deviation into account
    for word in applicable_words:
        total_arousal += float(data.getEntry(word)['arousal_mean'])

    return round(total_arousal / len(applicable_words), 2)

