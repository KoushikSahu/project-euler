import math, statistics, collections

"""
    Author: Koushik Sahu
    Created: 18 July 2021 Sun 21:41:18
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_binary_palindrome(n):
    return is_palindrome(bin(n).replace('0b', ''))

if __name__ == '__main__':
    ans_list = list()

    for i in range (1, 1000001):
        if is_palindrome(i) and is_binary_palindrome(i):
            ans_list.append(i)

    print(ans_list)
    print(sum(ans_list))
