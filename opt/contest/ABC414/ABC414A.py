N,L,R = map(int, input().split()) # N:リスナー数,L:配信開始時刻,R:配信終了時刻
X = [] # X:視聴開始時刻
Y = [] # Y:視聴終了時刻
count = 0
for _ in range(N):
    X_in,Y_in = map(int, input().split())
    X.append(X_in)
    Y.append(Y_in)

# L <= X < Y <= R 
for i in range(N):
    if X[i] <= L and R <= Y[i]:
        count = count + 1

print(count)