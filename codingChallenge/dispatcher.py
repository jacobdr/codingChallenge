import os
import csv

from codingChallenge import UniqueWordsCalculator, MedianCalculator


class Dispatcher(object):
    """
    This class is meant to coordinate the actions of the other two classes
    """
    def __init__(self, path_to_input_tweet_file):
        # Convert input file path to absolute as a sanity check
        if os.path.isabs(path_to_input_tweet_file):
            self.input_file_path = path_to_input_tweet_file
        else:
            self.input_file_path = os.path.abspath(path_to_input_tweet_file)

    def run_jobs(self):
        pass

