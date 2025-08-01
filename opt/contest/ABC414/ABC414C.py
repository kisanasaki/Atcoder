A = int(input())  # 2 <= A <= 9
N = int(input())  # 1 <= N <= 10**12

# 高速な 10 → A 進数変換
def to_base_n(num: int, base: int) -> str:
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return ''.join(reversed(digits))

# 回文判定
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# 10進数の回文数を生成（先頭0は除外済）
def generate_palindromes(max_num: int):
    max_length = len(str(max_num))
    for digits in range(1, max_length + 1):
        half = (digits + 1) // 2
        start = 10**(half - 1)  # 先頭0を除外
        end = 10**half
        for left_half in range(start, end):
            left_str = str(left_half)
            if digits % 2 == 0:
                pal_str = left_str + left_str[::-1]
            else:
                pal_str = left_str + left_str[-2::-1]
            pal_num = int(pal_str)
            if pal_num > max_num:
                return
            yield pal_num

# 総和の計算
total = 0
for pal in generate_palindromes(N):
    a_base = to_base_n(pal, A)
    if is_palindrome(a_base):
        total += pal

print(total)
