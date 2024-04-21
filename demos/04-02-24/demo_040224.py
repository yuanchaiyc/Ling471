import sys

#you can print something directly by pass it to the print() fucntion

print('Jane Eyre')

import os
#The text might be stored in a file and you want to print the file
#path = r"C:\Work\UW\teaching\ling471\class-demo\demo_04022024_pythonproject\pythonProject\janeeyre.txt"
#path_modify = os.path.normpath(path)

path = 'janeeyre.txt'

#open the file
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

#use configure to open the file
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

