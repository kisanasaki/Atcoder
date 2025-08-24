import sys
input = sys.stdin.readline

N = int(input())
R_min = C_min = 10**9
R_max = C_max = 0

for _ in range(N):
    R, C = map(int, input().split())
    R_min = min(R_min, R)
    R_max = max(R_max, R)
    C_min = min(C_min, C)
    C_max = max(C_max, C)

# 最小集結時刻
t_min = max((R_max - R_min + 1)//2, (C_max - C_min + 1)//2)
print(t_min)
