import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
total_sum = sum(A)
max_a = max(A) if A else 0

# 配列長は max_a+2 以上（max_a+1 まで参照するため）
count_ge = [0] * (max_a + 3)
sum_lt = [0] * (max_a + 3)

# 差分で準備
for a in A:
    count_ge[1] += 1
    count_ge[a + 1] -= 1
    sum_lt[a + 1] += a

# 累積和（1..max_a+1 まで作る）
for b in range(1, max_a + 2):
    count_ge[b] += count_ge[b - 1]
    sum_lt[b] += sum_lt[b - 1]

# クエリ処理
for _ in range(Q):
    b = int(input())
    # b が配列で用意した範囲を超える（つまり b > max_a+1）のときは
    # 「すべて a_i < b」となる -> sum(below) = total_sum
    if b > max_a + 1:
        min_x = total_sum + 1
    else:
        # 1 <= b <= max_a+1 のとき sum_lt[b] は "a_i < b の合計" を表す
        min_x = (b - 1) * count_ge[b] + sum_lt[b] + 1

    if min_x > total_sum:
        print(-1)
    else:
        print(min_x)
