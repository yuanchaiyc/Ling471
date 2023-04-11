## Assignment 2: Rudimentary data science

In this assignment, you will perform some basic word counting on one file from the IMDB dataset and then use this rudimentary approach to predict whether the file represents a positive or a negative review. You will also continue practicing using tools esseptial in all real-life projects.

Specifically and technically, you will practice:
1. Using version control and development tools (git and GitHub, and PyCharm). You already started practicing it in Assignment 1.
2. Reading text from a file, such as one coming from the IMDB dataset, and storing it in a variable.
3. Using regular expressions as well as built-in string functions, to clean up the data.
4. Tokenizing text into words (using a simplistic way).
5. Counting words in a text.
6. Making a (simplistic) prediction about whether a file represents a positive or a negative review.

In the next assignment, you will assess how well this system works and will compare it with something more sophisticated.

This assignment **looks long** again because of the instructions (Part 1). The program you will actually be writing (Part 2) is very **small and short** -- though it will require significant time if you never programmed before.

### Submission summary
There is only **one** deliverable:

1. The link to your submission **git commit** (the submission is on GitHub; the link to the specific commit associated with your final submission goes to Canvas for the time stamp.)

Logistical summary: You will **get** the homework by cloning this class Git repo. You will be able to add the assignment files to the private git repo that you created as part of Assignment 1. It is probably most convenient for you to work in that private repository and to save your work in progress there. Once you are done, your **complete python program, named appropriately, should be present in the repository you created for this class in Assignment 1**. There, Matt and Siyu are collaborators and they will be able to download your submission and test it.

### Important note about grading.
The preliminary assessment for this assignment will be done automatically. For this reason, it is crucial that you do exactly what the assignment is asking you and not something else, even if something else is better. There are always better ways of doing things, especially in programming. In this assignment, we are learning how to do some of the basic things following instructions, such that everyone arrives at the exact same result.

### Part 1. Cloning the skeleton code and stepping through it in the debugger. (Recommended to complete asap):
1. Clone this course repository with

    ```bash
    git clone https://github.com/maetshju/Ling471
    ```

    or the equivalent in PyCharm.

    You have now created your own local copy of the repository. Don't worry, you won't be able to mess up the original repository; it is protected from that.

2. Make a new project in PyCharm. You will need to add the `assignment2_skeleton.py` file to your project by copying and pasting it into your project folder.

3. Figure out where exactly the following review from the IMDB dataset is located on your machine: aclImdb/train/pos/1_7.txt

**NB**: On Windows, the standard filepath separator is `\`. However, most programming languages can now handle you using `/` on all systems, which is probably advisable on Windows. If, however, you want to use the `\` on Windows, you will need to insert an extra backslash everytime because because python thinks backslash is an **escape** character. So, you need to **escape the escape character**! Your path "C:\Users\myusername\dataset\etc" will turn into: "C:\\\Users\\\myusername\\\dataset\\\etc").

You need the full path. (Hint: Try using command line techniques to navigate to the file using a series of `cd` commands and then type `pwd` (Linux/Mac) or `echo %cd%` (on Windows). That should give you a full path which you can then copy.)

4. Create a Run Configuration (see under Run in PyCharm). You will only need to add one thing to the configuration: the path to the file you will pass to your program as a command line argument. See the lecture from 4/11 or [this StackOverflow page](https://stackoverflow.com/questions/33102272/pycharm-and-sys-argv-arguments) for additional information.

5. Now inspect assignment2_skeleton.py. There, we already named the functions for you and indicated in the comments what kind of statements you should write. We also included some of the statements already, to get you started.

6. Make sure you can both **debug** and **run** the program. Review the slides/lecture recording on debugging in PyCharm.

    1. If you run the program

        -- you should see the following output (with your path/filename instead of Matt's):

        `The prediction for file C:/Users/Matt/Downloads/aclImdb/train/pos/1_7.txt is NONE`

    2. Set the breakpoint at the first line of the main function. Start running the program in debug mode, and make sure the debugger stops and you see the program state on the left (in the debugger console/pane):

        ![Initial breakpoint](https://github.com/maetshju/Ling471/raw/main/imgs/a2_initial_breakpoint.png)

        Step through the program to understand exactly what it is doing and why it outputs NONE in the end. Use the debug controls and examine the program state at every step. This technique of using a debugger to slowly build an understanding of new code you've been given can be really useful when you work on new projects!

         You will be using the `Step Over` control to go from statement to statement within the same function. Use the `Step Into` control to jump into a function instead of stepping over it.
         Stepping over a function will allow you to immediately see what it returned but not to step through its execution. Experiment with this a few times to see what it means.

    3. Step through the program a few times, until you are comfortable with the debugger and understand fully what the program is doing and how its state changes and why it outputs what it outputs in the end. **Doing Part 1 carefully ahead of time, at a comfortable pace, will greatly help you with Part 2.**

### Part 2:
1. Ensure you have PyCharm sitting in the clone of your *personal* repo for the class, not the class repo you cloned earlier in this assignment. **RENAME** the Assignment 2 skeleton file: YourUWNetID_assignment2.py (note the underscore; not a dash). Make sure it is in your personal repo (you may need to copy and paste it around). Now you will be working in this file.

1. Fill in the program, gradually. Read the comments; they contain instructions and hints. Ask questions on the Discussion board. Revisit the lectures/readings on the relevant topics. Or search for error messages on Google. After adding a statement, set the breakpoint on it and make sure the statement is doing what you intended by stepping over it and examining the change in the program state. You need there to be a next statement for the debugger to stop, and most of your functions have return statements which can serve this purpose if nothing else is added.

    After you are done, your program should output "POSITIVE" for review 1_7.txt. Feel free to commit to your repository frequently, e.g. every time you make progress and the program starts doing something you intended it to do. Include meaningful commit messages, e.g. "Successfully replacing spaces with tabs". That will help you look at the last working state if you get confused and your program stops working.

    **NOTE**: We will be looking at your code and not just running the script. If you have written a program that just prints "POSITIVE" without doing any of the requested analysis, you will receive a 0.

2. After you are done: **Add** the file YourUWNetID_assignment2.py **to the repository which you created in Assignment 1** (the one for which you added Matt and Siyu as collaborators).  **Commit** with a message: "Assignment 2 submission", and **push**. give it a few minutes, go to Github, and make sure the file is there. **Note the commit number**. Click on the commit number and copy the URL path in the browser.

    ![Screen Shot 2021-04-07 at 2 13 43 PM](https://user-images.githubusercontent.com/10963114/113936426-9848a980-97ac-11eb-9fd8-19370cbfa420.JPG)

3.    **Submit the commit number and the link to Canvas as a text file**. Please don't forget a file extension!

   ![Screen Shot 2021-04-07 at 2 23 22 PM](https://user-images.githubusercontent.com/10963114/113936852-3f2d4580-97ad-11eb-8cc8-7d024a3b5227.JPG)

