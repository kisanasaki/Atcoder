N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

# 隣接家間の距離
gaps = [(X[i+1] - X[i], i) for i in range(N-1)]

# 大きい順にソート
gaps.sort(key=lambda x: x[0], reverse=True)

# M-1 個の最大隙間のインデックスを取得して昇順に
cut_indices = sorted([idx for (_, idx) in gaps[:M-1]])

# 区間の開始位置リスト
starts = [0] + [idx + 1 for idx in cut_indices] + [N]

total_power = 0
for i in range(M):
    left = X[starts[i]]
    right = X[starts[i+1]-1]
    length = right - left  # 区間長 = 電波強度
    total_power += length

print(total_power)
