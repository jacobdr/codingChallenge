import sys
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand


# from pip.req import parse_requirements

# # parse_requirements() returns generator of pip.req.InstallRequirement objects
# path_to_requirements = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#     "requirements.txt")
# install_reqs = parse_requirements(path_to_requirements)
# reqs = [str(ir.req) for ir in install_reqs]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name="codingChallenge",
    version="0.0.1",
    author="Jacob Roberts",
    author_email="jacobdr@gmail.com",
    url="https://github.com/jacobdr/codingChallenge",
    description="Hoping to win the challenge with this submission \
        that should run fast",
    packages=["codingChallenge"],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    install_requires=["numpy"]
)
