import SentimentData as sdc
import TweetAnalysisUtil as ta
import TwitterClient as tc
import LogAssist
from datetime import datetime as dta
from time import sleep
import sys

def runSent(sent_data, query):
    """

    :param sent_data: The filename for the sentiment dictionary
    :param query: The query to search
    :return: A list containing the positive percentage and the negative percentage
    """
    dt = dta.now()
    day = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)
    log_file = query + day + ".txt"
    client = tc.TwitterClient()
    client.connect()
    tweets = ta.parseSearchResultsForText(client.search(query))

    pos_count = 0
    neg_count = 0
    for tweet_text in tweets:
        if ta.isApplicable(tweet_text, sent_data, 2):
            mean_valence = ta.calculateTweetValence(tweet_text, sent_data)
            if (mean_valence > 5.5):
                #NOTE: 5.5 IS COMPLETELY ARBITRARY. RECOMMEND IMPLEMENTING SYSTEM TO DETERMINE AVERAGE
                #FOR A SPECIFIC SEARCH QUERY AND DECIDE AGAINST THAT
                pos_count += 1
            if (mean_valence < 5.5):
                neg_count += 1
    pos_per = int((pos_count / (pos_count + neg_count)) * 100)
    neg_per = int((neg_count / (pos_count + neg_count)) * 100)
    return [pos_per, neg_per]

def main(argv):
    usg_str = "usage: [query] [sentiment dictionary file] [sleep value] [log_file]"
    if len(argv) != 5:
        print(usg_str)
        exit(0)

    query = argv[1]
    sent_file = argv[2]
    sleep_val = int(argv[3])
    log_file = argv[4]

    sd = sdc.SentimentData(sent_file)
    hold_data = sd.getSentimentData()

    while True:
        data = runSent(hold_data, query)
        sentiment_data = str(data[0]) + "%P " + str(data[1]) + "%N"
        LogAssist.logData(sentiment_data, log_file)
        LogAssist.printData(sentiment_data)
        sleep(sleep_val)

main(sys.argv)