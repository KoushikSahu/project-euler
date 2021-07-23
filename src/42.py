import math, statistics, collections
from typing import List

"""
    Author: Koushik Sahu
    Created: 23 July 2021 Fri 22:23:57
"""

def binary_search(a: List[int], val: int) -> bool:
    low = 0
    high = len(a)-1
    ans = False

    while low <= high:
        mid = low + ((high-low) // 2)
        if a[mid] == val:
            ans = True
            break
        elif a[mid] > val:
            high = mid-1
        else:
            low = mid+1

    return ans

if __name__ == '__main__':
    t = [(n*(n+1))/2 for n in range(1, 100)]
    val = []

    with open('../assets/p042_words.txt', 'r') as f:
        content = f.read()
        for word in content.split(','):
            val.append(word[1:-1])
    
    ans = 0
    for word in val:
        word_val = 0
        for letter in word:
            word_val += (ord(letter)-ord('A')+1)
        if binary_search(t, word_val) == True:
            ans += 1

    print(ans)
