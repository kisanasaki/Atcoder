from collections import deque

T = int(input()) # ケース数
answers = []  # 答えを貯めるリスト

for _ in range(T):
    N = int(input()) # ドミノ数
    S = list(map(int, input().split())) # ドミノの大きさ

    # 倒せるドミノのグラフを作る
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and S[j] <= 2 * S[i]: # 条件
                graph[i].append(j)

    # 幅優先探索（BFS）で最短個数を探す
    dist = [-1] * N
    dist[0] = 1
    queue = deque([0])

    while queue:
        u = queue.popleft()
        if u == N - 1:
            break
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    # 答えをリストに追加
    answers.append(str(dist[N - 1]))

# 最後にまとめて出力
print("\n".join(answers))
