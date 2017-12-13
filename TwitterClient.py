import tweepy

class TwitterClient:
    def __init__(self):
        self.api = None

    def connect(self, consumer_token="YOUR CONSUMER TOKEN", consumer_secret='YOUR CONSUMER SECRET',
                access_token='YOUR ACCESS TOKEN', access_secret='YOUR ACCESS SECRET'):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        if not (api.verify_credentials()):
            print("Could not verify!")
            exit(1)
        else:
            self.api = api
            return api


    def search(self, _query, _count=100):
        """
        A method to run a search against Twitter's api
        :param _query: The query terms to run
        :param _count: The number of results to return, up to 100
        :return: The results of the search in JSON format
        """
        #TODO: Research the effects of different result types. Tweet limit of 100 for mixed and recent, 15 for popular
        results = self.api.search(_query, result_type='mixed', count=_count)
        return results