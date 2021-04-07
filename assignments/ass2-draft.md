[Home](../index.md)

## Assignment 2: Rudimentary data science

In this assignment, you will perform some basic word counting on one 
file from the IMDB dataset and then use this rudimentary approach to predict whether the file represents a positive or a negative review. You will also continue practicing using tools esseptial in all real-life projects.

Specifically and technically, you will practice:
1. Using version control and development tools (git and GitHub, and VSCode). You already started practicing it in Assignment 1.
2. Reading text from a file, such as one coming fromt the IMDB dataset, and storing it in a variable.
3. Removing punctuation from text using regular expressions.
4. Tokenizing text into words.
5. Counting words in a text.
6. Making a (simplistic) prediction about whether a file represents a positive or a negative review.

In the next assignment, you will assess how well this system works and will compare it with something more sophisticated.

### Submission summary
There is only one deliverable:

1. The link to your submission commit (the submission is on GitHub; the link to the specific commit associated with your final submission goes to Canvas for the time stamp.)

Details: The below details are also part of the instructions below. Here's a summary related to submission: You will **get** the homework from a repository that we created (by forking it). You won't be able to push anything to it; instead, forking will create your own **private** copy of the repository. It is convenient for you to work in that private repository and to save your work in progress there. You do not need to add us as collaborators there. Once you are done, you will **add your complete python program, renamed appropriately, to the repository you created for this class in Assignment 1**. There, Yuanhe and Olga are collaborators and they will be able to download your submission and test it. Otherwise, that repository is private and noone else will see it. Even if you do make it public, anything related to grading will be done via Canvas. GitHub is just to store the code. 

### Important note about grading.
The preliminary assessment for this assignment will be done automatically. For this reason, it is crucial that you do exactly what the assignment is asking you and not something else,
even if something else is better. There are always better ways of doing things, especially in programming. In this assignment, we are learning how to do some of the basic things
following instructions, such that everyone arrives at the exact same result. As an example, using regular expressions to clean punctuation is not necessarily the best way of doing it, and we will talk about it when we talk about algorithm complexity. Still, regular expressions are important to learn about, so please use them for this task. We will want everyone to get the exact same results rather that the best results.

### Part 1 (recommended to complete during the first week): 
1. Fork [the repository we created for your Assignment 2](https://github.com/olzama/ling471-SP2021-HW2) (review the slide about forking in the lecture about git, if needed). Click on "Fork" in the right upper corner on GitHub:

    <img width="452" alt="Screen Shot 2021-04-07 at 1 45 36 PM" src="https://user-images.githubusercontent.com/10963114/113931734-acd67300-97a7-11eb-954c-8c209281f5f1.png">

    Then click on your user, and a copy repository will be created under your account (NB: `erg` is a name of a repository; I cannot fork my own repository so I had to choose another one to make the screenshot):

   <img width="449" alt="Screen Shot 2021-04-07 at 1 45 45 PM" src="https://user-images.githubusercontent.com/10963114/113937338-ddb9a680-97ad-11eb-82ce-45feac9d5617.png">

   You have now created your own private copy of the repository. Don't worry, you won't be able to mess up the original repository; it is protected from that.

2. Clone your forked private copy to your local machine in VS Code (like you did in Assignment 1).
3. Make sure you see assignment2_skeleton.py in your VS Code project.
4. Figure out where exactly the following review from the IMDB dataset is located on your machine: aclImdb/train/pos/1_7.txt (on Windows, the slashes will be backslashes). You need the full path. For example, on my machine the full path happens to be: `/Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt`. On your machine, it will be something different. (Hint: Try using command line terminal to navigate to the file using a series of `cd` commands and then type `pwd` (Linux/Mac) or `echo %cd%` (on Windows). That should give you a full path which you can then copy.)
5. Create a Running Configuration. You will see a file called launch.json. Inspect launch.json. Add a variable called "args", as in the screenshot: 

    <img width="902" alt="Screen Shot 2021-04-07 at 1 41 11 PM" src="https://user-images.githubusercontent.com/10963114/113931102-f1154380-97a6-11eb-8d01-7d234fcc3309.png">

6. In the above screenshot, the "args" is a path from Olga's home machine. You need to point it to your path, which you found in the previous step! 
7. Now inspect assignment2_skeleton.py. There, we already named the functions for you and indicated in comments what kind of statements you should write. We also included some of the statements already, to get you started.
8. Make sure you can run and debug the program. Review the slides/lecture recording on debugging in VS code. 
    1. If you run your debug configuration, which will be available  in the debug console:

        ![Screen Shot 2021-04-07 at 1 07 19 PM](https://user-images.githubusercontent.com/10963114/113928440-ab0ab080-97a3-11eb-8200-856351def8ad.JPG)
    
        -- you should see the following output:
    
        `The prediction for file /Users/olzama/Teaching/Ling471/datasets/IMDB/aclImdb/train/pos/1_7.txt is NONE`
  
    2. Set the breakpoint at the first line of the main function, start running the program in debug mode, and make sure the debugger stops and you see the program state on the left (in the debugger console/pane):

        ![Screen Shot 2021-04-07 at 1 19 45 PM](https://user-images.githubusercontent.com/10963114/113928868-36844180-97a4-11eb-9478-4ef5fe1c77ed.JPG)

        Step through the program to understand exactly what it is doing and why it outputs NONE in the end. Use the debug controls and examine program state at every step.
    
        ![Screen Shot 2021-04-07 at 1 22 57 PM](https://user-images.githubusercontent.com/10963114/113936910-4f452500-97ad-11eb-81b9-aee5387db5a1.JPG)

         You will be isung the Step Over control to go from statement to statement within the same function. Use Step Into control to jump into a function instead of stepping over it.
         Stepping over a function will allow you to immediately see what it returned but not to step through its execution.
    
### Part 2 (complete during the second week):
1. Duplicate the skeleton file and **RENAME** it: YourUWNetID_assignment2.py (note the **underscore**; not a dash!). Add it to the repository. Now you will be working in this file. The skeleton should stay as is for reference. You may want to start over, or what not. Remember you always have the repository as the back up, to go back in time if needed.
1. Fill in the program, gradually. Read the comments; they contain instructions and hints. Ask questions on the Discussion board. Revisit the lectures/readings on the relevant topics. After adding a statement, set the breakpoint on it and make sure the statement is doing what you intended, by stepping over it and examining the change in the program state. You need there to be a next statement for the debugger to stop, and most your functions have return statements which can serve this purpose if nothing else is added. 

    After you are done, your program should output "POSITIVE" for review 1_7.txt. Feel free to commit to your forked repository frequently, e.g. every time you make progress. That will help you revert to the last working state if you get confused.

2. After you are done: **Add** the file YourUWNetID_assignment2.py **to the repository which you created in Assignment 1** (the one for which you added Olga and Yuanhe as collaborators).  **Commit** with a message: "Assignment 2 submission", and **push**. give it a few minutes, go to Github, and make sure the file is there. **Note the commit number**. Click on the commit number and copy the URL path in the browser.
 
    ![Screen Shot 2021-04-07 at 2 23 22 PM](https://user-images.githubusercontent.com/10963114/113936852-3f2d4580-97ad-11eb-8cc8-7d024a3b5227.JPG)
 

3.    **Submit the commit number and the link to Canvas as a text file**.

   ![Screen Shot 2021-04-07 at 2 13 43 PM](https://user-images.githubusercontent.com/10963114/113936426-9848a980-97ac-11eb-9fd8-19370cbfa420.JPG)


[Home](../index.md)
