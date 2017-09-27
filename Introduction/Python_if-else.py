#!/bin/python3

import sys


N = int(input().strip())
if N%2!=0 or (N<21 and N>5):
    print("Weird")
else:
    print("Not Weird")
