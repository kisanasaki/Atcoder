# 条件
# 1.文字数は同じ
# 2.T「.」、「#」、「o」で構成される
# 3.#の位置は同じ
# 4.oの間に#が最低1つ必要→oを複数置くときは、必ず#を挟む。

# 入力
S = input().strip()
N = len(S)
T = list(S) 

i = 0
while i < N:
    # 条件3
    if S[i] == '#':
        T[i] = '#'
        i += 1
    else:
        start = i
        while i < N and S[i] == '.':
            i += 1
        # 条件4
        T[start] = 'o'
        for j in range(start + 1, i):
            T[j] = '.'

# 出力
print("".join(T))
