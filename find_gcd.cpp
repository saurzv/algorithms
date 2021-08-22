// Find GCD
// euclid algorithm to find gcd
// T(n) = O(log(min(a,b)))

#include <bits/stdc++.h>
using namespace std;

int find_gcd(int a, int b){
    if(b == 0)
        return a;
    else
        return find_gcd(b, a%b);
}

int find_lcm(int a, int b){
    return (a*b)/find_gcd(a,b);
}

int main()
{
    int gcd = find_gcd(14, 24);
    int lcm = find_lcm(14,24);
    cout << gcd << " "<< lcm << '\n';
    return 0;
}

/*
prints: 2 168
*/