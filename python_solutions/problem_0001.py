# 
# Problem #1:   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#               Find the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1
# 

def calculate_sum():
    s = 0
    for i in range(1000):
        if not i % 3 or not i % 5:
            s += i
    return s

def main():
    s = calculate_sum()
    print(s)
    return s

if __name__ == "__main__":
    main()