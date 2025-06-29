N=int(input()) 
A = []
B = []

for _ in range(N):
    a,b= map(int, input().split())
    A.append(a)
    B.append(b)

count = 0
for i in range(N):
    if B[i] > A[i]:
        count += 1
print(count)