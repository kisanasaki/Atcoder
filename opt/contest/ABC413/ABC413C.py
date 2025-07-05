

Q = int(input())  # クエリ数
Query = []
A = []

# クエリの取得
# QueryをQ行分取得し、Query1, Query2, Query3に分ける
# Query1 = type種別
# Query1+Query2+Query3=type1
# Query2 = c
# Query3 = x
# Query1+Query2=type2
# Query2 = k
for _ in range(Q):
    row = input().split()
    Query1 = int(row[0])
    Query2 = int(row[1])
    Query3 = int(row[2]) if len(row) == 3 else None
    Query.append((Query1, Query2, Query3))  # タプルで保存

# クエリの処理
for q in Query:
    # type1の場合
    if q[0] == 1:
        c = q[1]
        x = q[2]
        for _ in range(c):
            A.append(x)  # x を c 回追加
    # type2の場合
    elif q[0] == 2:
        k = q[1]
        total = sum(A[:k])  # 先頭 k 個の合計
        print(total)
        A = A[k:]  # 先頭 k 個を削除