[Home](../index.md)

## Assignment 2: Rudimentary data science

In this assignment, you will perform some basic word counting on one 
file from the IMDB dataset and then use this rudimentary approach to predict whether the file represents a positive or negative reviews.

Specifically and technically, you will practice:
1. Reading text from a file, such as one coming fromt the IMDB dataset, and storing it in a variable.
2. Removing punctuation using regular expressions.
3. Tokenizing text into words.
4. Counting words in a text.
5. Making a (simplistic) prediction about whether a file represents a positive or a negative review and comparing it to the actual label.

In the next assignment, you will assess how well this system works and will compare it with something more sophisticated.

### Important note about grading.
The preliminary assessment for this assignment will be done automatically. For this reason, it is crucial that you do exactly what the assignment is asking you and not something else,
even if something else is better. There are always better ways of doing things, especially in programming. In this assignment, we are learning how to do some of the basic things
following instructions, such that everyone arrives at the exact same result. As an example, using regular expressions to clean punctuation is not necessarily the best way of doing it, and we will talk about it when we talk about algorithm complexity. Still, regular expressions are important to learn about, so please use them for this task. We will want everyone to get the exact same results rather that the best results.

### Part 1 (recommended to complete during the first week): 
1. Fork the repository we created for your Assignment 2 (review the slide about forking in the lecture about git). 
1. Clone your forked copy to your local machine in VS Code (like you did in Assignment 1).
1. Make sure you see both assignment2_skeleton.py.
1. Figure out where exactly the following review from the IMDB dataset is located on your machine: aclImdb/train/pos/1_7.txt (on Windows, the slashes will be backslashes). You need the full path. For example, on my machine the full path happens to be: `/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt`. On your machine, it will be something different. (Hint: Try using command line terminal to navigate to the file using a series of `cd` commands and then type `pwd`. That will give you a full path which you can then copy.)
1. Create a Running Configuration. You will see a file called launch.json. Inspect launch.json. Add a variable called "args", as in the screenshot: 

    <img width="902" alt="Screen Shot 2021-04-07 at 1 41 11 PM" src="https://user-images.githubusercontent.com/10963114/113931102-f1154380-97a6-11eb-8d01-7d234fcc3309.png">

1. In the above screenshot, the "args" is a path from Olga's home machine. You need to point it to your path, which you found in the previous step! 
1. Now inspect assignment2_skeleton.py. There, we already named the functions for you and indicated in comments what kind of statements you should write. We also included some of the statements already, to get you started.
1. Make sure you can run and debug the program. Review the slides/lecture recording on debugging in VS code. 
    1. If you run your debug configuration, which will be available  in the debug console:

    ![Screen Shot 2021-04-07 at 1 07 19 PM](https://user-images.githubusercontent.com/10963114/113928440-ab0ab080-97a3-11eb-8200-856351def8ad.JPG)
    
    -- you should see the following output:
    
    `The prediction for file /Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt is NONE`
  
    2. Set the break point at the first line of the main function, start running the program in debug mode, and make sure the debugger stops and you see the program state on the left (in the debugger console/pane):

    ![Screen Shot 2021-04-07 at 1 19 45 PM](https://user-images.githubusercontent.com/10963114/113928868-36844180-97a4-11eb-9478-4ef5fe1c77ed.JPG)

    Step through the program to understand exactly what it is doing and why it outputs NONE in the end. Use the debug controls and examine program state at every step.
    
    
    ![Screen Shot 2021-04-07 at 1 22 57 PM](https://user-images.githubusercontent.com/10963114/113929284-ba3e2e00-97a4-11eb-9d4f-e654c63862e7.JPG)

     You will be isung the Step Over control to go from statement to statement within the same function. Use Step Into control to jump into a function instead of stepping over it.
     Stepping over a function will allow you to immediately see what it returned but not to step through its execution.
    
### Part 2 (complete during the second week):
Fill in the program, gradually. Read the comments; they contain instructions and hints. Ask questions on the Discussion board. Revisit the lectures/readings on the relevant topics. After adding a statement, set the breakpoint on it and make sure the statement is doing what you intended, by stepping over it and examining the change in the program state. You need there to be a next statement for the debugger to stop, and most your functions have return statements which can serve this purpose if nothing else is added.

After you are done, your program should output "POSITIVE" for review 1_7.txt.

[Home](../index.md)
