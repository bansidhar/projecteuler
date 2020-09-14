'''
Problem #4:   
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4
'''

import math

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_largest_palindrome():
    l = 999 * 999
    while l:
        print(l)
        if is_palindrome(l):
            return l
        l -= 1
    return l

def main():
    m = get_largest_palindrome()
    print (m)
  
if __name__ == "__main__":
    main()