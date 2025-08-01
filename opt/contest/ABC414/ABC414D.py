import math
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()

    # 家の隙間の長さを計算
    gaps = []
    for i in range(N - 1):
        gaps.append(X[i+1] - X[i])

    # 隙間を降順に並べて大きい順にM-1個カットすることで区間を分割
    gaps.sort(reverse=True)

    # カットする隙間はM-1個なので、それ以外の隙間の合計が区間長の合計になる
    # 区間の長さの合計は (X[-1] - X[0]) の範囲に分割されている
    # 大きい隙間をカットすることで区間が短くなり電波強度が下がる

    # カットしない隙間の合計 = 総距離 - 大きいM-1個の隙間の合計
    total_range = X[-1] - X[0]
    if M == 1:
        # 1区間なら全体をカバー
        max_interval = total_range
        intervals = [max_interval]
    else:
        cut_sum = sum(gaps[:M-1])  # 大きい隙間M-1個
        remain_sum = total_range - cut_sum

        # 区間はM個できる
        # 区間長を決めるには、cutしなかった隙間で区間の長さを計算
        # ただし、区間長は隙間の位置により決まるため、
        # 大きい隙間をカットすると区間長が短くなる

        # 区間の長さは隙間を切った結果で計算したいので、
        # ここでは各区間の長さを取得するために隙間を使った実装が必要
        # ただし問題文は「基地局は任意の実数座標に置ける」ため、
        # 区間長は単純に各区間の「右端 - 左端」で計算可能

        # ここは区間長を計算するために実際の切り方を行う必要がある
        # 大きい隙間M-1個で区切る → その区間の区間長を計算する

        # 具体的には、M-1個の大きい隙間のインデックスを記録して
        # それで家配列を分割し、区間長を計算

        cut_gaps = gaps[:M-1]
        # 大きい隙間の位置を元に戻すために、隙間の情報（長さ, index）で管理
        gap_info = []
        for i in range(N - 1):
            gap_info.append((X[i+1] - X[i], i))
        gap_info.sort(key=lambda x: x[0], reverse=True)

        cut_indices = sorted([idx for (_, idx) in gap_info[:M-1]])

        intervals = []
        start = 0
        for idx in cut_indices:
            end = idx
            interval_len = X[end] - X[start]
            intervals.append(interval_len)
            start = end + 1
        # 最後の区間
        intervals.append(X[-1] - X[start])

    # 各区間の電波強度を計算し合計する
    total_power = 0
    for length in intervals:
        if length == 0:
            power = 0
        else:
            # 電波強度xは距離 <= 2^x * 2 = 2^(x+1)
            # length <= 2^(x+1) を満たす最小のxを求める
            power = math.ceil(math.log2(length)) if length > 0 else 0
            # ただし電波の届く距離は 2^x で、その範囲が左右に伸びるので距離は2^(x+1)
            # なので length <= 2^(x+1) -> x >= log2(length) - 1
            power = max(power - 1, 0)  # power-1 で調整
        total_power += power

    print(total_power)

if __name__ == "__main__":
    main()
