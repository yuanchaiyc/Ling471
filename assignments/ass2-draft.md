[Home](../index.md)

## Assignment 2: Rudimentary data science

In this assignment, you will perform some basic word counting on one 
file from the IMDB dataset and then use this rudimentary "model" to predict whether other files contain positive or negative reviews.

Specifically and technically, you will practice:
1. Reading text from a file, such as one coming fromt the IMDB dataset, and storing it in a variable, while also mapping it to a label with which it came.
2. Removing punctuation using regular expressions.
3. Tokenizing text into words.
4. Counting words in a text.
5. Making a (simplistic) prediction about whether a file represents a positive or a negative review and comparing it to the actual label
6. Computing and reporting the accuracy of your rudimentary sentiment analysis system

### Important note about grading.
The preliminary assessment for this assignment will be done automatically. For this reason, it is crucial that you do exactly what the assignment is asking you and not something else,
even if something else is better. There are always better ways of doing things, especially in programming. In this assignment, we are learning how to do some of the basic things
following instructions, such that everyone arrives at the exact same result. As an example, using regular expressions to clean punctuation is not necessarily the best way of doing it, and we will talk about it when we talk about algorithm complexity. Still, regular expressions are important to learn about, so please use them for this task. We will want everyone to get the exact same results rather that the best results.

### Part 1: 
1. Fork the repository we created for your Assignment 2 (review the slide about forking in the lecture about git). 
2. Open that folder in VS Code.
3. Make sure you see both assignment2.py and launch.json in VS Code.
4. Figure out where exactly the following review from the IMDB dataset is located on your machine: aclImdb/train/pos/1_7.txt (on Windows, the slashes will be backslashes). You need the full path.
5. Inspect launch.json. In "args", it will have a path from Olga's home machine. You don't have that path on your machine. You need to point it to the correct path you found in the previous step! 
6. Now inspect assignment2_skeleton.py. There, we already named the functions for you and indicated in comments what you kind of statements you should write. We also included some of the statements already, to get you started.
7. Make sure you can debug the program. Review the slides/lecture recording on debugging in VS code. Set the break point at the first line of the main function, run the program, and make sure you see the program state.
8. Fill in the program, gradually. Read the comments; they contain instructions and hints. Ask questions on the Discussion board. Revisit the lectures/readings on the relevant topics. After adding a statement, set the breakpoint on it and make sure the statement is doing what you intended, by stepping over it. You need there to be a next statement for the debugger to stop, and most your functions have return statements which can serve this purpose if nothing else is added.
[Home](../index.md)
