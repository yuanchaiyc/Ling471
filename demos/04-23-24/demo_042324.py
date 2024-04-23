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


lasagna_recipe = None

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