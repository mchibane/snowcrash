#!/usr/bin/python

import sys

str = ""
for i in range(len(sys.argv[1])):
        str += chr(ord(sys.argv[1][i]) - i)

print(str)

