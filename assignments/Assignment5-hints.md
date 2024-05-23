# Assignment 5 Hints

Consult these steps if you don't know how to start the programming in Part 1 and Part 2.

### Part 1: Capturing standard output

1. To capture standard output, you will need to keep a counter to print a message every 100th iteration. A list index serves as a great counter when you iterate over a list. You have an example of how to use the `enumerate()` function for list iteration in the skeleton; it returns **both** the element in the list and its index! 

### Part 1: Sorting dicts/dataframes for word frequency

To get the most frequent words from the dataframe columns:

1. Using Python documentation and/or StackOverflow (or similar), **learn how to sort a python dict by value in reverse (descending order)**. (I could explain it to you, but it is important to learn to figure such things out on your own.) For example, given a dict: `{'a':1, 'b':3, g: '2'}`, you should get: `{'b':3, 'g':2, 'a':1}`. Feel free to ask on Discussion board if you don't understand the documentation/solution. **Do not implement your own sorting algorithm; use the built-in python methods.** It may feel intimidating to use code which you don't fully understand at first but it's important to try/learn how. Google and ask on the board!

2. **After** you've successfully sorted a **toy** python dict (as in the above a,b,g example) by value in descending order, use this knowledge to sort the counts obtained from feeding your Assignment 2 counter a column from your dataframe. 

### Part 2: Model comparison (in UWNetID_assignment5.py)

1. Import or copy your `evaluation.py` functions computing accuracy and precision and recall into Assignment 5. 

2. Put all your Naive Bayes code from Assignment 4 into a function and import that function into Assignment 5. 

3. Modify it such that it accepts a column and grabs the review text from that column. (Maybe you won't need to modify anything if that's how you wrote it in the first place.) 

4. Modify it such that it returns a dict or a list contatining the 10 output numbers. It is up to you which order/format; just make sure it is clear to you what that is and you don't make a mistake later accessing the numbers. See example/comments in the skeleton code.
 