#!/bin/python3

"""
Initially attempted recursion but realized its way more efficent to just do a while loop
like no need to be fancy it makes a lot of sense. I am using an algorithim so it is still
better than brute forcing my way through it.
"""

import os
import sys


#
# Complete the getMoneySpent function below.

def getMoneySpent(keyboards, drives, b):
    kbs = sorted(keyboards)
    dr = sorted(drives)
    print(kbs[-1])
    closest = -1
    while len(kbs) >= 1 and len(dr) >= 1:
        print(kbs, dr)
        if kbs[-1] + dr[0] > b:
            kbs = kbs[:-1]
        else:
            closest = max(kbs[-1] + dr[0], closest)
            dr = dr[1:]
    return closest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
