// Finds all the subset of a given set
// T(n) = O(2^n)

#include <bits/stdc++.h>
using namespace std;

void search(vector<int>& A, vector<int>& subset, int k){
    // prints the active subset each time the search() is called.
    for( auto x : subset){
        cout << x << " ";
    }
    cout << "\n";

    // loops for each item in set A
    for(int i = k; i < A.size(); i++) {
        // add the active item
        subset.push_back(A[i]);
        // call the function again for the next item
        search(A, subset, i+1);
        // backtrack
        subset.pop_back();
    }
}

int main(int argc, char const *argv[])
{
    vector<int> array = {1,2,3};
    vector<int> subset;
    search(array, subset, 0);
    return 0;
}

/*
works fine, prints:

1 
1 2 
1 2 3 
1 3 
2 
2 3 
3
*/