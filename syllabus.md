[Home](index.md)

# Syllabus

The course Computational Methods for Linguists focuses on learning **how data science methods/tools can be applied in the domain of linguistics**. One of the main goals of the course is to familiarize the students with the **basics of programming**, including **general technical versatility skills** required to successfully undertake even the most basic programming tasks. While the syllabus doesn't mention linguistic and social concepts explicitly, they will be present throughout the class, as the assignments will be organized around **linguistic or linguistically-annotated data**. The presentations will be graded in particular based on **how well they are connected to linguistic and social concepts**.

### Learning outcomes 
<details>
  <summary>Click to expand</summary>
  
Students will learn about what counts as data in computational linguistics, as well as how linguistic theory and questions dictate which computational methods are employed. Similarly, students will learn about ethical and social implications of data uses in linguistics. Students will learn basic programming concepts and how to write a range of programs (using python programming language). They will also learn how to use command-line interface and version control. They will learn a range of techniques for data cleaning, representing data as vectors, thoughtfully choosing a model, loading the data into the model, running the model, and interpreting and visualizing results.
</details>

### Extended office hours ###
<details>
  <summary>Click to expand</summary>

In this class, we offer you <b>extended office hours</b>, because you will face technical issues with which every person needs help, when they come across them the first few times.
While the usual expectation applies, that you come to the office hours with a <b>specific issue</b> and show your work (demonstrate that you have made some effort already), remember that there is <b>no expectation</b> that your issue needs to be particularly complex or advanced. Many technical issues are simple but can take hours to figure out if you see them for the first time. <b>Use the extended office hours.</b>
</details>

### Asking questions on the Discussion Boards ###
<details>
  <summary>Click to expand</summary>

There will be a dedicated Discussion Board on Canvas for each assignment, as well as an area for general and other questions. It is important that you ask a lot of questions on the Discussion Boards, and we do mean it. Posting a question on the Discussion Board will allow others to benefit from your question and our answer! Use email for confidential questions such as regarding your grades and personal circumstances, but not for any questions related to assignments or class logistics! Use the Discussion Boards for that!

</details>

[Some advice on how to ask technical questions on the Discussion Board effectively](questions.md).

### Assessment
<details>
  <summary>Click to expand</summary>

The class is organized around a series of assignments targeting different concepts and skills but all connected to linguistic data/corpora (TBA). There are no exams. The assignments, on which the students will work individually, put toghether account for 80% of the grade. Additionally, there is a presentation related to the assignments which is worth another 15% (the presentation may be pre-recorded). Additionally, students will write a blog post reflecting on a reading of their choice and will also post comments to their classmate's posts; this is worth another 5%. Up to 2% (positive) adjustment for participation (such as asking questions during class or on the discussion board, attending office hours etc.). <br><br>

Grading scale: <br><br>

95% = 4.0, 94% = 3.9, 93% = 3.8 & so on.

</details>


### Late homework policy

* Homework is due at 11:59pm on the date posted.

* Unless you've made prior arrangements with Olga, homework turned in within one day of the due date will be graded at 80%, two days 70%. credit. No credit after that. This means, for example, that if you submitted a perfectly done assignment even a minute after the deadline, you will receive 80% credit. Please clarify the policy with Olga if unsure.

* By prior arrangements, we mean contacting Olga no later than the day before the homework is due (i.e., Wednesday for homework due Thursday) with the reason you feel you can't complete your homework on time. At that time, Olga will decide whether or not to grant an extension, and for how long.


### Assignments

The assignments will be roughly biweekly. The goal is to give you some breathing space in between and sufficient time to work on them in a reasonable pace. However, it will be very important for you to remember that **the assignments which are technical in nature may take a long time due to technical issues** (which is very normal, and dealing with it is **one of the main learning goals** in this class). This means, more or less, that if you delay starting the assignment, you are very likely to not finish it by the time it is due. 

I highly recommend the following <b>algorithm</b> for the technical assignments:

1. Start on the day assignment is published (or the next day).
1. Get a feel of how fast you are progressing. Take a note of the first block you are facing. [Post about it on the Discussion Board](questions.md). Then go do something else.
1. Come back to it next day. See if you get unblocked. If not, go to the next office hour and see if that helps you get unblocked.
1. Repeat from step 2.

Once you start feeling like you have not been making progress for 20-30 minutes, <b>stop</b>. Come back to it later (e.g. next day).

