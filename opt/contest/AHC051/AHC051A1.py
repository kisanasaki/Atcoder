import sys
from collections import defaultdict

sys.setrecursionlimit(10000)
input = sys.stdin.readline

# --- 入力読み込み ---
N, M, K = map(int, input().split())
processor_positions = [tuple(map(int, input().split())) for _ in range(N)]
sorter_positions = [tuple(map(int, input().split())) for _ in range(M)]
prob = [list(map(float, input().split())) for _ in range(K)]

# --- 線分交差チェック ---
def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def orientation(a, b, c):
    cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return sign(cross)

def segments_intersect(p1, p2, q1, q2):
    if (max(p1[0], p2[0]) < min(q1[0], q2[0]) or
        max(q1[0], q2[0]) < min(p1[0], p2[0]) or
        max(p1[1], p2[1]) < min(q1[1], q2[1]) or
        max(q1[1], q2[1]) < min(p1[1], p2[1])):
        return False
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)
    return (o1 * o2 <= 0) and (o3 * o4 <= 0)

# --- 閉路判定 ---
def has_cycle(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[node] = False
    return False

# --- ID割り当て ---
# 0: inlet, 1〜N: processors, N+1〜N+M: sorters
inlet = (0, 5000)
nodes = [inlet] + processor_positions + sorter_positions
total_nodes = 1 + N + M

# --- 出力情報構築 ---
proc_assign = ' '.join(str(i) for i in range(N))  # 各処理装置に対応するごみ種（固定）

# inlet から最も近い分別器を選ぶ
dist = [((x - inlet[0])**2 + (y - inlet[1])**2, i) for i, (x, y) in enumerate(sorter_positions)]
_, nearest_sorter_idx = min(dist)
inlet_conn = N + 1 + nearest_sorter_idx  # global node ID（+1: inlet, +N: offset）

# 分別器の設置：確率の高い/低いごみ種に対応
sorter_assigns = []
for i in range(M):
    if i < K:
        p = prob[i]
        imax = p.index(max(p))
        imin = p.index(min(p))
        sorter_assigns.append(f"{i} {imax} {imin}")
    else:
        sorter_assigns.append("-1")

# --- ベルト接続（衝突・閉路チェック） ---
edges = []
graph = defaultdict(list)

# inlet -> sorter
edges.append((0, inlet_conn))
graph[0].append(inlet_conn)

# sorter -> processor
used_sorter_id = inlet_conn - (N + 1)
row = prob[used_sorter_id]
imax = row.index(max(row))
imin = row.index(min(row))

to_sorter = inlet_conn
out1 = 1 + imax
out2 = 1 + imin

# 線分交差＆DAGチェック
def can_add_edge(a, b):
    for u, v in edges:
        if segments_intersect(nodes[a], nodes[b], nodes[u], nodes[v]):
            return False
    graph[a].append(b)
    if has_cycle(graph, a, [False]*total_nodes, [False]*total_nodes):
        graph[a].pop()
        return False
    return True

if can_add_edge(to_sorter, out1):
    edges.append((to_sorter, out1))
if out2 != out1 and can_add_edge(to_sorter, out2):
    edges.append((to_sorter, out2))

# --- 出力 ---
print(proc_assign)
print(inlet_conn)
print("\n".join(sorter_assigns))
