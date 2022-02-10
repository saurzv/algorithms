#include <bits/stdc++.h>
using namespace std;

void prob_1(){
    // given an array of numbers, finds the sum of XOR of each pair
    // i.e if given array : 1 2 3
    // it calculates: 1^2 + 1^3 + 2^3
    int n;
    cin >> n;
    long long cnt[31] = {0}, ans;   // cnt stores the number of 1 bit in each number in the array
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        for (int j = 0; j < 31; j++)    // for each bit of a 32-bit number
        {
            if((x>>j)&1)    // if j-th bit is 1
                cnt[j]++;   // increase the count of j-th index in cnt
        }
    }
    for (int i = 0; i < 31; i++)
    {
        // instead of XOR if we need to find sum of pairwise AND
        // we can change temp = (no. of 1 bits)Choose2
        // in case of OR, change temp = nChoose2 - (no. of 0 bit)Choose2
        long long temp = (cnt[i])*(n-cnt[i]);   // this calculates: (no. of 1 bits)*(no. of 0 bits)
        ans += temp*(1LL<<i);   // temp*2^i
    }
    cout << ans << '\n';
}
/*
ran with inputs :
5
1 2 3 4 5
got output :
42
working fine.
 */

int main()
{
    prob_1();
    return 0;
}