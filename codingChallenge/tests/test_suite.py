# -*- coding: utf-8 -*-
import os
# import sys
import unittest
import pytest
import filecmp
import shutil
# from collections import Counter

# pylint: disable=W391

from codingChallenge.unique_words import UniqueWordsCalculator
from codingChallenge.median_unique import MedianCalculator
from codingChallenge.dispatcher import Dispatcher
from codingChallenge import constants

# CONSTANTS
# TESTING_DIRECTORY_ABS_PATH = os.path.dirname(os.path.realpath("__file__"))
TESTING_DIRECTORY_ABS_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
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


@pytest.fixture
def insight_github_unique_word_results():
    """
    Test fixture that represents the alphabetized count of words from Tweets
    taken from the Insight Github page
    """
    counter_container = {}

    path_to_input_file = os.path.join(TESTING_DIRECTORY_ABS_PATH,
                                      "fixtures/ft1_expected_results_v1.txt")
    with open(path_to_input_file) as input_file:
        for line in input_file:
            word, count = line.split()
            counter_container[word] = int(count)
    return counter_container


@pytest.fixture(scope="class")
def sessiondir(request):
    session_path = os.path.join(constants.TEST_DIRECTORY, "fixtures",
                                "tmpOutput")
    os.mkdir(session_path)

    def fin():
        shutil.rmtree(session_path)
    request.addfinalizer(fin)
    return session_path


@pytest.fixture(scope="class")
def run_dispathcer(sessiondir):
    job_manager = Dispatcher(sessiondir)
    job_manager.run_jobs()
    return job_manager


class TestUniqueWords(unittest.TestCase):
    """
    Tests for the first feature ("ft1") case
    """
    def test_insight_github_unique_all_tweets(self):
        counting_machine = UniqueWordsCalculator()
        word_count = counting_machine.count_unique(
            original_three_tweets())
        assert word_count == insight_github_unique_word_results()


class TestMedianCount(unittest.TestCase):
    """
    Tests for the second feature ("ft2") case
    """
    all_three_input_tweets = original_three_tweets()
    case1 = all_three_input_tweets[0]
    case2 = all_three_input_tweets[0:2]
    case3 = all_three_input_tweets

    case1_test = MedianCalculator(case1)
    assert case1_test.populate_median_list()[-1] == 11

    case2_test = MedianCalculator(case2)
    assert case2_test.populate_median_list()[-1] == 12.5

    case3_test = MedianCalculator(case3)
    assert case3_test.populate_median_list()[-1] == 14


@pytest.mark.usefixtures("run_dispathcer")
@pytest.mark.usefixtures("sessiondir")
class TestDispatcher(unittest.TestCase):
    """
    Tests for correct input + output to the filesystem
    """

    # Compare the number of files
    def test_num_files(self, run_dispathcer, sessiondir):
        assert os.listdir(sessiondir) == 2

    # Compare the content of the files
    def test_ft1_file_contents_equality(self, run_dispathcer, sessiondir):
        ft1_test_fixture_path = os.path.join(constants.TEST_DIRECTORY,
                                             "fixtures",
                                             "tweet_output",
                                             "ft1.txt")

        ft1_dispath_result_path = os.path.join(sessiondir,
                                               "ft1.txt")
        assert True == filecmp.cmp(ft1_test_fixture_path,
                                   ft1_dispath_result_path)

    def test_ft2_file_contents_equality(self, run_dispathcer, sessiondir):
        ft2_test_fixture_path = os.path.join(constants.TEST_DIRECTORY,
                                             "fixtures",
                                             "tweet_output",
                                             "ft2.txt")

        ft2_dispath_result_path = os.path.join(sessiondir,
                                               "ft2.txt")
        assert True == filecmp.cmp(ft2_test_fixture_path,
                                   ft2_dispath_result_path)






