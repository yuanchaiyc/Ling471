import random

#This is an illustration on the function of the debugger

#create a function of addition for adding to numbers up.
def add(a, b):
    c = a+b
    return(c)

def main():
    #create an empty list
    a = []
    #create a for loop that will iterate five times
    for i in range(0, 5):
        #generate a random integer between 0 and 10
        b = random.randint(0, 10)
        #add the randomly generated integer with itself plus 2
        c = add(b, b+2)
        #append the result to the empty list
        a.append(c)

if __name__ == "__main__":
    main()