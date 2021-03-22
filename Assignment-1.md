[Home](index.md)

## Assignment 1: Preliminaries

In this assignment, you will:

* Download the data you will be working with in all (or most) of the assignments.
* Start thinking about language data in data science and machine learning terms.
* Create and start using a personal repository on GitHub where you will store your code for the class.
* Start learning how to program in python using the VS Code IDE.
* Learn how to connect to a remote server and run a python and git there.


Submission summary:
* Part 1: A text file answering questions about the IMDB review dataset.
* Part 2: Private GitHub repository created; Olga and Yuanhe added as collaborators.
* Part 3: 
   * A file called your-UW-NetID-assignment1.py in your repository
   * A question/comment in the Discussion area for Assignment 1 related to how things are organized in VS Code (note: a question about installation won't count here!)
   * A question/comment in the Discussion area for Assignment 1 related to Source Control and how to stage, commit, push, and pull changes using e.g. VS Code. (You can use command line if you know how to do it, or some other tool).
* Part 4: Your program from Part 3 submitted to the "patas" cluster.

### Part 1: The IMDB review dataset
We will be using the IMDB review dataset ([Maas et al. 2011](https://www.aclweb.org/anthology/P11-1015.pdf))
1. Download the dataset from [here](https://ai.stanford.edu/~amaas/data/sentiment/).
1. Unpack the dataset by double-clicking on it or by using a utility appropriate for your OS.
1. Read the README file which comes with the dataset.
1. In a text file, answer the following questions about the dataset:
   1. How many movie reviews does it contain?
   1. How is the dataset divided? (Here, talk about how many reivews are in each folder and what does each folder represent, in your own words. Do not copy the text from the README file)
   1. **Why** is it divided in this way? (Make sure to give a thoughtful answer here, at least a paragraph! You may not yet know everything about this, but answer the best you can, based on what you learned in the first couple weeks of class.)
   1. Why is a citation to the ACL paper by Maas et al. included in the README file and in the dataset description on the website? (**What is the relationship of the paper and of the dataset?** Thoughtful, paragraph-length answer here.)
   1.  Why is there a reference to Potts's paper?
   1. Would you say this README file qualifies as a "data statement" (see [Bender and Friedman](https://watermark.silverchair.com/tacl_a_00041.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAn0wggJ5BgkqhkiG9w0BBwagggJqMIICZgIBADCCAl8GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMDw2APtHtVVWN-T_FAgEQgIICMJJiPYGe86AdkkndbKNqCkMo2DXV54WMBqxsCkxZhHFR244ZkPQPLEAzcvk5QOLNmWQ-I_OYdt_t6kUDrF05VafErnhrEa6iJhePeSUggTryv01s2rO3dgopekdHWdvN4gbajwNN4k3heiTu_avCJPkO7xIwG81qf_KWFfwsgOth1F9UFJIhRudTmCQhDHb_PSu5NSjBvzKJL4ab1KNDrqN8BbHUyAq92lnnRUUWhnBCfMcVeW2e8hcBhmUAm40pCdUw32qcVcjC0ldztvwun5x2oPxtuR_PsCmzAsIHuCoTIdYDpMktBDADRtVmHV0Z-xQuPyNoiMPcGhv05LJGlMSDCooFQeS8dV62h-ZhBKFKqTPBo9TtbUoO6ynZNq0tWlLzP1RpVdMdzUnCO2Kv31css4JNd-oHUqghGC_TcLlSb5jesPNUYOEowxQGbMO5T6tEMe-NssBxeawnHrAw4vGXg0gGVn1klLpgMrXs-i_aoui1k-UH4L-nd6dp3687yt3GbS6KHVOA34B6RcgudaLOW50EbYr4pzOU6Y4FGrPyIDfDxwP_OWpKh5WRFQDKQ7fqZhgErcSouLMTFuXP9VXkztp53mj8kas92wF9Ye3AT9Ov1kdv7ofgsq8IscF8e9NTtWsyvESDoybMKtvTtlHHXM4WcACjYfRxQS6wxXrMSvXJM41jpz8GqMjk2vS-vUVIDZaom0OUKUrUv1GcnhIUzZbIIXBjeI6dMyiLQVYQ) paper which was assigned earlier). If yes, point to the specific portions of the file and map them to corresponding definitions from Bender and Friedman's paper. If no, explain what a data statement could look like for such a dataset or why the concept does not apply here. You can of course argue against data statements here if you like! It is up to you; what counts is the depth and quality of argument.
1. Submit your text file **to Canvas**, in the appropriate area associated with Assignment 1.

### Part 2: Your GitHub repository
In this part of the assignment, you will create a GitHub repository for your code in this class.
1. Create an account on https://github.com/
2. Create a new repository; make it private. Call it whatever you like, but you will use it for this class. The screenshot below shows what creating a repository looks like on GutHub:

<img width="736" alt="Screen Shot 2021-03-22 at 12 35 41 PM" src="https://user-images.githubusercontent.com/10963114/112048004-34b35080-8b0b-11eb-90e8-12cce9c612dd.png">

3. After you've created the repository, note its https:// address:

<img width="1287" alt="Screen Shot 2021-03-22 at 12 04 44 PM" src="https://user-images.githubusercontent.com/10963114/112044524-26fbcc00-8b07-11eb-9dff-05106a9234ba.png">

4. Go to setting and add olzama and FIXME: Yuanhe as "collaborators" (**NB:** this counts as your **submission** for this task):

<img width="1286" alt="Screen Shot 2021-03-22 at 12 22 26 PM" src="https://user-images.githubusercontent.com/10963114/112046453-4a277b00-8b09-11eb-85e9-acecf900369b.png">


### Part 3: Python and Visual Studio Code.
In this part of the assignment, you will start learning how to program in python and how to use an Integrated Development Environment.
1. Download and install [Visual Studio Code](https://code.visualstudio.com/download), a **free** IDE. Use all the default settings during the installation.
2. Install support for python by clicking on "Python" here:

<img width="1019" alt="python1" src="https://user-images.githubusercontent.com/10963114/112042641-fc107880-8b04-11eb-8fcf-d4d3871df483.png">

3. Now, clone the repository you've created in Part 2 into VS Code. Click on "clone a repository" and then enter the https:// address of your repository. Then choose a folder for the local copy of the repository to go to. It can be any folder on your computer, such as one dedicated to this class.

<img width="1368" alt="Screen Shot 2021-03-22 at 12 05 23 PM" src="https://user-images.githubusercontent.com/10963114/112044654-498de500-8b07-11eb-8f61-f4bbd940fd98.png">

4. Locate the local copy of your repository on your computer. (Navigate to the folder which you chose when cloning.) This is what it looks like in my Finder (I use a Mac):

<img width="772" alt="Screen Shot 2021-03-22 at 12 11 28 PM" src="https://user-images.githubusercontent.com/10963114/112045157-c15c0f80-8b07-11eb-9fe0-87c36e404f16.png">

5. Add a python file to your repository. You can do it any way you like, including from within VS Code:

<img width="833" alt="Screen Shot 2021-03-22 at 12 13 59 PM" src="https://user-images.githubusercontent.com/10963114/112045463-1f88f280-8b08-11eb-9a96-edd63c825887.png">

6. Write a program in python which prints a statement, such as "Hello, world!" (or whatever you like).

7. Find the Source Control menu in the left panel. Then find the small icon which is for "staging changes" and click on it. You will then see something like this:

<img width="934" alt="Screen Shot 2021-03-22 at 12 24 10 PM" src="https://user-images.githubusercontent.com/10963114/112046758-ac807b80-8b09-11eb-8f22-787ea6eae364.png">

8. Click on the "check mark"; it means committing the staged changes.

9. Now click on the "...", find the command "Push", and click it. 

10. Now check that your python file can be found not only in the local copy but also in the remote repository. (NB: This will count as your **submission** for this task.)

<img width="962" alt="Screen Shot 2021-03-22 at 12 31 09 PM" src="https://user-images.githubusercontent.com/10963114/112047449-8ad3c400-8b0a-11eb-83cb-8e620988fad3.png">

11. Write something in your README file using the GitHub website. Click on the README file, click on edit, write something, then click on "Commit changes".
[Home](index.md)

<img width="1096" alt="Screen Shot 2021-03-22 at 12 53 47 PM" src="https://user-images.githubusercontent.com/10963114/112050069-a8eef380-8b0d-11eb-900e-a3af67081026.png">

<img width="816" alt="Screen Shot 2021-03-22 at 12 54 49 PM" src="https://user-images.githubusercontent.com/10963114/112050206-ce7bfd00-8b0d-11eb-8bb1-943a1f182d95.png">

12. Now go to your VS Code, to the Source Control pane, find "Pull" under "..." and pull the changes into your local copy of the repository. Make sure that you now see the updated README!

### Part 4: Command line and remote servers

It is important to be able to connect to a remote server and to be able to copy files between that server and your machine. It is also important to be able to run things like python or git via the command line (rather than in an IDE such as VS Code or in a GUI such as github.com).

1. Open a terminal on your Linux/Mac or Windows 10 (if you have an earlier version of Windows, you will need additional instructions, so contact Olga and Yuanhe ahead of time).
2. Connect to patas cluster (where you should have created an account last week!):
`ssh your-NetID@patas.ling.washington.edu`

(It will ask you whether you should add patas to trusted hosts; type yes.)

3. Clone your git repository into your home directory on patas:
`git clone your-repo-address`

(It will ask you for your GitHub username and password. There may be some error messages; ignore them. Just make sure you type your password correctly.)

4. Navigate into your repository folder on patas. Execute the python program and observe it printing whatever it prints.

<img width="460" alt="Screen Shot 2021-03-22 at 1 45 46 PM" src="https://user-images.githubusercontent.com/10963114/112056206-fc187480-8b14-11eb-99c6-cbe36e422261.png">

5. Copy your python program to FIXME (the class folder).
