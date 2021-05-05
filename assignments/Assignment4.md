# Assignment 4: Dataframes and the Naive Bayes classifier

In this assignment, you will use a Naive Bayes classifier to classify the IMDB reviews. Its performance should be significantly better than our "simplistic model" on the training data, though it will still be not too impressive on the test data (it will be 50% accuracy on the test data, so, may as well be tossing a coin!).

The main() function is already provided for you for the most part. Your task is mostly to put the IMDB data into a **dataframe**, such that the data can be vectorized and a classifier can be trained on it. That's what you'll spend most of your time working on in this assignment. 

In addition, we are asking you to think about what the provided code is doing, reviewing the lectures from May 6 and May 11, in particular, and any python documentation that comes with the packages. We are asking you to **add comments** explaining, in your own words, what the code is doing. You do not need to be formal or 100% correct there, but you need to make a good effort.

Look for the TODO items in the skeleton! Make sure you addressed all the TODOs before you submit.

Submit as usual, to your repo which you share with the instructors.

### Summary of input/output:
1. Your main() for this assignment will accept **4 file paths**: to train/pos, train/neg, test/pos, and test/neg.
2. If you did everything as specified (particularly the clean up), then the output should be two numbers. The first number represents the accuracy of the Naive Bayes classifier on the **training data**. The second number is the accuracy on the **test data**. The expected output is:
    ```
    92.464
    50.0
    ```
    (We will not be computing precision and recall for this assignment.)

### Part 1: Installing packages

**Please leave ample time for this, especially if your pip isn't working!**

You will need multiple packages in this assignment. That's great because it means you can write a program which does something complex and get some results without having to write several complex programs first and then to test and debug them for a long time until you fix all the bugs. However, installing packages can sometimes be a pain at first.

1. Make sure you have `pip` working on your machine. First, just type `pip` in command line and if you see `command unrecognized`, then consult this, for example: [https://phoenixnap.com/kb/install-pip-windows](https://phoenixnap.com/kb/install-pip-windows). Sometimes even after you install `pip`, you still get the error message that the command is not recognized. You could try several solutions offered here: [https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command) -- one of them may work. Come to office hours and we can try them together.

2. After pip start working (test with e.g. `pip install numpy`), install the following packages (by typing `pip install [packagename]`):
    1. numpy
    2. pandas
    3. sklearn

    There should be no red error messages, ideally, in your terminal, when you install each.

3.  Import or clone and copy **privately** the skeleton for Assignment 4. It will have all the import statements; run the program and make sure everything gets imported successfully.


### Part 2: Dataframes: Another vector representation

In Assignment 3, we had a class for review vectors. That can be convenient for debugging/thinking about the problem, but in actuality, people usually use tables to store data vectors. Such a table simply contains rows where one of the columns is the gold label and another column represents the data. There may be other columns as well. Columns may have names, which is convenient because then you can access cells in the table by their name. Tables are **fast** to access, so it is important to know how to use them. 

1. Install (via `pip`) and import (in your assignment4.py) the `pandas` module. 

2.  Work on the function createDataFrames(). It should accept the `argv` array and return **two pandas dataframe tables** (see lecture for May 6). Use 1 and 0 for labels where 1 is the "positive" ("good") review label. Use "text" and "label" for column names. NB: It's easy to create a dataframe with the wrong number of columns, and get confused with the column names, so work on this until you have the right result. You should have 25,000 rows and 2 columns in each dataframe.

3. If you print out the dataframe, you should see something like this:

```
   label                                               text
0      1  For a movie that gets no respect there sure ar...
1      1  Bizarre horror movie filled with famous faces ...
2      1  A solid if unremarkable film Matthau as Einste...
3      1  Its a strange feeling to sit alone in a theate...
4      1  You probably all already know this by now but ...
```

-- these are the first five positive reviews from the training data. The first column is just the row's ordinal number.

### Part 3: Understanding and finishing up the main() function.

The main() is almost fully written for you. Only one TODO asks you to add a few simple lines of code. Other TODOs ask you to study the code and the documentation (and the lecture, where appropriate) and leave comments showing your understanding of the material and the program.

1. Find the third TODO in the main():
  ```
     # TODO: Set the below 4 variables to contain:
    # X_train: the training data; y_train: the training data labels;
    # X_test: the test data; y_test: the test data labels.
    # Access the data frames by column names.
  ```
  Uncomment the next 4 lines of code and store the appropriate values in each. This requires thinking about how what the dataframe looks like and how to access columns in it.
  
  After this, the code should start working. It will take it a few minutes to finish. You should now see the correct output!
  
2. Go through all the remaining TODOs, study the function docs where needed, and add comments, where required, explaining in your words what the code is doing. You don't need to be 100% correct or formal, but you need to show effort. The lecture from May 11 should be helpful here.

3. The training accuracy is over 90% yet the test accuracy is at chance level. In the last TODO, add a comment reflecting (briefly) on why that may be.

### Part 4: Submit
1. Add your NetID_assignment4.py to the repo you created in Assignment 1. If you used any other files (other than packages such as numpy, pandas, and sklearn), add them also.
2. Submit the commit number which you would like us to grade, to Canvas.

### You are now done with Assignment 4!