Having 2 weeks or so for each assignment can mean you can take nice breaks from the class, but that will only work if you start early. When progress feels slow, take frequent but short breaks (e.g. leave the assignment and come back to it next day). When you are almost done and you feel like you understand almost everything and will be able to finish the assignment quickly, then it becomes possible to take a few days break. But not before, or you will not succeed in earning a good grade. 

### Readings
<details>
    <summary>Click to expand</summary>  
There will be some assigned readings for most lectures. Some of them will just be blog posts and websites for beginner programmers etc. They are just as good for learning about these things as books ;) Maybe even better. Other readings will include scholarly papers; reading those is more difficult, so, try to identify some specific goals as you read. E.g. "I am reading this to understand what "Data Statements" are and I want to form an opinion about whether they are useful in some particular context." 
  
</details>  
  
(The [blogging assignment](blog.md) readings overlap with the assigned readings but it is not the same set.)


### Texts
<details>
  <summary>Click to expand</summary>
  
There are no required textbooks, though there will be some reading, all available online.<br><br>

Recommended text (for those who have not taken LING200): <i>Language Files 12</i>. <br><br>

You may find a book on python programming for beginners helpful, but in general we will rely on online resources.
</details>

### Class schedule (subject to change)

Date | Topic | Reading | Due
------------ | -------------
March 30 | [Introduction, course structure, etc.](slides/Ling471-0330.pdf)
April 1 | [Conceptual overview. Data science](slides/0401.pdf) | [What is Data Science?](https://hdsr.mitpress.mit.edu/pub/jhy4g6eg/release/7?readingCollection=72befc2a)| Online survey (on Canvas); ["Assignment 0"](assign0.md)
||| [Request an account on the patas cluster](https://cldb.ling.washington.edu/live/accountrequest-form.php)
April 6 | [Basic system/programming concepts](slides/0406.pdf) | [Basics of python programming (Chapter 1)](https://www.openbookproject.net/books/bpp4awd/ch01.html) |
April 8 | [VS Code basics. Version control.](slides/0408.pdf) [demo code](demos/April8_demo.py)| [1. The IMDB reviews dataset paper](https://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf)
|  | [2. Data statements for NLP; ](DataStatementsForNLP.pdf) [3. Version control (read conceptually; ignore the R-studio stuff etc.)](https://ourcodingclub.github.io/tutorials/git/) | Blogs 1
April 13 | [Variables, scope, and control flow;](slides/0413.pdf) [code;](demos/April13.py) [fizzbuzz](demos/fizzbuzz.py) |[0. Assignment and statements (2.1--2.13);](https://www.openbookproject.net/books/bpp4awd/ch02.html) [1. Numbers, strings, lists (3.1);](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator) [2. Logical operators; ](https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_propositional_logic.htm) [3. Control flow (4.1--4.5);](https://docs.python.org/3/tutorial/controlflow.html) [4. De Morgan's laws](https://blog.penjee.com/what-is-demorgans-law-in-programming-answered-with-pics/)| [Assignment 1](assignments/Assignment-1.md) 
April 15 | [Loops and dictionaries. Input/output; ](slides/0415.pdf) [code](demos/April15.py) | [1. Loops;](https://www.dataquest.io/blog/python-for-loop-tutorial/) [2. Dicts (6.1--6.2);](https://www.openbookproject.net/books/bpp4awd/ch06.html) [3. Input and output;](https://docs.python.org/3/tutorial/inputoutput.html) | 
April 20 | [Text processing; ](slides/0420.pdf) [code](demos/April20.py)| [0. Regular expressions;](https://docs.python.org/3/howto/regex.html) [1. Tokenization;](https://www.analyticsvidhya.com/blog/2019/07/how-get-started-nlp-6-unique-ways-perform-tokenization/) [2. Unicode;](https://docs.python.org/3/howto/unicode.html) [3. Modules](https://docs.python.org/3/tutorial/modules.html) | Blogs 2
April 22 | [Text processing, contd. Unicode. Evaluation. ](slides/0422.pdf) [VS Code settings](demos/setting-up-vs-code.md)  |  | 
April 27 | [Metrics. Precision and Recall. ](slides/0427.pdf) [code](demos/April27.py) | [Precision and recall](https://medium.com/@shrutisaxena0617/precision-vs-recall-386cf9f89488)  | [Assignment 2](assignments/Assignment2.md) 
April 29 | [Data science and probability; MLE](slides/0429.pdf)  | [A mathy tutorial](https://tutors4you.com/probabilitytutorial.htm) -- try to work through a couple problems of different types, listed there at the end. |
May 4 | [Statistics: distributions. The Gaussian distribution; ](slides/0504.pdf) [Exercise; ](https://github.com/olzama/Ling471/blob/gh-pages/assignments/ex-gauss.md) [solution code](demos/May4.py) | Start [tutorial](https://www.edureka.co/blog/statistics-and-probability/), read through "Measures of spread" | Blogs 3
May 6 | [Bayes Theorem. Dataframes; ](slides/0506.pdf) [code](demos/May6.py) | Finish [tutorial](https://www.edureka.co/blog/statistics-and-probability/), skip the section about R but make sure to read about the Bayes Theorem. You can also skip: Entropy and Information Gain; Inferential statistics. Read those if you like (they are generally important), but we probably don't have time for them. | [Assignment 3](assignments/Assignment3.md) 
May 11 | [Machine Learning and matrices: Linear regression; ](slides/0511.pdf) [exercise and demo code](demos/May11.py) | [Regression and classification; ](https://medium.com/quick-code/regression-versus-classification-machine-learning-whats-the-difference-345c56dd15f7) [skeleton code](demos/May11_skeleton.py) |
May 13 | ML-contd. Classification: Logistic regression, Naive Bayes | [Logistic regression; ](https://www.tibco.com/reference-center/what-is-logistic-regression)  [Naive Bayes; ](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)  | Blogs 4
May 18 | Deep Learning overview. Non-linearity and neural nets. Pre-trained models | [Deep learning for NLP; ](https://medium.com/dair-ai/deep-learning-for-nlp-an-overview-of-recent-trends-d0d8f40a776d) [Non-linear problems; ](https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7) [Testing NLP models](https://slideslive.com/38929272/beyond-accuracy-behavioral-testing-of-nlp-models-with-checklist) | 
May 20 | Using linguistic knowledge in NLP | TBA | 
May 25 | Working with linguistic corpora | TBA | [Assignment 4](https://olzama.github.io/Ling471/assignments/Assignment4.html)
May 27 | Visualization and Communication | TBA | Blogs 5
June 1 | Presentations 
June 3 | Presentations
June 8 | | | Assignment 5 


## Academic Integrity
The University takes academic integrity very seriously. Behaving with integrity is part of our responsibility to our shared learning community. If you’re uncertain about if something is academic misconduct, ask the instructor. The Instructor is willing to discuss questions you might have.

Acts of academic misconduct may include but are not limited to:

- Cheating (working collaboratively on quizzes/exams and discussion submissions, sharing answers and previewing quizzes/exams)
- Plagiarism (representing the work of others as your own without giving appropriate credit to the original author(s))
- Copying programming solutions (or parts of them) from other sources including but not limited to StackOverflow and similar websites
- Obtaining answer keys for the assigned homework and consulting them while preparing homework
- Unauthorized collaboration (working with each other on assignments unless permitted by the intructor)

Concerns about these or other behaviors prohibited by the Student Conduct Code will be referred for investigation and adjudication by (include information for specific campus office).

Students found to have engaged in academic misconduct may receive a zero on the assignment (or other possible outcome).

## Disability Accommodations 
Your experience in this class is important. It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law. If you have already established accommodations with Disability Resources for Students (DRS), please activate your accommodations via myDRS so we can discuss how they will be implemented in this course.

If you have not yet established services through DRS, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), contact DRS directly to set up an Access Plan. DRS facilitates the interactive process that establishes reasonable accommodations. Contact DRS at (www.disability.uw.edu).

## Safety 
Call SafeCampus at 206-685-7233 anytime – no matter where you work or study – to anonymously discuss safety and well-being concerns for yourself or others. SafeCampus’s team of caring professionals will provide individualized support, while discussing short- and long-term solutions and connecting you with additional resources when requested.

## Religious Accommodations 

Washington state law requires that UW develop a policy for accommodation of student absences or significant hardship due to reasons of faith or conscience, or for organized religious activities. The UW’s policy, including more information about how to request an accommodation, is available at Religious Accommodations Policy (https://registrar.washington.edu/staffandfaculty/religious-accommodations-policy/). Accommodations must be requested within the first two weeks of this course using the Religious Accommodations Request form (https://registrar.washington.edu/students/religious-accommodations-request/).”

[Home](index.md)
