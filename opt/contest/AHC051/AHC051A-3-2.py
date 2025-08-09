
import os
import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

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

# --- 閉路検出 ---
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

# --- グリッド構築と近傍取得 ---
def build_grid(nodes, grid_size=1000):
    grid = defaultdict(list)
    for idx, (x, y) in enumerate(nodes):
        gx, gy = x // grid_size, y // grid_size
        grid[(gx, gy)].append(idx)
    return grid

def get_nearby_nodes(idx, nodes, grid, grid_size=1000):
    x, y = nodes[idx]
    gx, gy = x // grid_size, y // grid_size
    nearby = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            cell = (gx + dx, gy + dy)
            nearby.extend(grid.get(cell, []))
    return [n for n in nearby if n != idx]

# --- 処理ロジック本体 ---
def process_case(case_input: str) -> str:
    lines = case_input.strip().splitlines()
    N, M, K = map(int, lines[0].split())
    ptr = 1
    processor_positions = [tuple(map(int, lines[ptr + i].split())) for i in range(N)]
    ptr += N
    sorter_positions = [tuple(map(int, lines[ptr + i].split())) for i in range(M)]
    ptr += M
    prob = [list(map(float, lines[ptr + i].split())) for i in range(K)]

    inlet = (0, 5000)
    nodes = [inlet] + processor_positions + sorter_positions
    total_nodes = 1 + N + M
    edges = []
    graph = defaultdict(list)
    grid = build_grid(nodes)

    def can_add_edge(a, b):
        for u, v in edges:
            if segments_intersect(nodes[a], nodes[b], nodes[u], nodes[v]):
                return False
        graph[a].append(b)
        if has_cycle(graph, a, [False] * total_nodes, [False] * total_nodes):
            graph[a].pop()
            return False
        return True

    proc_assign = ' '.join(str(i) for i in range(N))
    dists = [((x - inlet[0])**2 + (y - inlet[1])**2, i) for i, (x, y) in enumerate(sorter_positions)]
    _, nearest_sorter_idx = min(dists)
    inlet_conn = N + 1 + nearest_sorter_idx
    edges.append((0, inlet_conn))
    graph[0].append(inlet_conn)

    sorter_assigns = []
    for i in range(M):
        if i < K:
            p = prob[i]
            imax = p.index(max(p))
            imin = p.index(min(p))
            sorter_assigns.append(f"{i} {imax} {imin}")
        else:
            sorter_assigns.append("-1")

    for i in range(M):
        from_node = N + 1 + i
        if i >= K:
            continue
        p = prob[i]
        imax = p.index(max(p))
        imin = p.index(min(p))
        out1 = 1 + imax
        out2 = 1 + imin
        targets = [out1, out2]
        nearby = get_nearby_nodes(from_node, nodes, grid)
        processor_nearby = [n for n in nearby if 1 <= n <= N]
        for t in targets:
            if t not in processor_nearby:
                processor_nearby.append(t)
        for to_node in processor_nearby:
            if can_add_edge(from_node, to_node):
                edges.append((from_node, to_node))

    result = []
    result.append(proc_assign)
    result.append(str(inlet_conn))
    result.extend(sorter_assigns)
    return '\n'.join(result)

# =============================
# バッチ処理（ファイル） or 標準入力
# =============================
def main():
    BATCH_MODE = True  # ← False にすると標準入力から読み取る

    if BATCH_MODE:
        input_dir = 'input'
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        for i in range(100):
            fname = f"{i:04}.txt"
            input_path = os.path.join(input_dir, fname)
            output_path = os.path.join(output_dir, fname)

            with open(input_path, 'r') as fin:
                case_input = fin.read()
            result = process_case(case_input)
            with open(output_path, 'w') as fout:
                fout.write(result + '\n')

    else:
        # --- 標準入力から読み取りたい場合はこちらを有効化 ---
        # 標準入力は複数行が来る前提で、EOFまで読み取る
        import sys
        case_input = sys.stdin.read()
        result = process_case(case_input)
        print(result)

if __name__ == "__main__":
    main()
