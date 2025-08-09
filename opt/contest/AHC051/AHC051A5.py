import os

# --- 処理ロジック本体（元の単純な仕様ベース） ---
def process_instance(N, M, K, processor_positions, sorter_positions, prob):
    # ごみ種0〜N-1に処理装置を固定割当
    proc_assign = ' '.join(str(i) for i in range(N))

    # inlet → sorter（最も近いもの）
    inlet = (0, 5000)
    dist_sq = [((x - inlet[0])**2 + (y - inlet[1])**2, i) for i, (x, y) in enumerate(sorter_positions)]
    _, nearest_i = min(dist_sq)
    inlet_conn = N + nearest_i  # ノード番号はN以降がsorter

    # sorter の割当（確率最大→出口1, 最小→出口2）
    sorter_assigns = []
    for i in range(M):
        if i >= K:
            sorter_assigns.append("-1")
            continue
        first_row = prob[i]
        imax = first_row.index(max(first_row))
        imin = first_row.index(min(first_row))
        if i == nearest_i:
            sorter_assigns.append(f"0 {imax} {imin}")
        else:
            sorter_assigns.append("-1")

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
    BATCH_MODE = False  # ← False にすると標準入力に切り替え可能

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
