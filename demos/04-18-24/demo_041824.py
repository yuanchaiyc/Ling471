
if __name__ == '__main__':
    # validation
    # k-fold validation
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import load_iris
    # Load dataset
    iris = load_iris()
    x = iris.data
    y = iris.target

    # Initialize logistic regression model
    model = LogisticRegression()

    # Initialize k-fold cross-validation
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)

    # Perform k-fold cross-validation
    scores = cross_val_score(model, x, y, cv=kfold)

    # Print the cross-validation scores
    print("Cross-validation scores:", scores)

    # Print the average accuracy
    print("Average accuracy:", scores.mean())

    # Leave-one-out cross-validation
    from sklearn.model_selection import LeaveOneOut
    model = LogisticRegression(max_iter=1000)
    loo = LeaveOneOut()

    # Perform leave-one-out cross-validation
    scores = cross_val_score(model, x, y, cv=loo)

    # Print the cross-validation scores
    print("Cross-validation scores:", scores)

    # Print the average accuracy
    print("Average accuracy:", scores.mean())

    #--------------------------------------
    #Programming activity 1
    # print letters a to z
    for i in range(ord('a'), ord('z')):
        print(chr(i))

    # print letters A to Z and same them to a list

    #convert the following string to lowercase
    s = 'bUT i dOn\'T liKE eAtINg vegETAblEs!'
    # lower case
    s_lower = ''

    for c in s:
        n = ord(c)
        # if 65 <= n <= 90:
        if ord('A') <= n <= ord('Z'):
            #change pass to your code
            pass
        else:
            #change pass to your code

    print(s_lower)

    s_upper = ''
    # upper case
    for c in s:
        n = ord(c)
        # if 97 <= n <= 122:
        if ord('a') <= n <= ord('z'):
            #change pass to your code
            pass
        else:
            #change pass to your code
            pass

    print(s_upper)

    #------------------------------
    # list comprehension
    # non-comprehension way
    a = [1, 2, 3]
    a = []
    for i in range(1, 4):
        a.append(i)
    a = list(range(1, 4))
    b = []
    for x in a:
        if x % 2 == 0:
            b.append(x)

    # using list comprehension
    a = [x for x in range(1, 4)]
    a = [y * 2 for y in range(1, 4)]
    a = [z ** 2 for z in range(1, 4)]
    a = [1 for i in range(1, 4)]

    a = [x for x in range(21) if x % 2 == 0]
    b = [37, 234, 853, 95, 13, 264, 38]
    b = [x for x in b if x % 2 == 0]
    sentence = 'This is how cats and dogs get along'
    c = [x for x in sentence.split() if x.endswith('s')]
    c = [x for x in sentence.split() if re.match("\w+s", x)]

    import re
    wordlist = ["apple", "banana", "cherry", "1234", "orange", "5678"]
    # if something is matched, it is equivalent to passing "True" to "if".
    # if you write if [1,2,3,4], it will always be if True.
    filtered_words = [word for word in wordlist if re.match("^[a-zA-Z]+$", word)]

    #generator comprehension
    s = sum(x for x in range(11))
    d = {k: k ** 2 for k in range(11)}

    #it gets unreadable very soon
    s = "123 345 47 898"
    [math.cos(int(x.strip()) ** 2) if int(x.strip()) % 2 == 1 else 0 for x in s.split()]
    [(x, y, z) for x in range(10) for y in range(10) for z in range(10)]

    #-------------------------------
    #Programming activity 2
    #Using list comprehensions, do the following:
    #Create a list from 0 up to and including 10000

    #Create a list that squares all the numbers from the previous list

    #Create a list that only includes odd numbers from 0 up to and including 9877

    #Create a list that has converted each word in the following string to lowercase: "tHIs iS A sENtENce thaT hAS miXeD cASe"

    #Create a list that has called ord() on the characters in the example string 'The quick brown fox jumped over the lazy dog’


    #Using a generator comprehension
    #Create a dict that maps all integers from 0 up to and including 10000 to their square roots


    #Sum the value of all even numbers from 0 up to and including 4578

