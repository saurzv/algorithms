// Find Prime
// finds prime number between 1 to n
// T(n) = O(nlog(log(n)))

#include <bits/stdc++.h>
using namespace std;

// mark false to the number which are not prime
void find_prime(int n, vector<bool>& A){
    // 0 and 1 are not prime
    A[0] = A[1] = false;
    for (int i = 2; i <= n; i++){
        // if a certain number is prime, all it's multiple is not prime
        if(A[i] && i*i <= n){
            // mark all it's multiple flase
            for (int j = i*i; j <= n; j += i)
                A[j] = false;
        }
    }
}

int main()
{
    int n = 23;
    // container of size n+1, all set to true intitially.
    vector<bool> arr(n+1, true);
    // calling find_prime()
    find_prime(n, arr);
    // prints the element which are marked true (i.e. a prime number)
    for (int i = 0; i <= n; i++)
        if(arr[i])
            cout << i << " ";
    return 0;
}
