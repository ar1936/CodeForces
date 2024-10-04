#include <bits/stdc++.h>
using namespace std;


// Generic print function
template<typename T>
void print(const T& data) {
    std::cout << data;
}

// Specialization for std::vector
template<typename T>
void print(const std::vector<T>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        print(vec[i]);
        if (i < vec.size() - 1) std::cout << ", ";
    }
    std::cout << "]";
}

// Specialization for std::map
template<typename K, typename V>
void print(const std::map<K, V>& m) {
    std::cout << "{";
    for (auto it = m.begin(); it != m.end(); ++it) {
        print(it->first);
        std::cout << ": ";
        print(it->second);
        if (std::next(it) != m.end()) std::cout << ", ";
    }
    std::cout << "}";
}

// Specialization for std::set
template<typename T>
void print(const std::set<T>& s) {
    std::cout << "{";
    for (auto it = s.begin(); it != s.end(); ++it) {
        print(*it);
        if (std::next(it) != s.end()) std::cout << ", ";
    }
    std::cout << "}";
}

// Specialization for std::multiset
template<typename T>
void print(const std::multiset<T>& ms) {
    std::cout << "{";
    for (auto it = ms.begin(); it != ms.end(); ++it) {
        print(*it);
        if (std::next(it) != ms.end()) std::cout << ", ";
    }
    std::cout << "}";
}

// Specialization for const char*
void print(const char* str) {
    std::cout << str;
}

// Overload for std::string to avoid ambiguity with char*
void print(const std::string& str) {
    std::cout << str;
}

// Specialization for arrays
template<typename T, size_t N>
void print(const T(&arr)[N]) {
    std::cout << "[";
    for (size_t i = 0; i < N; ++i) {
        print(arr[i]);
        if (i < N - 1) std::cout << ", ";
    }
    std::cout << "]";
}

// Variadic template to handle multiple arguments
template<typename T, typename... Args>
void print(const T& first, const Args&... args) {
    print(first);
    std::cout << " ";
    print(args...);
}

// Newline function
void p_ln() {
    std::cout << std::endl;
}

template<typename T, typename... Args>
void p_ln(const T& first, const Args&... args) {
    print(first, args...);
    std::cout << std::endl;
}

#define int long long





void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    int mn = 32;
    for(int i =0;i<q;i++){
        int x;
        cin>>x;
        if(x>=mn){
            continue;
        }
        mn = x;
        x = (1<<x);
        for(auto &y:v){
            if(y%x==0){
                y+=x/2;
            }
        }
    }
    for(auto y:v){
        cout<<y<<" ";
    }
    p_ln();
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

