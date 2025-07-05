N = int(input())
mojiretu = []

# 入力
for _ in range(N):
    S = input().strip()
    mojiretu.append(S)

results = set() # 重複した文字が入らないようにsetで定義

# すべての異なる (i, j) の組を試す
for i in range(N):
    for j in range(N):
        if i != j:
            renketu = mojiretu[i] + mojiretu[j]
            results.add(renketu)

print(len(results))