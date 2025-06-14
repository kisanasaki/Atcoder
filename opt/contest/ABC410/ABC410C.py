N, Q = map(int, input().split())  # N:数列の長さ, Q:クエリ数
Query = []

# QueryをQ行分取得し、Query1, Query2, Query3に分ける
for _ in range(Q):
    row = input().split()
    Query1 = int(row[0])
    Query2 = int(row[1])
    Query3 = int(row[2]) if len(row) == 3 else None
    Query.append((Query1, Query2, Query3))  # タプルで保存

A = list(range(1, N + 1))  # 長さNの配列A

shift = 0  # 回転による先頭ズレ管理

for i in range(Q):
    t, p, x = Query[i]

    if t == 1:
        idx = (shift + p - 1) % N
        A[idx] = x

    elif t == 2:
        idx = (shift + p - 1) % N
        print(A[idx])

    else:  # t == 3
        # 先頭を末尾に回す操作を k 回繰り返す
        k = p  # Query2にkが入っている
        shift = (shift + k) % N
