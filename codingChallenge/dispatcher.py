import os
import csv
from codingChallenge import UniqueWordsCalculator, MedianCalculator, constants


class Dispatcher(object):
    """
    .. autoclass:: Dispatcher

    This class is meant to coordinate the actions of the two feature creation
    classes.

    Initialization Arguments:

    :param path_to_input_tweet_file: Input file of tweets to create features for
    :type path_to_input_tweet_file: file descriptor or other iterable
    :param path_to_output_directory: Directory to write the feature files to
    :type path_to_output_directory: string, ideally absolute filepath

    Methods:

    run_jobs():
        The only real important publicly accessible method. Calling run_jobs()
        instantiates each of the two feature creation classes (UniqueWordsCalculator
        and MedianCalculator) and calls their .run() methods. The return values from
        these .run() calls are then written to the feature output file.

    run_UniqueWordsCalculator():
        Generates output for the ft1.txt file -- which is an alphabetical list
        of unique words found in all of the input tweets and these words
        corresponding counts. The ft1.txt file gets written to the directory
        specificed by the second argument when the Dispatcher() class is initaited

    run_MedianCalculator():
        Generates output for the ft2.txt file -- which is a running median calculation
        of the unique words as all tweets get procssed. This ft2.txt file gets written
        to the directory specified by the second argument when the Dispatcher() class
        is initiated


    .. function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings
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
        """
        Call the UniqueWordsCalculator .run() method, and return the
        alphabetical-sorted list (items of an OrderedDict) of unique words

        Creates an iterable from the tweets.txt input file, instantiates the
        UniqueWordsCalculator with this iterable, and then calls the objects
        run method. Takes returned dictionary from run and writes it to
        "ft1.txt" file
        """
        ft1_file_path = os.path.join(self.output_file_directory, "ft1.txt")
        with open(self.input_file_path, 'r') as tweet_file:
            with open(ft1_file_path, 'w') as ft1_output:
                # words_writer = csv.writer(ft1_output, delimiter=' ',
                                          # lineterminator="\n")
                list_of_unique_words = UniqueWordsCalculator(tweet_file).run()
                for word, count in list_of_unique_words:
                    ft1_output.write(word + ' ' + str(count) + '\n')

    def run_MedianCalculator(self):
        """
        Call the MedianCalculator .run() method, write its returned array of
        medians to a file called "ft2.txt"

        Creates an iterable from the tweets.txt input file, instantiates the
        MedianCalculator with this iterable, and then calls the objects
        run method. Takes return list from run and writes it to "ft2.txt" file
        """
        ft2_file_path = os.path.join(self.output_file_directory, "ft2.txt")
        with open(self.input_file_path, 'r') as tweet_file:
            with open(ft2_file_path, 'w') as ft2_output:
                list_of_medians = MedianCalculator(tweet_file)\
                    .run()
                for median in list_of_medians:
                    ft2_output.write("{:.2f}".format(median) + "\n")

    def run_jobs(self):
        """
        The .run_jobs() method is the real workhorse of the API. It calls out to the
        .run_UniqueWordsCalculator() and .run_MedianCalculator() methods, which in turn
        instantiate the respective classes that generate the features, in addition to
        handing the file I/O of reading tweets and writing the features
        """
        self.run_UniqueWordsCalculator()
        self.run_MedianCalculator()
