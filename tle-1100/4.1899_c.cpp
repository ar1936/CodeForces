#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #include "/home/ashish/.vim/templates/debug.hpp" 
#else
    #define debug(...) 42
#endif

// debug("{variable}", variable);

#define int long long

void solve() {
    int n;
    cin>>n;
    vector<int>v(n);
    int mx = -100000000;
    for(int i =0;i<n;i++){
        cin>>v[i];
        mx= max(mx, v[i]);
    }
    int ans = v[0];
    int sum = v[0];
    int mn = min(0LL,v[0]);
    for(int i = 1;i<n;i++){
        if(abs(v[i])%2 == abs(v[i-1])%2){
            sum = 0;
            mn = 0;
        }
        sum+=v[i];
        ans = max(sum-mn, ans);
        mn = min(mn, sum);
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
    
    while (t--) {
        solve();
    }
    
    return 0;
}
