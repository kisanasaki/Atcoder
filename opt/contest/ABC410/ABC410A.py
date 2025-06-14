# 変数
N=int(input()) # レース数
A=list(map(int, input().split())) # 出場レースごとの馬年齢制限
K=int(input()) # 馬年齢
count = 0

# 処理
for i in range(N):
    if K <= A[i]: 
      count = count + 1
print(count)

