#include <bits/stdc++.h>
using namespace std;
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define all(x) x.begin(), x.end()
#define sz(x) (int)x.size()
typedef long long ll;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<int, int> ipair;
typedef pair<ll, ll> llpair;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

/*
    Author: Koushik Sahu
    Created: 21 August 2021 Sat 12:12:08
*/

const int nxm = 1e5+5;
int n=10000;
vll pent(nxm);

bool binary_search(int val){
    int l = 0, h = nxm-1;
    while(l<=h){
        int mid = l + (h-l)/2;
        if(pent[mid] == val) return true;
        else if(pent[mid] > val) h = mid-1;
        else l = mid+1;
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    for(int i=0; i<nxm; i++){
        pent[i] = (1ll*i*(3*i-1))/2;
    }
    ll ans = LONG_LONG_MAX;
    for(int i=1; i<n; i++){
        for(int j=i+1; j<n; j++){
            ll a = pent[i];
            ll b = pent[j];
            if(binary_search(a+b) && binary_search(abs(a-b))){
                if(abs(a-b)<ans) ans = abs(a-b);
            }
        }
    }
    cout<<ans<<'\n';
    return 0;
}
