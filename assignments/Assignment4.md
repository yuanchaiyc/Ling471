[Home](../index.md)

# Assignment 4: Dataframes and the Naive Bayes classifier

In this assignment, you will use a Naive Bayes classifier to classify the IMDB reviews. Its performance should be significantly better than our "simplistic model".

The main() function is already provided for you for the most part. Your task is mostly to put the IMDB data into a **dataframe** (an object from the popular data science package called "pandas"), such that the data can be fed to off-the-shelf packages. That's what you'll spend most of your time working on in this assignment, and that's very normal for data science to spend lots of time on formatting the data such that a package accepts it. 

In addition, we are asking you to think about what the provided code in main() is doing, reviewing the lectures from May 6 and May 11 as well as any python documentation that comes with the packages. We are asking you to **add comments** explaining, in your own words, what the code is doing. You do not need to be formal or 100% correct there, but you need to make a good effort. 

Look for the **TODO items** in the skeleton! Make sure you addressed **all** the TODOs before you submit. 

We will not be doing any error analysis this time, mainly because we won't really look at which words the classifier deemed most informative, so it would be complete guess work to try and reason why some of the reviews were misclassified. Of course you are welcome to look into the mistakes and to share your thoughts on the Discussion Board! As for most informative words, we will try to look into that in the last assignment.

Submit as usual, to your repo which you share with the instructors, and a commit number to Canvas.

### Summary of input/output:

1. Your main() for **Part 1** for this assignment will accept **4 file paths**: to train/pos, train/neg, test/pos, and test/neg. The result of running it should be creating a new .csv file.

2. Your main() for **Part 2** will accept a filename (you will be passing it the file you created in Part 1).

3. The output of Part 2 should look as follows:
    ```
    Train accuracy:                 0.9736
    Train precision positive:       0.9833
    Train recall positive:          0.9635
    Train precision negative:       0.9642
    Train recall negative:          0.9836
    Test accuracy:                  0.8697
    Test precision positive:        0.9011
    Test recall positive:           0.8305
    Test precision negative:        0.8428
    Test recall negative:           0.9089    
    ```
    
    Tne numbers may vary slightly but only very, very slightly, e.g. they should definitely be within a percent.
    
### Part 0: Getting the skeleton and installing packages

1. Set up a **private** repository to work on this assignment. Some options are listed here. You can download the skeleton repository and copy it to your submission repository (but then the instructors will see all your commits; it is not a problem for us though so long as you do not add other collaborators to the repository). Alternatively, import or otherwise privately copy the repository we created for Assignment 4 setup. Please **do not fork** (that has privacy issues because it turns out forks are public). To import, go to https://github.com/new/import and enter the assignment 4 url: `https://github.com/olzama/Ling471-SP2021-HW4`. Make sure to create a private repo at this step. In any case, please **make sure to not publish any solutions to this assignment anywhere, including but not limited to GitHub**.

2. Make sure you have `pip` working on your machine (e.g. run `pip install pandas` and see if pip actually runs). If you have issues (`pip is not recognized`), please consult the Discussion board ("Logistics and General Questions"); some solutions are provided there.

3. After pip starts working, install the following packages (by typing `pip install [packagename]`):
    1. pandas (Documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
    2. scikit-learn (Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)

    There should be no red error messages, ideally, in your terminal, when you install each.

4. The skeleton contains several import statements. If you installed the packages and are using the same version of python in VS Code that you have in the terminal, VS Code should not complain about the import statements at this point.

### Part 1: Putting the IMDB data into a pandas DataFrame and saving the result as a CSV file

In Assignment 3, we had a class for review vectors. That can be convenient for debugging/thinking about the problem (and we had to learn about classes!), but in actuality, people usually use tables to store data vectors. Such a table simply contains rows where one of the columns is the gold label and another column represents the data. There may be other columns as well. Columns may have names, which is convenient because then you can access cells in the table by their name. Tables are **fast** to access, so it is important to know how to use them. 

**NB**: If you look on Canvas --> Files, you will see a .csv file there called `imdb_master.cvs`. That file is similar in format to what we ask you to produce (but it has 100,000 rows instead of 50,000). You may look at it for reference and test the code in Part 2 with it, if you like. You will still be graded for whether your code for Part 1 works though, separately! We could just use that file directly but the goal is to learn how to **create** such files when they are not available.

1.  Work on `imdb_dataframe_skeleton.py` until you have successfully created a .csv file which contains **all the data in one table**. In particular, there are **three columns** which you must have, and they are the label of the review, the "type" (train or test), and the review itself (its text). You may add more columns if you find them helpful, such as the file name ("file" in the example below). You may call the columns whatever you like so long as you use them correctly in Part 2. However, as for the values, you must **use 1 and 0 for labels** where 1 is the "positive" ("good") review label and 0 is the "negative" ("bad") label. You also **should not modify the review text** apart from the usual clean up that you did for Assignment 3. You should have 50,000 rows in the resulting dataframe.

3. If you print out the dataframe, you should see something like this:

    ```
              file  label  type                                             review
    0   1821_4.txt      0  test  Alan Rickman Emma Thompson give good performan...
    1   9487_1.txt      0  test  I have seen this movie and I did not care for ...
    2   4604_4.txt      0  test  In Los Angeles the alcoholic and lazy Hank Chi...
    3   2828_2.txt      0  test  This film is bundled along with Gli fumavano l...
    4  10890_1.txt      0  test  I only comment on really very good films and o...
    ```

    -- these are the first five negative reviews from the test data. You may put training data first, but then make sure to read it in appropriately in Part 2. Once again, **make sure** you have **label, type, and review** columns in place and with the appropriate values. The table may look different in other respects.

4. Make sure to **save the result in a file** so that you don't have to redo this step every time you test your Part 2 program. This line of code is already included in the skeleton. The file will appear in your working directory. You can change this if you like!
 
### Part 2: Understanding and finishing up the main() function.

The main() in the skeleton is mostly written for you. Only a couple TODOs ask you to add a few lines of code. Other TODOs ask you to study the code and the documentation (and the lecture, where appropriate) and leave comments showing your understanding of the material.

1. Figure out what is missing in the code and work on it until it starts working. If you are not getting correct results (or very close to correct results), investigate (with our help). It's mainly reading data in correctly, storing the right things in each variable, and then at the end computing the metrics (using the code you wrote for Assignment 3).

2. Once the code is working and you are satisfied with the results, go through all the remaining TODOs, study the function docs where needed, and add comments, where required, explaining in your words what the code is doing. You don't need to be 100% correct or formal, but you need to show effort. The lecture from May 11 should be helpful here.


### Part 3: Submit
1. Rename your files appropriately: `UWNetID_imdb_dataframe.py` and `UWNetID_assignment4.py` and add them to the repo you created in Assignment 1. If you used any other files (other than packages such as numpy, pandas, and sklearn), add them also.
2. Submit the commit number which you would like us to grade, to Canvas.

### You are now done with Assignment 4!

[Home](../index.md)
