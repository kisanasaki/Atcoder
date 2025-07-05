# ABC410類題?
from collections import deque

Q = int(input())  # クエリ数
Query = []
# 
A = deque()

# クエリの取得
for _ in range(Q):
    row = input().split()
    Query1 = int(row[0])
    Query2 = int(row[1])
    Query3 = int(row[2]) if len(row) == 3 else None
    Query.append((Query1, Query2, Query3))  # タプルで保存

# クエリの処理
for q in Query:
    if q[0] == 1:
        # タイプ1: 値xをc個末尾に追加
        c = q[1]
        x = q[2]
        A.append((x, c))
    elif q[0] == 2:
        # タイプ2: 先頭からk個削除し、その合計を出力
        k = q[1]
        total = 0
        while k > 0:
            val, count = A[0]
            if count <= k:
                total += val * count
                k -= count
                A.popleft()
            else:
                total += val * k
                A[0] = (val, count - k)
                k = 0
        print(total)