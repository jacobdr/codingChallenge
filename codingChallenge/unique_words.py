from collections import Counter, OrderedDict
from operator import itemgetter

from codingChallenge import utils


class UniqueWordsCalculator(object):
    """
    Class container for the functions related to coungint the number of unique
    words as Tweets arrive
    """
    def __init__(self, tweet_iterable):
        self.tweet_iterable = tweet_iterable

    def count_unique(self):
        """
        This is the function documentation
        """
        count_container = Counter()
        for tweet in self.tweet_iterable:
            # Encapsulte tweet in string call and return strip to
            # escape any strange characters
            count_container = count_container + \
                Counter(utils.clean_tweet(tweet).split(" "))

        sorted_count_dictionary = OrderedDict(sorted(count_container.items(),
                                              key=itemgetter(0)))

        # Remove edge cases of blank string or space string
        sorted_count_dictionary.pop(' ', None)
        sorted_count_dictionary.pop('', None)
        return sorted_count_dictionary

