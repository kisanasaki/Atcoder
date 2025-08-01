H, W = map(int, input().split()) # H->縦,W->横
A = [input() for _ in range(H)] # A->map1
B = [input() for _ in range(H)] # B->map2

def shift(A,s,t):
    # 縦にs回シフト -> 下にずらす
    shifted = [A[(i - s) % H] for i in range(H)]
    # 横にt回シフト -> 右にずらす
    shifted = [''.join(row[(j - t) % W] for j in range(W)) for row in shifted]
    return shifted

found = False
for s in range(H):
    for t in range(W):
        if shift(A, s, t) == B:
            found = True
            break
    if found:
        break

print("Yes" if found else "No")