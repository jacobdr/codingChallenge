import os
import sys

from unique_words import UniqueWordsCalculator
from median_unique import MedianCalculator
from constants import MODULE_ROOT, PROJECT_ROOT, TEST_DIRECTORY
from dispatcher import Dispatcher
from utils import constants

if __name__ == "__main__":
    path_to_tweets_input = os.path.join(constants.PROJECT_ROOT,
                                        "tweet_input",
                                        "tweets.txt")
    path_to_output_directory = os.path.join(constants.PROJECT_ROOT,
                                            "tweet_output")
    Dispatcher(path_to_tweets_input, path_to_output_directory).run_jobs()
    sys.exit(0)
