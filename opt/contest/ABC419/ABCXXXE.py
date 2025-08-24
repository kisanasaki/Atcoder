N,L,M=map(int,input().split())
A=list(map(int,input().split()))
res=0
B=[0]*N
for i in range(N):
    B[i]=A[i]
for i in range(N-L+1):
    s=sum(B[i:i+L])%M
    if s!=0:
        d=M-s
        B[i+L-1]+=d
        res+=d
print(res if res!=0 else "O")