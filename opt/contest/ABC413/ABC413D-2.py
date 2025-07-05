import sys

def can_form_geometric(A, r):
    
    # 公比 r で数列 A から並べ替えて等比数列を作れるか判定する関数。
    # - A: 元の整数列
    # - r: 公比（実数）
    # 戻り値: 作れれば True、作れなければ False
    
    used = [False] * len(A)  # Aの各要素が既に使われたかを記録
    # 絶対値で昇順ソート（比率判定に使う）
    A_sorted = sorted(A, key=lambda x: abs(x))
    sequence = []

    # 最初の値は絶対値最小のものからスタート
    current = A_sorted[0]
    sequence.append(current)
    used[0] = True

    # 公比 r に従って次の値を決め、A内で探索
    for _ in range(len(A) - 1):
        next_val = current * r  # 次の項の値
        found = False
        # A_sortedから未使用で値が next_val に近いものを探す
        for i, val in enumerate(A_sorted):
            if not used[i] and abs(val - next_val) < 1e-9:
                sequence.append(val)
                used[i] = True
                current = val
                found = True
                break
        # 次の項が見つからなければ等比数列は作れない
        if not found:
            return False
    # すべての項が見つかったら成功
    return True

def solve(A):

    # 数列 A で、並べ替えにより等比数列を作れるか判定する関数。

    N = len(A)
    # 長さ2なら必ず等比数列になる
    if N == 2:
        return True

    # 候補となる公比を格納する集合
    candidates = set()

    # 絶対値で昇順ソート
    A_sorted = sorted(A, key=lambda x: abs(x))
    # 昇順の隣接要素の比を候補として収集
    for i in range(N - 1):
        if A_sorted[i] != 0:
            candidates.add(A_sorted[i+1] / A_sorted[i])

    # 昇順候補で等比数列が作れるか試す
    for r in candidates:
        if can_form_geometric(A, r):
            return True

    # 降順パターンでも同様に候補を収集して試す
    A_sorted_rev = A_sorted[::-1]
    candidates = set()
    for i in range(N - 1):
        if A_sorted_rev[i] != 0:
            candidates.add(A_sorted_rev[i+1] / A_sorted_rev[i])

    for r in candidates:
        if can_form_geometric(A, r):
            return True

    # どの公比でも作れなければFalse
    return False

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        # 判定結果を結果リストに追加
        results.append("Yes" if solve(A) else "No")
    # まとめて出力
    print("\n".join(results))

if __name__ == "__main__":
    main()
