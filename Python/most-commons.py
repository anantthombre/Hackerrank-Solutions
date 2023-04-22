# Link to the coding question -  https://www.hackerrank.com/challenges/most-commons

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s = sorted(s)
    
    Frequency = Counter(list(s))
    for k,v in Frequency.most_common(3):
        print(k, v)
 
