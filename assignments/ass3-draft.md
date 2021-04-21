## Assignment 3

### Summary

In this assignment, you will continue developing a movie review classifier. Mostly, you will be practicing **evaluating** a system. In particular, you will compute **accuracy** and **precision and recall** of the simplistic "system" you built in Assignment 2.

You will start with the code you submitted for Assignment 2 and will develop it further so that it now processes a bunch of files. You will represent the files as **labeled data points.** With that in hand, you will be able to run the simplistic prediction system on all of the files, compare the predicted labels with the actual labels, and compute the performance metrics.

After we are sure we know how to process multiple files, store the data as vectors and compute things, we will leave our simplisticPrediction() behind and will proceed with deploying more sophisticated (off-the-shelf) techniques on our data.

As before, you will submit your final version to the repository you created for the class in Assignment 1, and you will submit the commit number to Canvas, for time stamp.

### Part 1: Assignment 2 clean-up/fixes and Setup
1. Address any comments you received for Assignment 2 (if you already got it back), or otherwise make sure your Assignment 2 program is working correctly.

2. Fork the repository we created for Assignment 3 setup. You will find **two files** there: evaluation.py and review_vector.py. Now **add** a copy your Assignment2 python program  to your private repo in which you will work on Assignment 3. **Rename** it appropriately: yourNetID_assignment3.py.

### Part 2: Running simplistic prediction on many files
1. **Refactor** your assignment3.py program so that the simplisticPrediction function now accepts a **file name** as the sole argument and returns a prediction. This means that most of the work that the main() function was previously doing in HW2 will now be done **in** the simplisticPrediction() function. At this stage, the input and output of the whole program should still be the same as for Assignment 2 (a file name, for input, and a printed statement about that file, outputting the prediction). So, you are passing your main() a filename via launch.json (in debugging more) or settings.json (in non-debugging mode), and then you are just passing that same filename **further along**, to simplisticPrediction(). simplisticPrediction() then **does all the work to output the prediction, including opening the file**.

2. Create an empty directory somewhere on your machine (**NOT** within your dataset folder). **Copy** the same data file you were using for Assignment 2 (train/pos/1_7.txt) into that directory. This will be your **test** directory for a short while. It's crucial to **start small** before you tackle many files, or you'll get too confused. However **don't mess with the original dataset directory structure**. No new files/directories there.

3. Now, instead of passing your main() function a filename, pass it that new **directory** name. At this point, your program will **stop working**. Don't panic; the next step will fix it.

4. Review the lecture about the python **pathlib** module. In your main() function, write a loop which iterates over all files in the directory whose name was passed as the argument to main(). In the loop, call the simplisticPrediction() function on the file. For now, the loop will only run **once**, since there is only a single file in your test directory. This is your chance to calmly explore what's happening.

5. Step through the entire execution and make sure the program processes the sole file in the test directory correctly (and outputs POSITIVE, as before).

6. Now, replace the path that you are giving to your main function by the **path to all the TRAINING POSITIVE files** in the dataset. So, train/pos on Mac or train\\\pos\\\ on Windows. Observe the program output predictions for all the files in that folder! There is a lot of files, so, it will take the program a while to print all the outputs. (Consider [setting up settings.json](vscode_settings_json.md) and running the program in non-debug mode at this point, unless you actually want to debug.)

7. Add a second argument to your main() in launch.json (and settings.json, if you are using it as well); this second argument will be the path to all NEGATIVE TRAIN files in the dataset. Add another for-loop which processes all negative files before or after processing all positive ones. You should see lots of printed output sentences, one for each file.

### Part 3: Review vectors ###
1. You will probably find it helpful to store the data as instances of the review_vec class, which you downloaded along with evaluation.py from the forked repository. Import this class into your assignment3.py file and write two for-loops, one which goes over each positive review and one which goes over each negative review, and stores the text contents of each review along with the gold label for it in a list of review_vecs. Use this list of review_vecs in Part4. It will probably be less confusing than trying to manipulate the texts and the labels separately.

### Part 4: Computing accuracy, and computing precision and recall
1. Compute the accuracy of your system. Consult the function spec which you will find in evaluation.py. You can implement your function there and import it in your assignment3.py file. The accuracy of your system is the percentage, how many files it got correct. For now, have your program output the accuracy in a sentence: "The accuracy of Simplistic Prediction is X" -- just to see things working. Count NONE predictions as **mistakes** in this step. At this point, **comment out or delete** the print statements you had for each file and only output the accuracy in one sentence at the end.

2. Compute **precision** and **recall** with respect to positive and negative reviews, separately. Consult the function spec which you will find in evaluation.py. You can implement your function there and import it in your assignment3.py file. Review carefully what precision and recall are, in the lecture and reading. **NB**: the terms "positive" and "negative" may introduce **confusion**, because precision and recall is often talked about in the terms of "true/false positive/negative". Take your time to make sure you treat the terms appropriately. E.g., if a negative review is classified NEG, then, with respect to negative review class, this is a TRUE POSITIVE! (Yes, confusing. A common problem in data science, too :) ). The key here is to think about positive and negative reviews absolutely **separately**, as if they had nothing to do with each other. It might help to mentally "rename" positive and negative reviews in "good" and "bad" reviews; that'll make it easier for you not to confuse the review labels with the types of error.

3. Go over your code, cleaning it up as needed. **In particular, remove absolutely all print statements at this point**. This is **important for our grading procedure**. 

4. At the end of your program, output **5 numbers, one per line** in the **exact** following order: 
    1. Overall system accuracy
    2. Precision wrt positive (training) reviews
    3. Recall wrt positive (training) reviews
    4. Precision wrt negative (training) reviews,
    5. Recall wrt positive (training) reviews. 
    
    **Do not output any text**; we need just the numbers, for faster grading.
    
5. **At the end,** your main() should do the following:
    1. Accept two filepaths, one for postive (training) files and one for negative (training) files.
    2. Output **5 numbers** in the **exact** order specified above in Step 4.

The **expected output** is:

```
0.2751
0.2942
0.3214
0.2521
0.2287
```


### Part 5: Error analysis

1. Take note of 5 positive and 5 negative reviews which were classified incorrectly. (You can collect the filenames for which the prediction is incorrect, in a list, and then inspect it in the debugger.) Inspect the contents of these 10 files. What do you notice? What kind of phenomena (syntactic, semantic) can you observe which led to your system mistaking a good review for a bad review, and vice versa? The precision for negative reviews is much lower than for positive; upon inspecting the files, why do you think that is? 

2. Why do you think the precision and recall for positive reviews are better than for negative reviews?

3. Summarize your findings in a text file called `error_analysis.txt` and add it to the repository.

# You are now done with Assignment 3!

In the remaining couple of assignments, we will only be using our simplisticPrediction() as a **baseline**. In other words, we will use more sophisticated models (including off-the-shelf models) and compare their performance to each other and to our simplistic procedure. The purpose of writing simplisticPrediction() ourselves was mostly to practice basic programming.


