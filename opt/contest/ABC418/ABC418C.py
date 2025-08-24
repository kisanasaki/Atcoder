N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort

B = [(int(input()), i) for i in range(Q)]

B.sort()

print(B)

# def solve(A, b):
#     # Aをb以上とb未満に分割する
#     above_b = []
#     below_b = []
#     for a in A:
#         if a >= b:
#             above_b.append(a)
#         else:
#             below_b.append(a)
#     return above_b, below_b

answers = [0] * Q
above_b = []
below_b = []
for b, pre_idx in range(Q):
    # Aをb以上とb未満に分割する
    if b >= a
    above_b.append
    min_x = (b-1)*len(above_b) + sum(below_b)+1
    if min_x > sum(A):
        min_x = -1
    answers.append(min_x)

for ans in answers:
    print(ans)