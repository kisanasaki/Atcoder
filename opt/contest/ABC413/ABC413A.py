N,M = map(int, input().split()) # N=品物の数,M=鞄の大きさ
A = list(map(int, input().split())) # それぞれの品物の重さ

# すべての品物の大きさの合計がカバンの大きさ以下かどうか
if sum(A) <= M:
    print("Yes")
else:
    print("No")