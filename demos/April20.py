# Import statements

import re


def main():
    print("hello")

    # Regular expressions
    # Searching

    ts = "Testing regular expressions."
    pat = 's'
    m = re.search(pat, ts)

    if not m:  # the same as if m != None
        print("pattern not found.")

    # Iterating
    ms_list = re.findall(pat, ts)  # findall() returns a list of just strings
    # finditer() returns a list of special "match" objects
    ms = list(re.finditer(pat, ts))
    for m in ms:
        print(m.group(0))  # goup(0): access the surface form of the match

    # Substituting
    ts = "And, so, it, begins."  # Overwriting the previous value of ts!
    # Splitting thes tring by comma:
    toks = ts.split(',')  # strip() helps with cleaning up initial spaces
    pat = "begins"
    sub = "began"
    # Assignment: First, execute re.sub, then assign the value it returned to the variable ts
    ts = re.sub(pat, sub, ts)

    # Using regex to remove commas, dots, question marks, and exclamation marks from the text.
    pat = "[,.?!]"
    new_ts = re.sub(pat, '', ts)
    # Can put break point here to make sure the debugger doesn't exit the program:
    print("stop")


if __name__ == "__main__":
    main()
