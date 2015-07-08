# -*- coding: utf-8 -*-
import os
import sys
import unittest
import pytest


from codingChallenge import unique_words


@pytest.fixture
def small_input_tweets():
    return ["tweet 1", "tweet 2"]


class TestUniqueWords(unittest.TestCase):
    def test_method(self):
        word_count = unique_words.count_unique(small_input_tweets)
        assert word_count == 3
