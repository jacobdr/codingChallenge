"""
Declare useful constants for use throughout the project
"""

import os

absolute_path_to_file = os.path.abspath(__file__)
MODULE_ROOT = os.path.dirname(absolute_path_to_file)
PROJECT_ROOT = os.path.dirname(MODULE_ROOT)
TEST_DIRECTORY = os.path.join(MODULE_ROOT, "tests")

if __name__ == "__main__":
    print "__file__ is: {0}".format(__file__)
    print "MODULE_ROOT is: {0}".format(MODULE_ROOT)
    print "PROJECT_ROOT is: {0}".format(PROJECT_ROOT)
    print "PROJECT_ROOT is: {0}".format(TEST_DIRECTORY)
