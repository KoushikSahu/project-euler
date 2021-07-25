#include <bits/stdc++.h>
using namespace std;

bool palindrome_check(string a,int i,int j){
    if(a[i]==a[j] && i<=j){
        palindrome_check(a,i+1,j-1);
    }else{
        return 0;
    }
    return 1; 
}

int main()
{
    cout<<palindrome_check("axyza",0,4)<<"\n";
}