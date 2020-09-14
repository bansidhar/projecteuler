'''
Problem #3:   
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
'''

import math

def get_max_prime_factor(n):
  m = 0
  while not n%2:
    m = 2
    n = n/2

  for i in range(3, int(math.sqrt(n)+1), 2):
    if not n%i:
      m = i
      n = n/i
  return m

def main():
  n = 600851475143
  m = get_max_prime_factor(n)
  print (m)
  
if __name__ == "__main__":
    main()
