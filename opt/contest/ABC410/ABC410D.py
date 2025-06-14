# 入力の受け取り
N,Q=map(int,input().split())
A=list(map(int,input().split()))

# Aをソート
A.sort()

# クエリの記録
query=[]

# Q回
for i in range(Q):
    # 入力の受け取り
    x=int(input())
    # [x,i番目のクエリ]と記録
    query.append([x,i])