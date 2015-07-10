import numpy as np
from codingChallenge import utils


class MedianCalculator(object):
    """
    Class used to abstract the calculation of the median
    """
    def __init__(self, tweet_input):
        self.tweet_iterable = []
        # Handle the edge case where a single tweet is supplied as a string,
        # not an array iterable
        if type(tweet_input) == str:
            self.tweet_iterable = [tweet_input]
        else:
            self.tweet_iterable = tweet_input
        self.num_unique_words_sorted = []
        self.median_list = []

    def format_to_two_decimal(self, input_amount):
        formatted_string = "{0:.2f}".format(input_amount)
        return float(formatted_string)

    def append_to_unique_word_list(self, tweet):
        tweet_unique_words = len(set(tweet.split()))
        self.num_unique_words_sorted.append(tweet_unique_words)
        self.num_unique_words_sorted = sorted(self.num_unique_words_sorted)

    def populate_median_list(self):
        for dirty_tweet in self.tweet_iterable:
            tweet = utils.clean_tweet(dirty_tweet)
            self.append_to_unique_word_list(tweet)
            current_number_of_tweets = len(self.num_unique_words_sorted)
            # Condition if odd amount
            if current_number_of_tweets % 2:
                index = current_number_of_tweets / 2
                self.median_list.append(self.num_unique_words_sorted[index])
            # Condition if even amount
            else:
                left_index = (current_number_of_tweets / 2) - 1
                right_index = current_number_of_tweets / 2

                average_of_medians = self.format_to_two_decimal(
                    (self.num_unique_words_sorted[left_index] +
                     self.num_unique_words_sorted[right_index]) / 2.0)
                self.median_list.append(average_of_medians)

        return self.median_list

    def numpy_calculate_median(self):
            tweet_array = np.genfromtxt(self.tweet_iterable, dtype=np.string_,
                                        comments=False, delimiter="\n")
            tweet_bag_of_words = np.array([tweet.split() for tweet in tweet_array])
            running_list_of_uniques = np.empty(0)
            running_list_of_median = np.empty(0)
            for tweet in tweet_bag_of_words:
                filtered_tweet_length = np.unique(tweet).size
                running_list_of_uniques = np.append(running_list_of_uniques,
                                                    filtered_tweet_length)
                running_list_of_median = np.append(running_list_of_median,
                                                   np.median(running_list_of_uniques))
            return running_list_of_median

    def run(self):
        """
        Run methods necessary to return the array of medians.

        The run method helps abstract away the calling of the methods so that
        less refacotring is needed later on.
        """
        return self.numpy_calculate_median()




