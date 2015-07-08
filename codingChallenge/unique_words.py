from collections import Counter
from operator import itemgetter


class UniqueWords():
    """
    Class container for the functions related to coungint the number of unique
    words as Tweets arrive
    """
    def count_unique(self, input_tweet_array):
        """
        This is the function documentation
        """
        count_container = Counter()
        for tweet in input_tweet_array:
            count_container = count_container + Counter(tweet.split(" "))

        sorted_count_dictionary = dict(sorted(count_container.items(),
                                       key=itemgetter(0)))

        # Remove edge cases of blank string or space string
        sorted_count_dictionary.pop(' ', None)
        sorted_count_dictionary.pop('', None)
        return sorted_count_dictionary
