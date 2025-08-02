from collections import Counter

M,N = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

b_count = Counter(B)

# 結果
result = []

# A から B の要素を順に削除
for a in A:
    if b_count[a] > 0:
        b_count[a] -= 1
    else:
        result.append(a)

# 出力
print(' '.join(map(str, result)))