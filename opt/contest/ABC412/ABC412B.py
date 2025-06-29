# 例
# S = AtCoder
# T = Total
# A[t]Coder
# tがTの中に含まれているかどうかをチェック（大文字小文字は区別する）

# aBCdE
# abcdcba
# a[B]CdE
# Tの中に[B]はないのでNoを出力

# abcde
# XYZ
# Sに大文字がないのでYesと出力

# 入力の受け取り
S = input()
T = input()

flg = True
for i in range(1, len(S)):
    if S[i].isupper():
        if S[i-1] not in T:
            flg = False

if flg:
    print("Yes")
else:
    print("No")