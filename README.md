# Twitter Sentiment Analysis Engine

A basic Python sentiment analysis tool based on tweets collected about a certain phrase.

## Usage
Before using, be sure to put your own default Twitter client token, client key, access token, and access key into TwitterClient.py. If you do not have any of those, you
can snag some [here](https://developer.twitter.com/)
```
python Engine.py [search query] [sentiment dictionary]
```

A basic sentiment dictionary (BRM-emot-submit.csv) is provided courtesy of Warriner AB, Kuperman V, and Brysbaert M as part of their 
published [collection of norms of valence, arousal, and dominance for 13,915 English lemmas](https://www.ncbi.nlm.nih.gov/pubmed/23404613). 

### Prerequisites

```
Python 3.0 or higher
```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

## Acknowledgments

* [The Tweepy library](http://www.tweepy.org/)
* Dictionary authors Warriner AB, Kuperman V, and Brysbaert M

