# そのままだとO(NQ)
# プレゼント 価値P,テンション上げ度A,テンション下げ度B
# テンション初期値Xi N個のプレゼント

# 例1
# プレゼント4個
# 4
# 3 1 4
# 1 5 9
# 2 6 5
# 3 5 8

# 質問11個
# 11
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


N = int(input())
gifts = []
for _ in range(N):
    P, A, B = map(int, input().split())
    gifts.append((P, A, B))

Q = int(input())
queries = [int(input()) for _ in range(Q)]
# x:テンション初期値
for x in queries:
    tension = x
    for P, A, B in gifts:
        #テンション <= 価値Pの場合、テンションがAだけ増加する。
        if tension <= P:
            tension += A
        #テンション > 価値Pの場合、テンションがBだけ減少する。
        #ただし、テンション < Bの場合、テンションは0になる。
        else:
            tension = max(0, tension - B)
    print(tension)