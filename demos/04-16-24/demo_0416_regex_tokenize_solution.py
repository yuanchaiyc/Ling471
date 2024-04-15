import math
import statistics
import re
import nltk
import sys
#only download it once if prompt
#nltk.download('punkt')

if __name__ == '__main__':

    #import modules and use the methods in the moduel
    math.sqrt(4)
    sys.argv[0]
    #select specific parts of a module to import
    from math import sqrt
    sqrt(4)
    #rename improted modules
    import math as m
    m.sqrt(4)
    from math import sqrt as sq_root
    sq_root(4)

    #-------------------------------
    #Programming activity 1
    #Import the math module and try using the following functions
    #on whatever numbers you want: sin, cos, sqrt, pow, log, floor
    #Try any other functions or variables from the documentation that you think are interesting
    print(math.sin(1))
    print(math.sin(-1))
    print(math.cos(math.pi))
    print(math.sqrt(1))

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

    try:
        print(math.sqrt(-1))
    except:
        print('Sqrt can\'t handle complex components')
    else:
        print('Nothing went wrong')
    finally:
        print('The sqrt is finished')

    print(math.pow(4, 2))
    print(math.log(10))
    print(math.floor(3.14))

    #Make a list with the numbers 1 up to and including 10
    #and assign it to a variable (hint: use list(range()) )

    #Import the statistics module and try using the following functions: mean, median, stdev\

    #Call the sum function over your list and then divide the result by the length of the list (hint: len()).
    #Does it match the output of statistics.mean?

    #Try any other functions or variables from the documentation that you think are interesting
    a = list(range(1, 11))
    print(statistics.mean(a))
    print(statistics.median(a))
    print(statistics.stdev(a))
    print(sum(a) / len(a))

    #-------------------------------
    #Regular expression
    'ello' in 'hello'
    'halo' in 'hello'

    'hello'.count('l')
    'hello'.count('a')

    'hello'.replace('el','a')
    'hello'.replace('eel','a')
    'hello'.replace('l','')

    import re
    #find the plural nouns in the sentence
    re.findall(r'(\w+es)', 'the puppers and kitties played in the yard')
    #literal: family
    re.findall('family','family gathering')
    #disjunction (or)
    #?: means the things inside the parenthesis is non-capturing. Do not capture the piece in the parenthesis, so that you can match the entire string.
    re.findall(r'famil(?:y|ies)','Happy families are all alike; every unhappy family is unhappy in its own way.')
    #capture parenthesis
    re.findall(r'famil(y|ies)','Happy families are all alike; every unhappy family is unhappy in its own way.')

    #character class
    re.findall('[Tt]he', 'The news shows the current situation.')
    re.findall('bec[oa]me', 'She became a college student last week. Her parents\' dreams become true.')
    #[A-z] will match ASCII characters in the range from A to z
    #https://stackoverflow.com/questions/4923380/difference-between-regex-a-z-and-a-za-z
    re.findall('[A-z]', r'Asdfjc1124rBexzSdsf1234i809![]\_')
    #number
    re.findall('[0-9]', 'Asdfjc1124rBexzSdsf1234i809!')
    #+ one or more times
    re.findall('[0-9]+', 'Asdfj0c1124rBexzSdsf1234i809!')
    #* zero or more times
    re.findall(r'[0-9]*', 'I have 3 apples and 12 strawberries')
    #? zero or one time
    re.findall(r'[0-9]?', 'I have 3 apples and 12 strawberries')
    re.findall(r'colou?r', 'colour could also be spelled as color')
    #match one and only one digit
    re.findall(r'[0-9]', 'I have 3 apples and 12 strawberries')
    #. any character
    re.findall(r'.', 'I have 3 apples and 12 strawberries')
    #escape special character to make them literal
    re.findall(r'\.', 'I have 3 apples and 12 strawberries')
    #\w characters that can make words
    re.findall(r"\w","word_?.,[]")
    #\s whitespace
    re.findall(r'\s', 'I have 3 apples and 12 strawberries')
    print('\n')  # line returned
    print('\\n')  # \n
    print(r'\n')  # \n
    print(r'\\n')  # \\n

    #would work. \n is new line in regular expression and regular string
    re.findall('\n', 'hello\nworld')
    re.findall(r'\n', 'hello\nworld')
    re.findall(r'\n', r'hello\nworld')


    #wouldn't work. \s is treated as space
    re.findall("\section", '\section')
    #wouldn't work. first \ escape second \, making \s literal for regex, but \s means space in regex
    re.findall("\\section", '\section')
    #wouldn't work. \s is treated literally, but in regex, \s means space
    re.findall(r"\section", '\section')
    #would work. \ escape \\s, making \\s literal
    re.findall("\\\section", '\section')
    #would work. first \ escape second \; third \ escape fourth \
    re.findall("\\\\section", '\section')
    #would work. \\s is treated literally. And first \ escape second \, meaning \ will be treated literal
    re.findall(r"\\section", '\section')

    re.findall(r'\w\d+\w', 'abc123def')  # ['c123d']
    re.findall('\w\d+\w', 'abc123def')  # ['c123d’]


    #re.sub
    re.sub(r'\d+', '2024', 'abcdefg2023')
    #re.findall
    re.findall(r'\w\d+\w', 'abcdef2023g')
    #re.finditer
    for match in re.finditer(r'\d{2}', 'abcdef2023g'):
        print(match)
        print(match.group())

    #--------------------------------
    #Programming activity 2
    #Assign the string "The passcode is 8675309. Please remember it." to a variable
    #Use re.findall or re.sub to do the following:
    # Extract just the passcode
    # Change the passcode to "555-5555"
    # Extract all words that start with "p"
    # Extract the first word of each sentence
    # Delete the word "Please" and capitalize "remember" afterward. This can be done with just a single replacement!
    # Change each "." to "!"

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

    # Delete "Please" and capitalize the first letter of "remember"
    p = re.sub('Please r', 'R', s)
    print(p)
    print(s.replace('Please r', 'R'))

    p = re.sub(r'.', '!', s)
    print(p)

    #-----------------------------
    #Tokenization
    'the brown cow'.split()
    'The brown cow eats.'.split()
    #use regex to tokenize; maybe too complicated to write
    re.findall('\w+', re.sub('![\w|\s]', '', re.sub('[A-Z]', lambda x: x.group(0).lower(), 'The brown cow ate.')))

    #doesn't handle contraction too well
    re.findall('\w+', re.sub('![\w|\s]', '', re.sub('[A-Z]', lambda x: x.group(0).lower(), 'This\'s my friend. That\'s Sofia\'s friend')))

    #use nltk
    from nltk.tokenize import word_tokenize
    s = 'This\'s a sentence. It includes punctuation, and includes punctuation, and handles abbreviation such as St., Ave., and Dr.'
    word_tokenize(s)


    #-----------------------------
    #Programming activity 3: tokenization
    s = 'Here is some simple text to work with.'
    print(nltk.tokenize.word_tokenize(s))

    s = '[hɪɹ iz sʌm tɛkst ɹɪʔn̩ juzɪ̃ŋ ði a͡ɪ pʰi eɪ]'
    print(nltk.tokenize.word_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = '这是一些中文。'
    print(nltk.tokenize.word_tokenize(s))
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'here is some more lovely 😘😍 text to look at, but I don\'t like it 😤😤😡😡'
    print(nltk.tokenize.word_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'She said, \'Today is a nice day!\''
    print(nltk.tokenize.word_tokenize(s))
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = "I was told not to use lots of contractions, but the lessons mustn't've stuck because I'd've preferred to never've done that within a day's time but especially if'n I spent some time doing in rural ID, U.S.A. at B.S.U."
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = "I'm going to use lots of abbrvns. in this sentnce, such as Abd., Aberd., Aberdeensh., abl., etc."
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'I\'m going to put some linguistics abbrvns., such as ABESS, ABIL, ABL., ABS., ARG., PROG., PERF.'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    from nltk.tokenize import wordpunct_tokenize as wt

    s = 'Some people write money as $2.44, but others write it as 2.44$.'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))

    s = 'Some people eat at Arby\'s.'
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))
