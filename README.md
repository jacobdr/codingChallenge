# Insight Coding Challenge -- Submission by Jacob Roberts

## 

## Development Diary
* Step 1: Unit Tests - TDD
    - Duplicate the example listed on the [Insight challenge Github page](https://github.com/InsightDataScience/cc-example) so that our initial code fails

http://help.sentiment140.com/for-students

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

IMPROVEMNETS
* Expanded test coverage
* Pipeline testing 



python setup.py install --user
