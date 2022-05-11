# Assignment 4: Dataframes and the Naive Bayes classifier

In this assignment, you will use a Naive Bayes classifier to classify the IMDB reviews. Its performance should be significantly better than our "simplistic model".

The main() function is already provided for you for the most part. Your task is mostly to put the IMDB data into a `DataFrame` from `pandas`, such that the data can be fed to off-the-shelf packages. That's what you'll spend most of your time working on in this assignment, and that's very normal for data science to spend lots of time on formatting the data such that a package accepts it. 

In addition, we are asking you to think about what the provided code in `main()` is doing, reviewing relevant lectures from, as well as any python documentation that comes with the packages. We are asking you to **add comments** explaining, in your own words, what the code is doing. You do not need to be formal or 100% correct there, but you need to make a good effort. **You will lose points if you do not add these comments!**

Look for the **TODO items** in the skeleton! Make sure you have addressed **all** the TODOs before you submit. 

We will not be doing any error analysis this time, mainly because we won't really look at which words the classifier deemed most informative. As such, it would be complete guess work to try and reason why some of the reviews were misclassified. Of course, you are welcome to look into the mistakes and to share your thoughts on the Discussion Board! As for most informative words, we will try to look into that in the last assignment.

Submit as usual, to your repo which you share with the instructors, and a commit number to Canvas.

### Summary of input/output:

1. Your `main()` for **Part 1** for this assignment will accept **4 file paths**: to train/pos, train/neg, test/pos, and test/neg. The result of running it should be creating a new .csv file.

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
    
    Tne numbers may vary slightly but only very, very slightly, e.g. they should definitely be within a percent. That is, if you subtract your number from the target number, the absolute value of the resulting number should <= 0.01.
    
    For example, if you got 0.9771 for train accuracy, the absolute difference is `abs(0.9736 - 0.9771)`, which is 0.0035. This difference is <= 0.01, so it would be accepted. However, if you got 0.9502, the difference is 0.0234, which is not <= 0.01, so we would interpret this result as (partially) incorrect.
    
### Part 0: Getting the skeleton and installing packages

1. Run `git pull` in your copy of the class repository to get the skeleton files downloaded. Then, either set up a new project in PyCharm with these files or add them to an existing project. Please **make sure to not publish any solutions to this assignment anywhere, including but not limited to GitHub**.

2. In PyCharm, install `pandas` and `scikit-learn` for your project, if you have not already.

### Part 1: Putting the IMDB data into a pandas DataFrame and saving the result as a CSV file

In Assignment 3, we had a class for review **vectors**. That can be convenient for debugging/thinking about the problem (and we had to learn about classes!), but in actuality, people usually use **tables** to store data vectors. Such a table simply contains **rows** where one of the columns is the **gold label** and another column represents the **data**. There may be other columns as well. Columns may have names, which is convenient because then you can **access** cells in the table directly by their name (and row number). Tables are **fast** to access, so it is important to know how to use them. 

**NB**: If you look on Canvas --> Files, you will see a .csv file there called `my_imdb.cvs`. That file is **similar in format** to what we ask you to produce. You may look at it **for reference** and **test the code** in Part 2 with it, if you like. You will still be **graded for whether your code for Part 1 works** though, separately! (As for the uploaded file, we could just use that file directly but the goal is to learn how to **create** such files when they are not available.)

1.  Work on `imdb_dataframe_skeleton.py` until you have successfully created a .csv file which contains **all the data in one table**. In particular, there are **three columns** which you must have, and they are the label of the review, the "type" (train or test), and the review itself (its text). You may add more columns if you find them helpful, such as the file name ("file" in the example below). You may call the columns whatever you like so long as you use them correctly in Part 2. However, as for the values, you may **use 1 and 0 for labels** where 1 is the "positive" ("good") review label and 0 is the "negative" ("bad") label. Or, you may use textual labels like "pos" and "neg" or "good" and "bad". Many packages expect numbers, but scikit-learn seems to be able to handle textual labels. You also **should not modify the review text** apart from the usual clean up that you did for Assignment 3. You should have 50,000 rows in the resulting dataframe.

3. If you print out the dataframe, you should see something like this:

    ```
              file  label  type                                             review
    0   1821_4.txt      0  test  Alan Rickman Emma Thompson give good performan...
    1   9487_1.txt      0  test  I have seen this movie and I did not care for ...
    2   4604_4.txt      0  test  In Los Angeles the alcoholic and lazy Hank Chi...
    3   2828_2.txt      0  test  This film is bundled along with Gli fumavano l...
    4  10890_1.txt      0  test  I only comment on really very good films and o...
    ```

    -- these are the first five negative reviews from the test data. Your `label` column may say "neg", "bad", or similar. You may put training data first, but then make sure to read it in appropriately in Part 2. Once again, **make sure** you have **label, type, and review** columns in place and with the appropriate values. The table may look different in other respects.

4. Make sure to **save the result in a file** so that you don't have to redo this step every time you test your Part 2 program. This line of code is already included in the skeleton. The file should appear in your working directory.
 
### Part 2: Understanding and finishing up the main() function.

The `main()` function in the skeleton is mostly written for you. Only a couple TODOs ask you to add a few lines of code. Other TODOs ask you to study the code and the documentation (and the lecture, where appropriate) and leave comments showing your understanding of the material.

1. Figure out what is missing in the code and work on it until it starts working. If you are not getting correct results (or very close to correct results), investigate with the debugger or ask for help. Your task is mainly about reading data in correctly, storing the right things in each variable, and then at the end computing the metrics (using the code you wrote for Assignment 3).

2. Once the code is working and you are satisfied with the results, go through all the remaining TODOs, study the function docs where needed, and add comments, where required, explaining in your words what the code is doing. You don't need to be 100% correct or formal, but you need to show effort. Some lecture material may be helpful here too.


### Part 3: Submit
1. Rename your files appropriately: `UWNetID_imdb_dataframe.py` and `UWNetID_assignment4.py` and add them to the repo you created in Assignment 1. If you used any other files (other than packages such as numpy, pandas, and sklearn), add them also.
2. Submit the commit number which you would like us to grade, to Canvas.

### You are now done with Assignment 4!
