import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


# Lists, dicts, and sorting
l = [3, 5, 6, 1, -6]
d = {'a': 9, 'b': 2, 'c': 5, 'd': 3}
sl = sorted(l)
sorted(d)
sorted(d.values())
sorted(d.items())
print(l[:2])

# Capturing standard output
# Call this program in cmd/terminal and do: python program_name.py > captured_std_output.txt
print("Here's some text.")


# Enumerate()
for i, x in enumerate([1, 2, 3, 4, 5]):
    print("The index of {} is {}".format(x, i))

# # Inelegant, don't do:
# i = 0
# for x in [1,2,3,4,5]:
#     print("The index of {} is {}".format(x, i))
#     i += 1

# Plots
X = range(-5, 6)  # this actually ranges from -5 to 4
Y = [pow(x, 2) for x in X]

# Label the axes:
plt.xlabel('Integers')
plt.ylabel('f(x)')
# Control the scale of the Y-axis
plt.ylim([0, 30])
plt.plot(X, Y, label="X-squared")
plt.show()
plt.savefig('figures/parabola1.png')

# Add a second plot
Y2 = [pow(x, 3) for x in X]
plt.plot(X, Y2, 'o-', color='fuchsia', label="X-cubed")  # 'o-', '--'
plt.legend()
plt.savefig('figures/cube.png')


# Activity: Plot 4 different polynomial functions!
# https://github.com/olzama/Ling471/blob/gh-pages/assignments/activity_plots.py


# Bars
numbers = np.random.rand(10, 4)
# print(numbers)
# Let's use pandas visualization tools:
df = pd.DataFrame(numbers, columns=['a', 'b', 'c', 'd'])
print(df)
df.plot.bar().get_figure().savefig('figures/bars.png')
df.plot.barh().get_figure().savefig('figures/hbars.png')
df.plot.bar(stacked=True).get_figure().savefig('figures/stacked-bars.png')

# Pie chart
df = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
                   'radius': [2439.7, 6051.8, 6378.1]},
                  index=['Mercury', 'Venus', 'Earth'])
df.plot.pie(y='mass').get_figure().savefig('figures/pie.png')
fig = plt.figure()
subplots = df.plot.pie(subplots=True, figsize=(11, 6))
# Subplots will contain an object that has a savefig() function at index [0]:
subplots[0].get_figure().savefig('figures/pie1.png')

# Text
# Back to matplotlib:
plt.cla()  # Clear plot
plt.clf()
imdb = pd.read_csv('../datasets/my_imdb.csv')
text = imdb['review'][0]
print(text)
wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='blue',
                      collocations=False, stopwords=STOPWORDS).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('figures/wordcloud.png')
