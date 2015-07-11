# Insight codingChallenge -- Submission by Jacob Roberts

## Summary
The purpose of this project is to compute two features -- a list of unique words and their respective frequencies, and a running median of the unique number of words per tweet -- from a given set of input tweets. 

## Documentation
** CURRENTLY NOT IMPLEMENTED **  
[Read The Docs](http://codingchallenge.readthedocs.org/en/master)

## Setup + Processing of Files from the input_text Directory
```bash
git clone https://github.com/jacobdr/codingChallenge
cd codingChallenge
pip install -r requirements.txt
source run.sh
```

## Testing  
#### Preferred Method  
`nosetests`  
#### Verbose Output + PDB Debugging  
`py.test -vv --pdb`  

## API  
__It should be noted that old implementaions of the UniqueWordsCalculator and MedianCalculaotr have not been cleaned from each of the class source files so that improvement can be assessed without having to checkout old version tags. However, the the fastest implementation for each of the classes is used in the UniqueWorldsCalculator.run() and MedianCalculator.run() methods__  

###  Dispatcher  
This class is meant to coordinate the actions of the two feature creation
classes.

It exposes a Dispatcher.run_jobs() instantiates each of the two feature creation classes (UniqueWordsCalculator and MedianCalculator) and calls their .run() methods. The return values from these .run() calls are then written to the feature output file.

    Dispatcher(path_to_input_tweet_file, path_to_output_directory)
    
    Initialization Arguments:

    path_to_input_tweet_file (file descriptor, or other iterable): Input file of tweets to create features for  
    
    path_to_output_directory (string, ideally absolute filepath): Directory to write the feature files to   

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

    Examples:
        Dispatcher("codingChallenge/benchmark/data/100k_tweets.txt", "codingChallenge/benchmark/output/")

        Dispatcher("codingChallenge/benchmark/data/100k_tweets.txt", "codingChallenge/benchmark/output/").run_jobs()

###  UniqueWordsCalculator + MedianCalculator  
Each of the above are implemented as a class that take only one argument in order to instantiate them, which is an iterable object. In the case of an input tweets.txt file, this iterable is a file descriptor created with an open() system call. They each expose a .run() method, which then call to whichever method is currently in vogue. The source code has not been cleaned of old implementations
  

## TODO Improvements For Future Versions
*  Expanded test coverage:
    - Currently, the only major tests provided are copied directly from the [cc-example respository](https://github.com/InsightDataScience/cc-example), with additional integration tests added to make sure that the Dispatcher() class successfully coordinated the other classes responsible for actually dealing with feature creation. Ideally in the future the testing suite would include better tests of edge cases, such as:
        + Tweets of only one word or one letter
        + Tweets with strange combinations of string delimiters, like single- and double-quotation marks
*  Pipelining:
    - The current implemenation treates each feature as a independent entities, so that the input tweets.txt file is read twice -- once by each class responsible for creating a feature. 
    - A future version should try to benchmark a different implemntation that uses streaming updating, so that a tweet would first be passed to the UniqueWords calculator (which would update the word counts for words already seen, or append new words to the list), and then from there directly passed to the MedianCalculator
    - Such an implementation would help reduce memory pressure and eliminate the overhead of file I/O, especially when it is redundant
*  Threading:
    -  Right now the Dispatcher.run_jobs() method runs sequentially. There is no reason for this since the operations are indepndent. With trivial effort this could be re-implemented using threading, so that the total run-time would be bound by the slower of the two processes, rather than the summation of the two proccesses' runtimes
*  Median Calculation:
    -  The median calculation methodology is taking much longer than I would like, and could stand to be improved by a better algorithm. A future developer might want to look into a min-max heap implementation, which might be more efficient than falling back on the iterative update used at present

## Development Diary
* Step 1: Unit Tests - TDD
    - Duplicate the example listed on the [Insight challenge Github page](https://github.com/InsightDataScience/cc-example) so that our initial code fails
    - Goal was to use the "Red, Green, Re-factor" Approach to development
* Step 2: Python "Batteries Only" Version
    - Initial versions of the two classes that calculate features used only standard python modules, largely the Collections() data structure. 
* Step 3: Python profiling
    - Used the Python "profile" module to understand which functions were contributing most to runtime
    - Results of each version of the program can be found in the benchmarks/stats directory
    - Input data was initally only 1k tweets, but as performance improved I moved to standardizing performance tests around the processing of 100k Tweets
* Step 4: "Numpy-ing" The Code
    - Numpy uses optimized C-code for efficient vector and matrix calculations -- though I utilized its features for efficient array creation, insertion, and summary statistic calculation

## Performance
Stats directory: /Users/Jacob/Documents/Projects/DataInsight/codingChallenge/benchmark/stats  

*  **v0.2:**

    -  1k_tweets:
        +  Dispatcher.run_jobs()
            *  Time: 15.016 seconds
        +  Dispatcher.run_Median
            *  0.080 seconds
        +  Dispatcher.run_Unique
            *  15.273 seconds
        +  Path: /Users/Jacob/Documents/Projects/DataInsight/codingChallenge/benchmark/stats/v0.2_1kTweets.txt
    -  10k_tweets:
        +  Unable to run
    -  
* **v0.3:**
    -  1k_tweets:
        +  Dispatcher.run_Unique
            *  15.339 seconds
* **v0.4:**
    - 100k_tweets
        + Dispatcher.run_Median
            * 119.033 seconds
        + Dispatcher.run_Unique
            * 18.454 seconds
* **v0.5:**
    - 100k_tweets
    - Dispathcer.run_Median
        + Dispathcer.run_Median
* **v0.6**:
    - 100k_tweets
        + Dispatcher.run_Median
            * 98.216 seconds 
        + Dispatcher.run_Unique
            * 17.694 seconds
        + Dipatcher._run_jobs
            * 117.778 seconds

## Requirements + Environment
### Requirements:
* Python 2.7.x
* Numpy
```
ProductName:    Mac OS X
ProductVersion: 10.10
BuildVersion:   14A389
```

## Sources of Test Tweet Data:
http://help.sentiment140.com/for-students



