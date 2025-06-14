# 変数
N,Q=map(int, input().split()) # N:箱の数,Q:ボールの数
X=list(map(int, input().split())) # 数列
box_counts = [0] * N
B = []

# 処理
for x in X:
    if x >= 1:
        # 指定された箱に入れる（1-indexed → 0-indexed）
        box_counts[x - 1] += 1
        B.append(x)
    else:
        # 最小のボール数の箱のうち、最も番号の小さいものを探す
        min_count = min(box_counts)
        min_index = box_counts.index(min_count)  # 最初に見つかった最小の箱
        box_counts[min_index] += 1
        B.append(min_index + 1)  # 0-indexed → 1-indexed に戻す

# 出力
print(*B)