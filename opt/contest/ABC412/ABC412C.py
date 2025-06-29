import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
answers = []

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))

    # 各ドミノを1〜Nの順番で並べる前提で右隣りだけを見て構築
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        if S[i + 1] <= 2 * S[i]:
            graph[i].append(i + 1)

    # BFSで最短経路（最小並べ個数）を探す
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

    answers.append(str(dist[N - 1]))

# 出力を最後にまとめて表示
print("\n".join(answers))
