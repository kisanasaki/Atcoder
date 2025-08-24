
import sys
import heapq

input = sys.stdin.readline

Q = int(input())

hq = []
for _ in range(Q):
    query = input().split()
    # クエリが「1 x」の場合 → x を袋に追加
    if query[0] == "1":
        x = int(query[1])
        heapq.heappush(hq, x)
    # クエリが「2」の場合 → 最小値を取り出して出力
    else:  # "2"
        print(heapq.heappop(hq))