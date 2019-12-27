#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(0, n):
        for j in range(0, n-(i+1)):
            print(' ', end='')
        for j in range(0, i+1):
            print('#', end='')
        print()


if __name__ == '__main__':
    n = int(input())

    staircase(n)
