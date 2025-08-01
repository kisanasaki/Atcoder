A = int(input())
N = int(input())

def is_palindrome_str(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def base_n_to_decimal(digits: list[int], base: int) -> int:
    res = 0
    for d in digits:
        res = res * base + d
    return res

def generate_a_base_palindromes(base: int, max_decimal: int):
    max_len = len(to_base_n(max_decimal, base))  # A進法での桁数上限

    for length in range(1, max_len + 1):
        half_len = (length + 1) // 2

        def dfs(pos: int, path: list[int]):
            if pos == half_len:
                if length % 2 == 0:
                    full = path + path[::-1]
                else:
                    full = path + path[-2::-1]
                if full[0] == 0:  # 先頭0スキップ
                    return
                dec = base_n_to_decimal(full, base)
                if dec <= N:
                    yield dec
                return

            for d in range(base):
                path.append(d)
                yield from dfs(pos + 1, path)
                path.pop()

        yield from dfs(0, [])

# 十進法→A進法変換（桁数上限のために使用）
def to_base_n(num: int, base: int) -> str:
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return ''.join(digits[::-1])

# main
total = 0
seen = set()

for dec in generate_a_base_palindromes(A, N):
    if dec in seen:  # 重複回避
        continue
    seen.add(dec)
    if is_palindrome_str(dec):
        total += dec

print(total)
