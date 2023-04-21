import math
import statistics
import re
import nltk
if __name__ == '__main__':

    print(math.sin(1))
    print(math.sin(-1))
    print(math.cos(math.pi))
    print(math.sqrt(1))
    try:
        print(math.sqrt(-1))
    except:
        print('Sqrt can\'t handle complex components')
    print(math.pow(4, 2))
    print(math.log(10))
    print(math.floor(3.14))

    a = list(range(1, 11))
    print(statistics.mean(a))
    print(statistics.median(a))
    print(statistics.stdev(a))
    print(sum(a) / len(a))

    print('----REGEX ACTIVITY-----')

    s = 'The passcode is 8675309. Please remember it.'
    p = re.findall(r'\d+', s)[0]
    print(f'Just the passcode {p}')

    p = re.sub('\d+', '555-5555', s)
    print(f'Changed {p}')
    # All words that start with "p"
    p = re.findall(r'p\w+', s)
    print(f'All words that start with "p" {p}')

    # First word of each sentence
    p = re.findall(r'[A-Z]\w+', s)
    print(f'First word of each sentence {p}')

    # Delete "Please" and capitalize "remember"
    p = re.sub('Please r', 'R', s)
    print(p)
    print(s.replace('Please r', 'R'))

    p = re.sub(r'.', '!', s)
    print(p)

    s = 'Here is some simple text to work with.'
    print(nltk.tokenize.word_tokenize(s))

    s = '[hɪɹ iz sʌm tɛkst ɹɪʔn̩ juzɪ̃ŋ ði a͡ɪ pʰi eɪ]'
    print(nltk.tokenize.wordpunct_tokenize(s))

    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'here is some more lovely 😘😍 text to look at, but I don\'t like it 😤😤😡😡'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = "I was told not to use lots of contractions, but the lessons mustn't've stuck because I'd've preferred to never've done that within a day's time but especially if'n I spent some time doing a Ph.D. in rural ID, U.S.A. at B.S.U."
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = "I'm going to use lots of abbrvns. in this sentnce, lots of FCNs are used to write code for Ph.D.'s and M.Sc.'s in Edmonton, AB, Canada."
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    from nltk.tokenize import wordpunct_tokenize as wt

    s = 'Some people write money as $2.44, but others write it as 2.44$.'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'Some people eat at Arby\'s.'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    nltk.tokenize.wordpunct_tokenize('blah', )