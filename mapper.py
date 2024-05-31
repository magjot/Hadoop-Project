#!/usr/bin/env python3

import sys
import string

# Student ID: <Replace with your ID number>

excluded = {"i","not","is"}

def eprint(*args, **kwargs):
    print(*args,file=sys.stderr,**kwargs)

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # Get the type of review, the review text and the sentiment    
    (type,review,sentiment) = line.split('\t')

    # Print the type and sentiment
    # Note that this is not the required output for a valid solution
    # and will just give a count of how many reviews of each type there are.
    # You will need to change the code from this point onward to meet the
    # assignment requirements.           
    print('%s\t%s' % (type,1))
        