import os
import csv
from codingChallenge import UniqueWordsCalculator, MedianCalculator, constants


class Dispatcher(object):
    """
    This class is meant to coordinate the actions of the other two classes
    """
    def __init__(self, path_to_input_tweet_file, path_to_output_directory):
        # Convert input file path to absolute as a sanity check
        if os.path.isabs(path_to_input_tweet_file):
            self.input_file_path = path_to_input_tweet_file
        else:
            self.input_file_path = os.path.abspath(path_to_input_tweet_file)

        # Convert output file path to absolute as a sanity check
        if os.path.isabs(path_to_output_directory):
            self.output_file_directory = path_to_output_directory
        else:
            self.output_file_directory = os.path.abspath(
                path_to_output_directory)

    def run_UniqueWordsCalculator(self):
        ft1_file_path = os.path.join(self.output_file_directory, "ft1.txt")
        with open(self.input_file_path, 'r') as tweet_file:
            with open(ft1_file_path, 'w') as ft1_output:
                words_writer = csv.writer(ft1_output, delimiter=' ',
                                          lineterminator="\n")
                list_of_unique_words = UniqueWordsCalculator(tweet_file)\
                    .count_unique().items()
                for word in list_of_unique_words:
                    words_writer.writerow(word)
    def run_MedianCalculator(self):
        ft2_file_path = os.path.join(self.output_file_directory, "ft2.txt")
        with open(self.input_file_path, 'r') as tweet_file:
            with open(ft2_file_path, 'w') as ft2_output:
                list_of_medians = MedianCalculator(tweet_file)\
                    .populate_median_list()
                for median in list_of_medians:
                    ft2_output.write(str(median) + "\n")

    def run_jobs(self):
        self.run_UniqueWordsCalculator()
        self.run_MedianCalculator()
