#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #include "/home/ashish/.vim/templates/debug.hpp" 
#else
    #define debug(...) 42
#endif

// debug("{variable}", variable);

#define int long long

int MOD = 1e9 + 7;
void solve() {
    int n;
    cin>>n;
    vector<int>a(n), b(n);
    for(int i =0;i<n;i++){
        cin>>a[i];
    }
    for(int i =0;i<n;i++){
        cin>>b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int ans = 1;

    for(int i = 0;i<n;i++){
        int ind = 1 + lower_bound(b.begin(), b.end(), a[i]) - b.begin()-i-1;
        ans = (ind * ans)%MOD;
    }
    
    cout<<ans<<"\n";
}

int32_t main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    #ifdef ONLINEJUDGE
    clock_t tStart = clock();
    freopen("input.txt", "r", stdin);  // Change input source to input.txt
    freopen("output.txt", "w", stdout); 
    #endif
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    int tmp_t = t;
    while (t--) {
        // cout<<"Case #"<<tmp_t-t<<": ";
        solve();
    }
    #ifdef ONLINEJUDGE
    clock_t tEnd = clock();
    double time_taken = double(tEnd - tStart) / CLOCKS_PER_SEC;
    std::cerr << "Time taken: " << time_taken << " seconds" << std::endl;
    #endif
    return 0;
}

