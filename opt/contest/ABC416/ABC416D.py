import bisect

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split()) # N:配列の長さ,M:割る数
    A = list(map(int, input().split())) # A:非負整数列
    B = list(map(int, input().split())) # B:非負整数列

    A_mod = sorted([a % M for a in A])
    B_mod = [b % M for b in B]

    total = 0
    for b in B_mod:
        target = (M - b) % M
        idx = bisect.bisect_left(A_mod, target)
        if idx == len(A_mod):
            chosen = A_mod.pop(0)
        else:
            chosen = A_mod.pop(idx)
        total += (chosen + b) % M

    results.append(total)

# 出力
for res in results:
    print(res)