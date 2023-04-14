
if __name__ == '__main__':
    i = 1
    while i <= 10:
        print(i)
        i += 1

    a = [1, 2, 3, 4, 5]
    print(10 in a)

    for i in range(1, 11):
        print(i)

    for c in 'ling471':
        print(c)

    # while True:
    #     print('I am looping')

    while False:
        print('Is this true?')

    for x in []:
        print('What is for?')

    # empty dict
    d = {}
    d['a'] = 1
    print(d)
    d[1] = 'b'
    print(d)
    print(2 in d)
    print('a' in d)
    d['a'] = 2
    print(d)

    d = {}
    for x in range(1, 5):
        d[x] = x**2
    print(d)

    with open('lowercasetext.txt', 'r', encoding='utf-8') as f:
        s = f.read()
    s_new = s.upper()
    with open('uppercasetxt.txt', 'w', encoding='utf-8') as w:
        w.write(s_new)