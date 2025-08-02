// 元のプログラム C++に変換
// N = int(input())
// gifts = [tuple(map(int, input().split())) for _ in range(N)]

// Q = int(input())
// queries = [int(input()) for _ in range(Q)]

// MAX_P = 500

// dp = [i for i in range(MAX_P + 1)]

// for P, A, B in reversed(gifts):
//     new_dp = [0] * (MAX_P + 1)
//     for t in range(MAX_P + 1):
//         if t <= P:
//             nt = t + A
//         else:
//             nt = max(0, t - B)
//         if nt > MAX_P:
//             nt = MAX_P
//         new_dp[t] = dp[nt]
//     dp = new_dp

// for x in queries:
//     if x <= MAX_P:
//         print(dp[x])
//     else:
//         tension = x
//         for P, A, B in gifts:
//             if tension <= P:
//                 tension += A
//             else:
//                 tension = max(0, tension - B)
//         print(tension)



#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<tuple<int,int,int>> gifts(N);
    for (int i = 0; i < N; ++i) {
        int P, A, B; cin >> P >> A >> B;
        gifts[i] = make_tuple(P, A, B);
    }

    int Q; cin >> Q;
    vector<long long> queries(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> queries[i];
    }

    const int MAX_P = 500;
    vector<int> dp(MAX_P + 1);
    for (int i = 0; i <= MAX_P; ++i) dp[i] = i;

    // giftsを逆順に処理
    for (int i = N - 1; i >= 0; --i) {
        int P, A, B; 
        tie(P, A, B) = gifts[i];
        vector<int> new_dp(MAX_P + 1);
        for (int t = 0; t <= MAX_P; ++t) {
            int nt;
            if (t <= P) nt = t + A;
            else nt = t - B < 0 ? 0 : t - B;
            if (nt > MAX_P) nt = MAX_P;
            new_dp[t] = dp[nt];
        }
        dp = move(new_dp);
    }

    // クエリ処理
    for (auto x : queries) {
        if (x <= MAX_P) {
            cout << dp[(int)x] << "\n";
        } else {
            long long tension = x;
            for (auto& gift : gifts) {
                int P, A, B;
                tie(P, A, B) = gift;
                if (tension <= P) tension += A;
                else tension = max(0LL, tension - B);
            }
            cout << tension << "\n";
        }
    }

    return 0;
}
