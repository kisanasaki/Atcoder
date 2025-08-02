# j - Aj= i + Ai
# (4,7) 7 - 2 = 4 + 1 = 5
# 9
# 3 1 4 1 5 9 2 6 5
from collections import Counter

N = int(input())
A = list(map(int, input().split()))  # A: 整数列

def count(N, A):
    counter = Counter()
    ans = 0
    for j in range(N):
        key = j - A[j]           
        ans += counter[key]      
        counter[j + A[j]] += 1
    return ans

print(count(N, A))