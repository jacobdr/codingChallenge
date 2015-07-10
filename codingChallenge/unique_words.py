from collections import Counter, OrderedDict
from operator import itemgetter
import tempfile
import numpy as np
from codingChallenge import utils


class UniqueWordsCalculator(object):
    """
    Class container for the functions related to coungint the number of unique
    words as Tweets arrive
    """
    def __init__(self, tweet_iterable):
        self.tweet_iterable = tweet_iterable
        # self.input_file_path = input_file_path

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

    def counter_on_all_words(self):
        with tempfile.TemporaryFile() as tmpfile:
            # Clean each tweet and write it out to the temporary file, with
            # a trailing newline
            for tweet in self.tweet_iterable:
                for word in utils.clean_tweet(tweet).split(" "):
                    tmpfile.write(word + "\n")
            # Make sure that the file is at the beginning and then create a
            # Counter from it to get the unique items
            tmpfile.seek(0)
            count_container = Counter(tmpfile.read().splitlines())

            sorted_count_dictionary = OrderedDict(sorted(count_container.items(),
                                              key=itemgetter(0)))
            return sorted_count_dictionary.items()

    def numpy_count_unique(self):
        tweet_array = np.genfromtxt(self.tweet_iterable, dtype=np.string_,
                                    comments=False, delimiter="\n")
        word_array = np.concatenate([tweet.split() for tweet in tweet_array])
        word_count = Counter(word_array)
        alphabetized_count = OrderedDict(sorted(word_count.items(), key=itemgetter(0)))
        return alphabetized_count.items()


    def run(self):
        """
        Create a generic run method on the object to make reimplemntation
        easier. That way code in the Dispatcher doesn't need to be refactored
        """
        # return self.count_unique()
        return self.numpy_count_unique()

