import os
from collections import defaultdict

# --- 線分交差 & 閉路チェック 関数 ---
def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
def orientation(a, b, c):
    cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return sign(cross)

def segments_intersect(p1, p2, q1, q2):
    if (max(p1[0], p2[0]) < min(q1[0], q2[0]) or
        max(q1[0], q2[0]) < min(p1[0], p2[0]) or
        max(p1[1], p2[1]) < min(q1[1], q2[1]) or
        max(q1[1], q2[1]) < min(p1[1], p2[1])):
        return False
    o1, o2 = orientation(p1, p2, q1), orientation(p1, p2, q2)
    o3, o4 = orientation(q1, q2, p1), orientation(q1, q2, p2)
    return (o1 * o2 <= 0) and (o3 * o4 <= 0)

def has_cycle(graph, node, visited, rec_stack):
    visited[node], rec_stack[node] = True, True
    for neighbor in graph[node]:
        if not visited[neighbor] and has_cycle(graph, neighbor, visited, rec_stack):
            return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[node] = False
    return False

# --- 処理ロジック本体 ---
def process_instance(N, M, K, processor_positions, sorter_positions, prob):
    inlet = (0, 5000)
    nodes = [inlet] + processor_positions + sorter_positions
    total_nodes = 1 + N + M

    edges = []
    graph = defaultdict(list)

    def can_add_edge(a, b):
        for u, v in edges:
            if segments_intersect(nodes[a], nodes[b], nodes[u], nodes[v]):
                return False
        graph[a].append(b)
        if has_cycle(graph, a, [False]*total_nodes, [False]*total_nodes):
            graph[a].pop()
            return False
        return True

    # ごみ種0〜N-1に処理装置を固定割当
    proc_assign = ' '.join(str(i) for i in range(N))

    # inlet → sorter（交差なしの最も近いもの）
    dist = [((x - inlet[0])**2 + (y - inlet[1])**2, i) for i, (x, y) in enumerate(sorter_positions)]
    sorted_dists = sorted(dist)
    inlet_conn = -1
    for _, idx in sorted_dists:
        candidate = N + 1 + idx
        if can_add_edge(0, candidate):
            edges.append((0, candidate))
            inlet_conn = candidate
            break

    if inlet_conn == -1:
        raise Exception("No valid inlet connection found")

    # sorter の割当と接続（最大・最小確率の2系統）
    sorter_assigns = []
    for i in range(M):
        if i >= K:
            sorter_assigns.append("-1")
            continue
        p = prob[i]
        imax, imin = p.index(max(p)), p.index(min(p))
        sorter_assigns.append(f"{i} {imax} {imin}")

        from_node = N + 1 + i
        out1, out2 = 1 + imax, 1 + imin
        for to_node in [out1, out2]:
            if can_add_edge(from_node, to_node):
                edges.append((from_node, to_node))

    return proc_assign, inlet_conn, sorter_assigns

# --- バッチまたは標準入力で実行 ---
def process_single_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    N, M, K = map(int, lines[0].split())
    processor_positions = [tuple(map(int, lines[i+1].split())) for i in range(N)]
    sorter_positions = [tuple(map(int, lines[N+1+i].split())) for i in range(M)]
    prob = [list(map(float, lines[N+1+M+i].split())) for i in range(K)]

    proc_assign, inlet_conn, sorter_assigns = process_instance(N, M, K, processor_positions, sorter_positions, prob)

    with open(output_path, 'w') as f:
        f.write(proc_assign + '\n')
        f.write(str(inlet_conn) + '\n')
        f.write('\n'.join(sorter_assigns) + '\n')

def main():
    BATCH_MODE = True  # ← True で input/output フォルダ使う

    if BATCH_MODE:
        input_dir = "input"
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        for i in range(100):  # 0000.txt 〜 0099.txt
            name = f"{i:04}.txt"
            input_path = os.path.join(input_dir, name)
            output_path = os.path.join(output_dir, name)

            if not os.path.exists(input_path):
                print(f"⚠️ input/{name} が見つかりません")
                continue

            try:
                process_single_file(input_path, output_path)
                print(f"✅ 出力完了: {output_path}")
            except Exception as e:
                print(f"❌ エラー {name}: {e}")
    else:
        import sys
        input = sys.stdin.readline

        N, M, K = map(int, input().split())
        processor_positions = [tuple(map(int, input().split())) for _ in range(N)]
        sorter_positions = [tuple(map(int, input().split())) for _ in range(M)]
        prob = [list(map(float, input().split())) for _ in range(K)]

        proc_assign, inlet_conn, sorter_assigns = process_instance(N, M, K, processor_positions, sorter_positions, prob)

        print(proc_assign)
        print(inlet_conn)
        print("\n".join(sorter_assigns))

if __name__ == "__main__":
    main()
