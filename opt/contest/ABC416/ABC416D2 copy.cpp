# 置換元 Python
# import bisect

# T = int(input())
# results = []

# for _ in range(T):
#     N, M = map(int, input().split()) # N:配列の長さ,M:割る数
#     A = list(map(int, input().split())) # A:非負整数列
#     B = list(map(int, input().split())) # B:非負整数列

#     A_mod = sorted([a % M for a in A])
#     B_mod = [b % M for b in B]

#     total = 0
#     for b in B_mod:
#         target = (M - b) % M
#         idx = bisect.bisect_left(A_mod, target)
#         if idx == len(A_mod):
#             chosen = A_mod.pop(0)
#         else:
#             chosen = A_mod.pop(idx)
#         total += (chosen + b) % M

#     results.append(total)

# # 出力
# for res in results:
#     print(res)

# 置換先C++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    vector<int> results;

    while (T--) {
        int N, M;
        cin >> N >> M;
        vector<int> A(N), B(N);

        for (int i = 0; i < N; ++i) cin >> A[i];
        for (int i = 0; i < N; ++i) cin >> B[i];

        vector<int> A_mod(N), B_mod(N), used(N, 0);

        for (int i = 0; i < N; ++i) A_mod[i] = A[i] % M;
        for (int i = 0; i < N; ++i) B_mod[i] = B[i] % M;

        sort(A_mod.begin(), A_mod.end());

        int total = 0;
        for (int i = 0; i < N; ++i) {
            int b = B_mod[i];
            int target = (M - b) % M;

            auto it = lower_bound(A_mod.begin(), A_mod.end(), target);

            // 探索開始位置
            int idx = distance(A_mod.begin(), it);
            while (idx < N && used[idx]) ++idx;

            if (idx == N) {
                idx = 0;
                while (used[idx]) ++idx;
            }

            used[idx] = 1;
            total += (A_mod[idx] + b) % M;
        }

        results.push_back(total);
    }

    for (int res : results) {
        cout << res << '\n';
    }

    return 0;
}
