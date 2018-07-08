# coding: utf-8
import sys
sys.setrecursionlimit(1500)
def recursion(n):
    if(n <= 0):
        print(n)
        return
    print(n)
    recursion(n - 1)

if __name__ == "__main__":
    recursion(1200)