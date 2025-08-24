# 入力受け取り
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

# 差分配列を使って区間反転を管理
diff = [0] * (N + 1)  # 長さ N+1

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1  # 0-indexに
    diff[L] ^= 1        # 区間開始で反転
    diff[R] ^= 1        # 区間終了で反転を戻す

# swap_flagを計算
swap_flag = [0] * N
current = 0
for i in range(N):
    current ^= diff[i]
    swap_flag[i] = current

# 最終Sを構築
result = [T[i] if swap_flag[i] else S[i] for i in range(N)]
print("".join(result))
