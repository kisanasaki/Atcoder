import sys
import math
input = sys.stdin.read

# 等比数列になれるか調べる

# 並べ変えても公比は変わるが等比数列は成立。
# 公比=1/2,2
# A = [2, 8, 1, 4, 16],A = [1, 2, 4, 8, 16]

def solv(A):
    A.sort() # 昇順ソート
    N = len(A)

    a, b = A[0], A[1]

    g = math.gcd(abs(a), abs(b))
    r_num = (b // g)
    r_den = (a // g)
    # 比率が正しいかチェック
    for i in range(1, N - 1):
        a, b = A[i], A[i + 1]

        g = math.gcd(abs(a), abs(b))
        num = b // g
        den = a // g

        if num * r_den != den * r_num:
            return False
    return True

data = input().split()
i = 0
T = int(data[i])
i += 1

results = []

for testcase in range(T):
    N = int(data[i])
    i += 1
    A = list(map(int, data[i:i+N]))
    i += N

    if N == 2:
        results.append("Yes")
    else:
        results.append("Yes" if solv(A) else "No")

print("\n".join(results))