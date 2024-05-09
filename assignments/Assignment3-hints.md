### Assignment 3 hints

Here's specific steps you could use to guide you through parts of Assignment 3.

### Part 2: Running simplistic prediction on many files

The **goal** here is to consolidate the work you were doing in Assignment 2 into a single function that is not the `main()` function. This will make it easier for you to think about what to do in `main()` for Assignment 3. Basically, you want your `main()` to iterate over many files and collect predictions for those. Everything necessary to obtain a prediction is best done outside `main()`. 

1. **Refactor** your assignment3.py program so that the `simplisticPrediction()` function now accepts a **file name** as the sole argument and returns a prediction. This means that most of the work that the main() function was previously doing in HW2 will now be done **in** the `simplisticPrediction()` function. At this stage, the input and output of the whole program should still be the same as for Assignment 2 (a file name, for input, and a printed statement about that file, outputting the prediction). So, you are passing your `main()` a filename via the parameters field in your run configuration, and then you are just passing that same filename **further along**, to `simplisticPrediction()`. `simplisticPrediction()` then **does all the work to output the prediction, including opening the file**.

2. Create an empty directory somewhere on your machine (**NOT** within your dataset folder and **NOT** within your GitHub repo). **Copy** the same data file you were using for Assignment 2 (train/pos/1_7.txt) into that directory. This will be your **test** directory for a short while. It's crucial to **start small** before you tackle many files, or you'll get too confused. However **don't mess with the original dataset directory structure**. No new files/directories there.

3. Now, instead of passing your main() function a filename, pass it that new **directory** name. At this point, your program will **stop working**. Don't panic; the next step will fix it.

4. Review the lecture about the Python **pathlib** module. In your `main()` function, write a loop which iterates over all `.txt` files in the directory whose name was passed as the argument to `main()`. In the loop, call the `simplisticPrediction()` function on the file. For now, the loop will only run **once**, since there is only a single file in your test directory. This is your chance to calmly explore what's happening.

5. Step through the entire execution and make sure the program processes the sole file in the test directory correctly (and outputs POSITIVE, as before).

6. Now, replace the path that you are giving to your main function by the **path to all the TRAINING POSITIVE files** in the dataset. So, train/pos on Mac or train\\\pos\\\ on Windows. Observe the program output predictions for all the files in that folder! There is a lot of files, so, it will take the program a while to print all the outputs.

7. Add a second argument to your `main()` your run/debug configuration; this second argument will be the path to all NEGATIVE TRAIN files in the dataset. Add another `for` loop which processes all negative files before or after processing all positive ones. You should see lots of printed output sentences, one for each file.

### Review vectors ###

You may find it helpful to store the data as instances of the `reviewVec` class, which you downloaded along with `evaluation.py` from the class repository. The reviewVec takes three properties: the text, the correct label, and the prediction. This vector will conveniently store the text, correct label, and prediction together in one reviewVec unit.

1. Import this class into your assignment3.py file.

2. Write two for-loops, one which goes over each positive review and one which goes over each negative review, and stores the text contents of each review along with the gold label for it in a list of reviewVecs. Use this list of reviewVecs in Part4. It will probably be less confusing than trying to manipulate the texts and the labels separately.

If you know how to make a [named tuple](https://docs.python.org/3/library/collections.html#collections.namedtuple), you may also use that instead.

### Part 3: Computing accuracy, and computing precision and recall

The updates to the repo you downloaded contain a tiny artificial dataset. Use it for testing as you work on this part. Make sure you understand what accuracy, precision, and recall **should be** for this tiny dataset and **why**. Once your program outputs the correct values for the tiny dataset, you can run it on the actual dataset and be more sure you are doing the right things. Working on a small dataset will make it easier for you to debug, when you experience problems. You won't be able to easily understand why your program doesn't output the correct values for the large dataset.

In the `evaluation.py` file, there are skeletons of two functions: `computeAccuracy` and `computePrecisionRecall`. For `computeAccuracy`, I suggest you create a lists that stores the correct predictions. Then you can use the length of the correct list divided by the length of all predictions to compute the acuracy. For `computePrecisionRecall`, I suggest you create four list, storing the predictions that are true positive, true negative, false positive, and false negative, then use the length of these lists to caculate the precision and recall values. The methods that will be useful are `zip()` (to combine the list of prediction and the list of gold_labels) and list comprehension.

1. Compute the **accuracy** of your system. Consult the function spec which you will find in `evaluation.py`. You can implement your function there and import it in your assignment3.py file. The accuracy of your system is the percentage, how many files it got correct. For now, have your program output the accuracy in a sentence: "The accuracy of Simplistic Prediction is X" -- just to see things working. Count NONE predictions as **mistakes** in this step. At this point, **comment out or delete** the print statements you had for each file and only output the accuracy in one sentence at the end. The accuracy of your system on the tiny-test dataset should be `0.625`. 

2. Compute **precision** and **recall** with respect to positive and negative reviews, separately. Consult the function spec which you will find in evaluation.py. You can implement your function there and import it in your assignment3.py file. Review carefully what precision and recall are, in the lecture and reading. **NB**: the terms "positive" and "negative" may introduce **confusion**, because precision and recall is often talked about in the terms of "true/false positive/negative". Take your time to make sure you treat the terms appropriately. E.g., if a negative review is classified NEG, then, with respect to negative review class, this is a TRUE POSITIVE! (Yes, confusing. A common problem in data science, too :) ). The key here is to think about positive and negative reviews absolutely **separately**, as if they had nothing to do with each other. It might help to mentally "rename" positive and negative reviews in "good" and "bad" reviews; that'll make it easier for you not to confuse the review labels with the types of error. For the tiny-test dataset, the precision wrt positive reviews should be `1`; recall `0.5`. The precision wrt negative reviews in the tiny-test dataset should `0.75`; recall `0.75`. **Remember** that you also have the `NONE` predictions in the system! They do not correspond to any gold label but they do count towards mistakes. Think carefully here; your goal is to identify/retrieve/classify something, and an output of `NONE` means you did not do that successfully.

3. Go over your code, cleaning it up as needed. **In particular, remove absolutely all print statements that are not printing out your overall accuracy, precision, and recall**. You should only be printing 5 numbers out. This is **important for our grading procedure**. 
