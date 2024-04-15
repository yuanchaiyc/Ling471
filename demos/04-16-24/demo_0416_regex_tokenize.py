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

    #Make a list with the numbers 1 up to and including 10
    #and assign it to a variable (hint: use list(range()) )

    #Import the statistics module and try using the following functions: mean, median, stdev

    #Call the sum function over your list and then divide the result by the length of the list (hint: len()).
    #Does it match the output of statistics.mean?

    #Try any other functions or variables from the documentation that you think are interesting

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

    # Delete the word "Please" and capitalize the first letter of "remember" afterward.
    # This can be done with just a single replacement!

    # Change each "." to "!"

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
    #Try to come up with a sentence that NLTK's function does not correctly tokenize
    #Try messing with capitalization, foreign characters/words, abbreviations, contractions, colloquial language, etc.

    #Tokenize the same string with different methods:
    # nltk.tokenizer.word_tokenize
    # nltk.tokenizer.wordpunct_tokenize
    # nltk.tokenize.regexp.wordpunct_tokenize

    s = ""

    print(nltk.tokenize.word_tokenize(s))
    print(nltk.tokenize.wordpunct_tokenize(s))
    print(nltk.tokenize.regexp.wordpunct_tokenize(s))