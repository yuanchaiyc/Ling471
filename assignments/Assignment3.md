## Assignment 3

### Attention

A [detailed walkthrough](Assignment3-hints.md) is available for Parts 2 and 3. It is located in a **separate file**, to keep this file shorter.

### Summary

In this assignment, you will continue developing a movie review classifier. Mostly, you will be practicing **evaluating** a system. In particular, you will compute **accuracy**, **precision**, and **recall** of the simplistic "system" you built in Assignment 2.

You will start with the code you submitted for Assignment 2 and will develop it further so that it now processes a series of files. You will represent the files as **labeled data points**. With those labels in hand, you will be able to run the simplistic prediction system on all of the files, compare the predicted labels with the actual labels, and compute the performance metrics.

After we are sure we know how to process multiple files, store the data as vectors and compute things, we will leave our `simplisticPrediction()` behind and will proceed with deploying more sophisticated (off-the-shelf) techniques on our data. (That is, assignments 4 and 5 will involve more sophisticated methods.)

**Spec:** After you are done, your program should do the following:

1. Accept two filepaths as input, one the first one for postive (training) files and the second one for negative (training) files.
2. Output **5 numbers** in the **exact** order specified below in Part 3 Step 2.

**Do not output any text**; we need just the numbers, for faster grading. 

We should be able to run your program in command line as follows: `python netID_assignment3.py path_to_the_pos_dir path_to_the_neg_dir`. It's a good idea to test it out in command line before you submit.

Below you will find the assignment description in several parts. If you are not sure how to do something, please make sure to also consult the [detailed walkthrough for Parts 2 and 3](Assignment3-hints.md). That walkthrough is not the only way of doing things; it is intended as helpful though. Ask questions!

Just one **hint for everyone**: Make it so your program **only pays attention to files with the .txt extension** and ignores everything else which may have ended up in the directory! Consult the lecture on the `glob()` method for a `Path` object or read the `pathlib` documentation for more information on this. If using the `sys.os.path` module to work with file paths, you may want to use a list comprehension to filter out files that do not end with `.txt` as a file extension.

As before, you will **submit** your final version to the repository you created for the class in Assignment 1, and you will submit the commit number to Canvas, for time stamp, grading, and feedback.

### Part 1: Assignment 2 clean-up/fixes and Setup

1. Address any comments you received for Assignment 2 (if you already got it back), or otherwise make sure your Assignment 2 program is working correctly.

2. Update your copy of the class repo with `git pull` to download the information for Assignment 3. You will need to copy the assignment 3 information over into the private repo you made the class. Make sure to not publicly publish any solutions to this assignment anywhere, including but not limited to GitHub.

3. You will find **two files** in the skeleton directory: evaluation.py and review_vector.py, as well as a folder for a tiny test dataset. Now **add** a copy your Assignment2 python program  to your **private** repo in which you will work on Assignment 3. **Rename** it appropriately: yourNetID_assignment3.py.

### Part 2: Running simplistic prediction on many files

1. Refactor your assignment3.py program so that your main() function iterates over all files in both train/pos and train/neg directories, outputting a prediction for each file.

### Part 3: Computing accuracy, and computing precision and recall

1. Compute **accuracy, precision, and recall** of your system. The acuracy is for the overall system while precision and recall are **with respect to** (wrt) positive and negative review classes, **separately**. The NONE predictions should be counted as mistakes (think carefully here!).

2. At the end of your program, output **5 numbers, one per line, rounded to 4 decimal points,** in the **exact** following order: 
    1. Overall system accuracy
    2. Precision wrt positive (training) reviews
    3. Recall wrt positive (training) reviews
    4. Precision wrt negative (training) reviews,
    5. Recall wrt positive (training) reviews. 
    
    **Do not output any text**; we need just the numbers, for faster grading.
    
    You can use the python built-in round() function to round up the floats. Read the Python documentation on it for more details.
    
    The **expected output** is:

    ```
    0.2751
    0.5558
    0.3214
    0.8072
    0.2287
    ```


### Part 4: Error analysis

1. Take note of 5 positive and 5 negative reviews which were classified incorrectly. (You can collect the filenames for which the prediction is incorrect, in a list, and then inspect it in the debugger.) Inspect the contents of these 10 files. What do you notice? What kind of phenomena (syntactic, semantic) can you observe which led to your system mistaking a good review for a bad review, and vice versa? 

2. Why do you think the precision is so much better than the recall?

3. Why do you think the precision for negative reviews may be so much better than for positive reviews?

4. Summarize your findings in a text file called `yourNetID_EA_assignment3.txt` and add it your repository. If you wish, you may instead use [Markdown formatting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for this file; if you do so, please call the file `yourNetID_EA_assignment3.md`.

### Part 5 Submit

1. **Link** to the commit you want us to grade **in the repository which you created for Assignment 1**. In that repository, we should be able to find:
    1. **yourNetID_assignment3.py** 
    2. Any files that **yourNetID_assignment3.py** imports (for example, the **evaluation.py** and **review_vector.py**, if you imported functions from these files. If you had all the functions written in the main python file, and didn't import functions from any external files, then just the **yourNetID_assignment3.py** is sufficient.)
    3. **yourNetID_EA_assignment3.txt** (or .md).


# You are now done with Assignment 3!

In the remaining couple of assignments, we will only be using our `simplisticPrediction()` as a **baseline**. In other words, we will use more sophisticated models (including off-the-shelf models) and compare their performance to each other and to our simplistic procedure. The purpose of writing `simplisticPrediction()` ourselves was mostly to practice basic programming.

