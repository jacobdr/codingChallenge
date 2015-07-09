import os
import sys

from unique_words import UniqueWordsCalculator
from median_unique import MedianCalculator
from constants import MODULE_ROOT, PROJECT_ROOT, TEST_DIRECTORY
from dispatcher import Dispatcher
import constants

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
        const=sum, default=max,
                   help='sum the integers (default: find the max)')

    path_to_tweets_input = os.path.join(constants.PROJECT_ROOT,
                                        "tweet_input",
                                        "tweets.txt")
    path_to_output_directory = os.path.join(constants.PROJECT_ROOT,
                                            "tweet_output")
    Dispatcher(path_to_tweets_input, path_to_output_directory).run_jobs()
    sys.exit(0)
