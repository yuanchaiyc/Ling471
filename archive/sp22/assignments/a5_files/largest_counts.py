import sys
import pandas as pd

# From Assignment 2, copied manually here just to remind you
# that you can copy stuff manually if importing isn't working out.
# You can just use this or you can replace it with your function.


def countTokens(text):
    token_counts = {}
    tokens = text.split(' ')
    for word in tokens:
        if not word in token_counts:
            token_counts[word] = 0
        token_counts[word] += 1
    return token_counts


def largest_counts(data):  # TODO: Finish implementing this function

    # TODO: Cut up the rows in the dataset according to how you stored things.
    # The below assumes test data is stored first and negative is stored before positive.
    # If you did the same, no change is required.
    neg_test_data = data[:12500]
    neg_train_data = data[25000:37500]
    pos_test_data = data[12500:25000]
    pos_train_data = data[37500:50000]

    # TODO: SORT the count dicts which countTokens() returns
    # by value (count) in reverse (descending) order.
    # It is your task to Google and learn how to do this, but we will help of course,
    # if you come to use with questions. This can be daunting at first, but give it time.
    # Spend some (reasonable) time across a few days if necessary, and you will do it!

    # As is, the counts returned by the counter AREN'T sorted!
    # So you won't be able to easily retrieve the most frequent words.

    # NB: str.cat() turns whole column into one text
    train_counts_pos_original = countTokens(pos_train_data["review"].str.cat())
    train_counts_pos_cleaned = countTokens(
        pos_train_data["cleaned_review"].str.cat())
    train_counts_pos_lowercased = countTokens(
        pos_train_data["lowercased"].str.cat())
    train_counts_pos_no_stop = countTokens(
        pos_train_data["no stopwords"].str.cat())
    train_counts_pos_lemmatized = countTokens(
        pos_train_data["lemmatized"].str.cat())

    # Once the dicts are sorted, output the first 20 rows for each.
    # This is already done below, but changes may be needed depending on what you did to sort the dicts.
    # The [:19] "slicing" syntax expects a list. If you sorting call return a list (which is likely, as being sorted
    # is conceptualy a properly of LISTS,  NOT dicts),
    # you may want to remove the additional list(dict_name.items()) conversion.
    with open('counts.txt', 'w') as f:
        f.write('Original POS reviews:\n')
        for k, v in list(train_counts_pos_original.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Cleaned POS reviews:\n')
        for k, v in list(train_counts_pos_cleaned.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lowercased POS reviews:\n')
        for k, v in list(train_counts_pos_lowercased.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('No stopwords POS reviews:\n')
        for k, v in list(train_counts_pos_no_stop.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lemmatized POS reviews:\n')
        for k, v in list(train_counts_pos_lemmatized.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        # TODO: Do the same for all the remaining training dicts, per Assignment spec.

    # TODO: Copy the output of the above print statements
    #  into your document/report, or otherwise create a table/visualization for these counts.
    # Manually is fine, or you may explore bar charts in pandas! Be creative :).


def main(argv):
    data = pd.read_csv(argv[1], index_col=[0])
    # print(data.head())  # <- Verify the format. Comment this back out once done.

    largest_counts(data)


if __name__ == "__main__":
    main(sys.argv)
