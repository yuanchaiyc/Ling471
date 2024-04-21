import random as r
r.seed(20220426)
gold = r.choices([0, 1], k=15)
preds = r.choices([0, 1], k=15)

#let's see what zip() do
list(zip(gold, preds))

corr = sum(1 for g, p in zip(gold, preds) if g == p)
acc = corr / len(gold)

#OR
gold = r.choices([0, 1], k=15)
preds = r.choices([0, 1], k=15)
#when it comes to sum(), True = 1, False = 2
corr = sum(g == p for g, p in zip(gold, preds))
acc = corr / len(gold)

#OR
corr = 0
for i in range(len(gold)):
    g = gold[i]
    p = preds[i]
    if g == p:
        corr += 1
acc = corr / len(gold)



#------------------------
#Programming activity 1
#Consider a task of classifying tweets as political or not
#1 = political
#0 = not political
#You have 10 tweets, and the ground truth is:
ground_truth = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
#Calculate accuracy, precision, and recall if your system outputs:
prediction1 = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
prediction2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prediction3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
prediction4 = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]

#if we regard "political" as positive
relevant_class = 1
predict_list = prediction2
true_pos = sum(1 for x, y in zip(ground_truth, predict_list) if (x==y) and (y == relevant_class))
true_neg = sum(1 for x, y in zip(ground_truth, predict_list) if (x==y) and (y != relevant_class))
false_pos = sum(1 for x, y in zip(ground_truth, predict_list) if (x!=y) and (y == relevant_class))
false_neg = sum(1 for x, y in zip(ground_truth, predict_list) if (x!=y) and (y != relevant_class))

precision = true_pos/(true_pos + false_pos)
recall = true_pos/(true_pos + false_neg)

#------------------------
#Class

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def add(self, new):
        print(f'{new} added!')


lasagna_recipe = Recipe("Lasagna", ["pasta", "tomato sauce", "cheese", "beef"])

# Using methods of the Recipe class
lasagna_recipe.name
lasagna_recipe.ingredients
lasagna_recipe.add("Olive oil")


#-----------------------------------
#Programming activity 2
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def add(self, new):
        print(f'{new} added!')

    def prepare(self):
        # Method to prepare the dish
        print(f"Preparing {self.name} with ingredients: {', '.join(self.ingredients)}")


lasagna_recipe = Recipe("Lasagna", ["pasta", "tomato sauce", "cheese", "beef"])

# Using methods of the Recipe class

lasagna_recipe.add("Olive oil")
lasagna_recipe.prepare()

#----------------------------------
#Import multiple files from a folder
from pathlib import Path
p = Path(r'C:\Work\UW\teaching')
p = p / 'ling471'
#or
p = Path(r'C:\Work\UW\teaching')
p /= 'ling471'
#or
p = Path(r'C:\Work\UW\teaching')
p2 = Path('ling471')
p = Path(p, p2)
#They all produce WindowsPath('C:/Work/UW/teaching/ling471')


p = Path()
#Any files and folders in this path
p.glob('*')
#Store all Python files in this path to a list
py_files = list(p.glob('*.py'))
#Store all Python files in this path to a list using list comprehension
files = [x for x in p.glob('*.py') if x.is_file()]

p = Path(r'C:\Work\UW\teaching\ling471\class-demo\demo_042324\pythonProject1')
#Any files and folders in this path
list(p.glob('*'))
files = [x.stem for x in p.glob('*') if x.is_file()]
# ['test1', 'test2']
files = [x.name for x in p.glob('*') if x.is_file()]
# ['test1.txt', 'test2.txt']


#-------------------------
#Programming activity 3
from pathlib import Path
p = Path(r'C:\Work\UW\teaching\ling471\class-demo\demo_042324\pythonProject1')
p_pos = Path(p, r'tiny-test/hw3-pos')
p_neg = Path(p, r'tiny-test/hw3-neg')

#Any files and folders in this path
list(p_neg.glob('*.txt'))
list(p_pos.glob('*.txt'))
#Store all Python files in this path to a list using list comprehension
files_pos = [x for x in p_pos.glob('*.txt') if x.is_file()]
files_neg = [x for x in p_neg.glob('*.txt') if x.is_file()]


