import sys
import bisect

input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())  # N: 配列の長さ, M: 割る数
    A = list(map(int, input().split()))  # A: 非負整数列
    B = list(map(int, input().split()))  # B: 非負整数列

    A_mod = sorted([a % M for a in A])  # A の各要素を M で割った余りでソート
    B_mod = [b % M for b in B]          # B の各要素も余りを計算（順序は変えない）
    used = [False] * N                  # A_mod の要素が使用済みかを管理

    total = 0
    for b in B_mod:
        target = (M - b) % M
        idx = bisect.bisect_left(A_mod, target)

        # idx 以降に未使用要素を探す
        while idx < N and used[idx]:
            idx += 1

        if idx == N:
            # 先頭から未使用の要素を探す
            idx = 0
            while used[idx]:
                idx += 1

        used[idx] = True
        total += (A_mod[idx] + b) % M

    results.append(total)

# 出力
for res in results:
    print(res)