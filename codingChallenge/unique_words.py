from collections import Counter
from operator import itemgetter


class UniqueWordsCalculator(object):
    """
    Class container for the functions related to coungint the number of unique
    words as Tweets arrive
    """
    # def __init__(self, ):

    def count_unique(self, tweet_iterable):
        """
        This is the function documentation
        """
        count_container = Counter()
        for tweet in tweet_iterable:
            count_container = count_container + Counter(tweet.split(" "))

        sorted_count_dictionary = dict(sorted(count_container.items(),
                                       key=itemgetter(0)))

        # Remove edge cases of blank string or space string
        sorted_count_dictionary.pop(' ', None)
        sorted_count_dictionary.pop('', None)
        return sorted_count_dictionary

