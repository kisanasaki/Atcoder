import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()

def II():
    return int(input())

def LII():
    return list(map(int, input().split()))

T = II()
results = []

for _ in range(T):
    N, M = LII()
    A = LII()
    B = LII()

    A_mod = sorted([a % M for a in A])
    B_mod = sorted([b % M for b in B])

    mod_overflow_count = 0  # M 以上になる組み合わせの数
    B_index = 0

    for a in reversed(A_mod):  # A を大きい順に
        target = M - a  # M を超えないために欲しい B の下限

        # B_mod の中から「target 以上」の最初の位置を探す（i以降）
        j = bisect_left(B_mod, target, B_index)

        if j < N:
            mod_overflow_count += 1  # M 以上になる
        B_index = j + 1  # 次はこの位置以降を見る（ペアに使ったとみなす）

    total_sum = sum(A_mod) + sum(B_mod) - mod_overflow_count * M
    results.append(total_sum)

# 出力
for res in results:
    print(res)
