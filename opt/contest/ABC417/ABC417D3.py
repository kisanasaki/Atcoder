N = int(input())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

Q = int(input())
queries = [int(input()) for _ in range(Q)]

MAX_P = 500

dp = [i for i in range(MAX_P + 1)]

for P, A, B in reversed(gifts):
    new_dp = [0] * (MAX_P + 1)
    for t in range(MAX_P + 1):
        if t <= P:
            nt = t + A
        else:
            nt = max(0, t - B)
        if nt > MAX_P:
            nt = MAX_P
        new_dp[t] = dp[nt]
    dp = new_dp

for x in queries:
    if x <= MAX_P:
        print(dp[x])
    else:
        tension = x
        for P, A, B in gifts:
            if tension <= P:
                tension += A
            else:
                tension = max(0, tension - B)
        print(tension)
