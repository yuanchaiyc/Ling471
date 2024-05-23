__author__ = 'Yuan Chai'
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Examples: Bar plot
'''
# Sample data for three series
categories = ['The', 'cat', 'chase', 'dog']
values = [1781580, 428363, 556892, 1131181]

# Create a DataFrame
df = pd.DataFrame({
    'Category': categories,
    'Value': values,
})

# Plot the stacked bar plot
plt.bar(df['Category'], df['Value'], label = "values")

# Add title and labels
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()

'''
Example: Grouped bar plots
'''
categories = ['train_accuracy_pos', 'train_precision_pos', 'train_recall_pos', 'train_precision_neg', 'train_recall_neg',
              'test_accuracy_pos', 'test_precision_pos', 'test_recall_pos', 'test_precision_neg', 'test_recall_neg']
original = np.random.rand(10)
clean = np.random.rand(10)
lowercase = np.random.rand(10)
no_stop = np.random.rand(10)
lemmatized = np.random.rand(10)

# Create a DataFrame
df = pd.DataFrame({
    'category': categories,
    'original': original,
    'clean': clean,
    'lowercase': lowercase,
    'no_stop': no_stop,
    'lemmatized': lemmatized
})

# Width of each bar
bar_width = 0.15
group_gap = 0.5

# Set position of bars on X axis
bar_positions = np.arange(len(df['category'])) + 5
bar1 = bar_positions
bar2 = bar1 + bar_width
bar3 = bar1 + 2 * bar_width
bar4 = bar1 + 3 * bar_width
bar5 = bar1 + 4 * bar_width

# Create the figure
plt.figure(figsize=(14, 8))
# Plot the bars
plt.bar(bar1, df['original'], color='b', width=bar_width, edgecolor='grey', label='Original')
plt.bar(bar2, df['clean'], color='g', width=bar_width, edgecolor='grey', label='Clean')
plt.bar(bar3, df['lowercase'], color='r', width=bar_width, edgecolor='grey', label='Lowercase')
plt.bar(bar4, df['no_stop'], color='c', width=bar_width, edgecolor='grey', label='No Stop Words')
plt.bar(bar5, df['lemmatized'], color='m', width=bar_width, edgecolor='grey', label='Lemmatized')

# Add title and labels
plt.title('Grouped Bar Plot of Different Text Processing Techniques')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(bar1 + 2 * bar_width, df['category'], rotation=90)

# Add legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()



#----------------------------------------
# Exercises
categories = ['accuracy', 'precision_pos', 'recall_pos', 'precision_neg', 'recall_neg']*2
type = ['train', 'train', 'train', 'train', 'train', 'test', 'test', 'test', 'test', 'test']
values = [0.9736, 0.9833, 0.9635, 0.9642, 0.9836,
          0.8697, 0.9011, 0.8305, 0.8428, 0.9089]

# Create a DataFrame
df = pd.DataFrame({
    'category': categories,
    'type': type,
    'value': values,
})

# TODO: Given the dataset, plot two bar plots, one for train, the other for test

# TODO: Rearrange the dataset, so that you can group things either by test/train, or by the error analysis values
