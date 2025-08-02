import sys
input = sys.stdin.readline

N = int(input())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

Q = int(input())
queries = [int(input()) for _ in range(Q)]

MAX_TENSION = 10000

dp = [i for i in range(MAX_TENSION + 1)]

for P, A, B in gifts:
    new_dp = [0] * (MAX_TENSION + 1)
    for t in range(MAX_TENSION + 1):
        if t >= P:
            nt = t + A
            if nt > MAX_TENSION:
                nt = MAX_TENSION
        else:
            nt = t - B
            if nt < 0:
                nt = 0
        new_dp[t] = dp[nt]
    dp = new_dp

for x in queries:
    if x > MAX_TENSION:
        print(dp[MAX_TENSION])
    else:
        print(dp[x])
