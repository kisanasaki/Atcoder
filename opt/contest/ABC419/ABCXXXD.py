# 入力
N, M = map(int, input().split())
S = list(input())
T = list(input())

L_list = []
R_list = []

for _ in range(M):
    L, R = map(int, input().split())
    L_list.append(L)
    R_list.append(R)

for i in range(M):
    L = L_list[i] - 1
    R = R_list[i]
    S[L:R], T[L:R] = T[L:R], S[L:R]

print("".join(S))
