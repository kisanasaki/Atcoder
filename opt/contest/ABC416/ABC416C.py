# S1,...,SN を辞書順にソート
# 長さ K の重複あり順列 N^K 通りを辞書順で生成
# X番目取得
from itertools import product

# 入力
N, K, X = map(int, input().split()) # N:文字列の個数,K:連結する数,X:出力する番号
S = [input().strip() for _ in range(N)] # S:文字列

# 辞書順にソート
S.sort()

all_strings = []
# 長さ K の重複あり順列 N^K 通り
for indices in product(range(N), repeat=K):
    s = ''.join(S[i] for i in indices)
    all_strings.append(s)

# ←ソート
all_strings.sort()
# X番目取得
print(all_strings[X-1])