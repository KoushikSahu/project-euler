#include <bits/stdc++.h>
using namespace std;
bool check_prime(int num);

int main()
{
    int number;
    vector<int> factors;
    cout<<"Enter the number to find greatest prime factor\n";
    cin>>number;
    if(check_prime(number)){
        cout<<number<<endl;
    }else
    {
        if(number%2==0){
            factors.push_back(2);;
        }
        for(int i=3;i<=(number/2);i+=2){
            if(number%i==0){
                if(check_prime(i)){
                    factors.push_back(i);
                }else{continue;}
            }
        }
    }
    cout<<factors.at(factors.size()-1);
}

bool check_prime(int num)
{
    if(num==2){
        return true;
    }
    for(int i=2;i<=ceil(pow(num,0.5));i++){
        if(num%i==0){
            return false;
        }
    }return true;
}
