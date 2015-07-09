# -*- coding: utf-8 -*-
import os
# import sys
import unittest
import pytest
import filecmp
import shutil
from collections import OrderedDict
from operator import itemgetter
from collections import Counter
import difflib

# pylint: disable=W391

from codingChallenge.unique_words import UniqueWordsCalculator
from codingChallenge.median_unique import MedianCalculator
from codingChallenge.dispatcher import Dispatcher
from codingChallenge import constants


@pytest.fixture(scope="class")
def original_three_tweets():
    """
    Test fixture that represents the three orignal Tweets from the Insight
    Github page as an array
    """
    test_tweets = [
        "is #bigdata finally the answer to end poverty? \
        @lavanyarathnam http://ow.ly/o8gt3 #analytics",
        "interview: xia wang, astrazeneca on #bigdata and the promise of effective \
        healthcare #kdn http://ow.ly/ot2uj",
        "big data is not just for big business. on how #bigdata is being deployed for \
        small businesses: http://bddy.me/1bzukb3 @cxotodayalerts #smb"
    ]
    return test_tweets


@pytest.fixture(scope="class", autouse=True)
def insight_github_unique_word_results():
    """
    Test fixture that represents the alphabetized count of words from Tweets
    taken from the Insight Github page
    """
    counter_container = OrderedDict()

    path_to_input_file = os.path.join(constants.TEST_DIRECTORY,
                                      "fixtures/ft1_expected_results_v1.txt")
    with open(path_to_input_file, 'r') as input_file:
        for line in input_file:
            word, count = line.split()
            counter_container[word] = int(count)
    return counter_container


@pytest.fixture()
def sessiondir():
    session_path = os.path.join(constants.TEST_DIRECTORY, "fixtures",
                                "tmpOutput")
    os.mkdir(session_path)

    return session_path


@pytest.fixture()
def run_dispathcer(input_path, output_path):
    job_manager = Dispatcher(input_path, output_path)
    job_manager.run_jobs()
    return job_manager


@pytest.mark.usefixtures("insight_github_unique_word_results",
                         "original_three_tweets")
class TestUniqueWords(unittest.TestCase):
    """
    Tests for the first feature ("ft1") case
    """
    def test_insight_github_unique_all_tweets(self):
            input_tweets = original_three_tweets()
            insight_results = insight_github_unique_word_results()
            counting_machine = UniqueWordsCalculator(input_tweets)
            assert counting_machine.count_unique() == insight_results


@pytest.mark.usefixtures("original_three_tweets")
class TestMedianCount(unittest.TestCase):
    """
    Tests for the second feature ("ft2") case
    """

    def test_one_tweet(self):
        case1 = original_three_tweets()[:1]
        case1_test = MedianCalculator(case1)
        assert case1_test.populate_median_list()[-1] == 11

    def test_two_cumulative_tweets(self):
        case2 = original_three_tweets()[:2]
        case2_test = MedianCalculator(case2)
        assert case2_test.populate_median_list()[-1] == 12.5

    def test_three_cumulative_tweets(self):
        case3 = original_three_tweets()
        case3_test = MedianCalculator(case3)
        assert case3_test.populate_median_list()[-1] == 14


class TestDispatcher(unittest.TestCase):
    """
    Tests for correct input + output to the filesystem
    """
    @classmethod
    @pytest.mark.usefixtures("run_dispathcer", "sessiondir")
    def setup_class(cls):
        cls.input_dir = os.path.join(constants.TEST_DIRECTORY, "fixtures",
                                     "tweet_input", "tweets.txt")
        cls.output_dir = sessiondir()
        cls.dispatched = run_dispathcer(cls.input_dir, cls.output_dir)

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls.output_dir)

    def test_num_files(self):
        assert len(os.listdir(TestDispatcher.output_dir)) == 2

    # Compare the content of the files
    def test_ft1_file_contents_equality(self):
        ft1_test_fixture_path = os.path.join(constants.TEST_DIRECTORY,
                                             "fixtures",
                                             "tweet_output",
                                             "ft1.txt")

        ft1_dispath_result_path = os.path.join(TestDispatcher.output_dir,
                                               "ft1.txt")
        test_result = filecmp.cmp(ft1_test_fixture_path,
                                  ft1_dispath_result_path, shallow=False)
        assert test_result

        # with open(ft1_test_fixture_path, 'r') as official_result,\
        #         open(ft1_dispath_result_path) as computed_result:
        #         diff = difflib.Differ()
        #         differences = list(diff.compare(official_result.readlines(),
        #                      computed_result.readlines()))
        # assert len(differences) == 0

    def test_ft2_file_contents_equality(self):
        ft2_test_fixture_path = os.path.join(constants.TEST_DIRECTORY,
                                             "fixtures",
                                             "tweet_output",
                                             "ft2.txt")

        ft2_dispath_result_path = os.path.join(TestDispatcher.output_dir,
                                               "ft2.txt")
        test_result = filecmp.cmp(ft2_test_fixture_path,
                                  ft2_dispath_result_path, shallow=False)
        assert test_result

        # with open(ft2_test_fixture_path, 'r') as official_result,\
        #     open(ft2_dispath_result_path) as computed_result:
        #         diff = difflib.Differ()
        #         differences = list(diff.compare(official_result.readlines(),
        #                            computed_result.readlines()))
        #         assert len(differences) == 0







