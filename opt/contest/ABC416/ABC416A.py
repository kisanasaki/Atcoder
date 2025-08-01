# 入力
N, L, R = map(int, input().split())
S = input().strip()

# L〜R（1-indexed）
target = S[L-1:R]

# 判定
if all(c == 'o' for c in target):
    print("Yes")
else:
    print("No")