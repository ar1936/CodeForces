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
    for(int i =0;i<n;i++){
        cin>>v[i];
    }
    vector<int>fac;
    for(int i =1;i*i<=n;i++){
        if(n%i==0){
            fac.push_back(i);
            fac.push_back(n/i);
        }
    }
    int ans = 0;
    for(auto f:fac){
        vector<int>val;
        for(int i =0;i<n;i+=f){
            int sum = 0;
            for(int j = 0;j<f;j++){
                sum+=v[i+j];
            }
            val.push_back(sum);
        }
        sort(val.begin(),val.end());
        ans = max(val.back()-val[0], ans);        
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



