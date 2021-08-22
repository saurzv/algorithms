// Find Exponent
// given a and n, finds a^n
// T(n) = O(log(n))

#include <bits/stdc++.h>
using namespace std;

unsigned long long int find_expo(int a, int n){
    if(n == 0)
        return 1;
    // keep reducing n until n becomes 0, total log(n) call.
    unsigned long long int m = find_expo(a, n/2);
    if(n%2)
        return m*m*a;
    else
        return m*m;
}

int main()
{
    int a = 14, n = 12;
    unsigned long long int x = find_expo(a, n);
    cout << x << '\n';
    return 0;
}

/*
works fine, prints : 56693912375296
*/