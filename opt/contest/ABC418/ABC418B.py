S = input()

n = len(S)

def count_t(part_str):
    count = 0
    for i in part_str:
        if i == "t":
            count += 1
    return count

max_fill_rate = 0
for i in range(n-1):
    for j in range(i+1, n+1):
        part_str = S[i:j]
        # tから始まってtで終わるかどうか
        part_str_length = len(part_str)
        if part_str[0] == "t" and part_str[-1] == "t" and part_str_length >= 3:
            t_count = count_t(part_str)
            fill_rate = (t_count - 2) / (part_str_length - 2)
            max_fill_rate = max(max_fill_rate, fill_rate)

print(max_fill_rate)