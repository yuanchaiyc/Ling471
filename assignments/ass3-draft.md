## Assignment 3

### Summary

In this assignment, you will continue developing a movie review classifier. Mostly, you will be practicing **evaluating** a system. In particular, you will compute **accuracy** and **precision and recall** of the simplistic "system" you built in Assignment 2.

You will start with the code you submitted for Assignment 2 and will develop it further so that it now processes a bunch of files. You will represent the files as **labeled data points.** With that in hand, you will be able to run the simplistic prediction system on all of the files, compare the predicted labels with the actual labels, and compute the performance metrics.

After we are sure we know how to process multiple files, store the data as vectors and compute things, we will leave our simplisticPrediction() behind and will proceed with deploying more sophisticated (off-the-shelf) techniques on our data.

As before, you will submit your final version to the repository you created for the class in Assignment 1, and you will submit the commit number to Canvas, for time stamp.

### Part 1: Assignment 2 clean-up/fixes
1. Address any comments you received for Assignment 2 (if you already got it back), or otherwise make sure your Assignment 2 program is working correctly.

### Part 2: Running simplistic prediction on many files
1. **Refactor** your program so that the simplisticPrediction function now accepts a file name as the sole argument and returns a prediction. This means that most of the work that the main() function was previously doing will now be done in the simplisticPrediction() function. At this stage, the input and output of the program should still be the same as for Assignment 2. So, you are passing your main() a filename via launch.json, and then you are just passing that same filename further along, to simplisticPrediction(). simplisticPrediction() then does all the work to output the prediction, including opening the file.

2. Create an empty directory somewhere on your machine (NOT within your dataset folder). **Copy** the same file you were using for Assignment 2 (train/pos/1_7.txt) into that directory. This will be your **test** directory. It's good practice to start small before you tackle many files, however don't mess with the original directory structure. No new files/directories there.

3. Now, instead of passing your main() function a filename, pass it that new directory name. At this point, your program will stop working. The next step will fix it.

4. Review the lecture about the python **pathlib** module. In your main() function, write a loop which iterates over all files in the directory whose name was passed as the argument to main(). In the loop, call the simplisticPrediction() function on the file.

5. Step through the entire execution and make sure the program processes the sole file in the test directory correctly (and outputs POSITIVE, as before).

6. Now, replace the path that you are giving to your main function by the path to all the TRAIN POSITIVE files in the dataset. So, train/pos on Mac or train\\\pos\\\ on Windows. Observe the program output predictions for all the files in that folder! There is a lot of files, so, it will take the program a while to print all the outputs.

7. Add a second argument to your main() in launch.json; this second argument will be the path to all NEGATIVE TRAIN files in the dataset. Add another for loop which processes all negative files after processing all positive ones.

### Part 3: Computing accuracy and computing precision and recall
1. Compute the accuracy of your system. The accuracy of your system is the percentage, how many files it got correct. Have your program output the accuracy in a sentence: "The accuracy of Simplistic Prediction is X". Count NONE predictions as mistakes in this step.

2. Compute **precision** and **recall** with respect to positive and negative reviews, separately. You will need to declare **more variables** to do this! **Exclude** the NONE predictions from your computations (do not count the files for which the prediction is NONE as mistakes and do not add them to the totals). Review carefully what precision and recall are, in the lecture and reading. **NB**: the terms "positive" and "negative" may introduce **confusion**, because precision and recall is often talked about in the terms of "true/false positive/negative". Take your time to make sure you treat the terms appropriately. E.g., if a negative review is classified NEG, this is a TRUE POSITIVE! (Yes, confusing. A common problem in data science, too :) ). The key here is to think about positive and negative reviews absolutely **separately**, as if they had nothing to do with each other. It might help to mentally "rename" positive and negative reviews in "good" and "bad" reviews; that'll make it easier for you not to confuse the review labels with the types of error. 

3. **Refactor** your program once again, so that all your main() does is call a (new) function called evaluateSimplistic(). Try the following: select all the code that does the evaluation, then right click and find the "Extract method" option. Click on it. The code you selected was **extracted** as a new method with some name like "newmethod877". Rename that to "evaluateSimplistic". Make sure your main() contains a call to that method, with appropriate arguments, if applicable. Test that the program works as expected.

The **expected output** is:

```
The accuracy of Simplistic Prediction is 0.27508
The precision of Simplistic Prediction wrt POSITIVE is 0.8547117634545841
The precision of Simplistic Prediction wrt NEGATIVE is 0.47100494233937396
```


### Part 4: Error analysis
1. Take note of 5 positive and 5 negative reviews which were classified incorrectly. (You can collect the filenames for which the prediction is incorrect, in a list, and then output the list in a file, or just print it out.) Inspect the files. What do you notice? What kind of phenomena (syntactic, semantic) can you observe which led to your system mistaking a good review for a bad review, and vice versa? The precision for negative reviews is much lower than for positive; upon inspecting the files, why do you think that is?


From now on, we will only be using our simplisticPrediction() as a "baseline". In other words, we will use more sophisticated models (we won't build them ourselves but will use off-the-shelf ones) and compare their performance to each other and to our simplistic procedure. The purpose of writing simplisticPrediction() ourselves was mostly to practice basic programming.


