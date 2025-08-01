N = int(input())  # N: 圧縮データの組数
C = []  # C: 各文字
L = []  # L: 各文字の繰り返し回数
S = ""  # S: 復元された文字列
length = 0  # length: 現在の文字列の長さ

for _ in range(N):
    c_in, l_in = input().split()
    C.append(c_in)
    L.append(int(l_in))

for i in range(N):
    length += L[i]
    if length > 100:
        print("Too Long")
        exit()
    S += C[i] * L[i]

print(S)