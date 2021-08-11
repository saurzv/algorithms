// Finds all the permutation of a given set
// T(n) = O(n!) <-- might be wrong, haven't analysed thoroughly

#include <bits/stdc++.h>
using namespace std;

// print all the permutation of a given set
void search(vector<int>& A, vector<int>& permutation, vector<bool>& chosen){
    // if the size of active permutation set is size of given set A
    // print the active permutation array
    if(permutation.size() == A.size()){
        for(auto x : permutation){
            cout << x << " ";
        }
        cout << "\n";
    }
    else {
        for (int i = 0; i < A.size(); i++)
        {   
            // don't chose the chosen object twice
            if(chosen[i] == true)
                continue;
            // if not chosen mark it chosen
            chosen[i] = true;
            // push the active item in the active permutation set
            permutation.push_back(A[i]);
            // do the same for next item
            search(A, permutation, chosen);
            // backtrack
            chosen[i] = false;
            permutation.pop_back();
        }
        
    }
}

int main(int argc, char const *argv[])
{
    vector<int> array = {1,2,3};
    vector<bool> chosen(array.size(), false);
    vector<int> permutation;
    search(array, permutation, chosen);
    return 0;
}

/*
works fine, prints:
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1
*/