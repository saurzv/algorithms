// Counting Sort
// Sort the given array into increasing order
// T(n) = O(n+k)    <-- k is range of numbers to be sorted (max - min)
// worst case time complexity depends on k

#include <bits/stdc++.h>
using namespace std;

void count_sort(vector<int>& arr){

    // finds the maximum number in the array
    int max = arr[0];
    for(auto x : arr)
        if(x > max)
            max = x;
    
    // make another array to store the count of each number in the original array
    vector<int> c(max);
    for (int i = 0; i < arr.size(); i++)
        c[arr[i]] += 1;     // increase the count of each number
    
    // modify the array according to the count of each number
    int j = 0;
    for (int i = 0; i <= c.size(); i++)
    {
        int k = c[i];
        for (int l = 0; l < k; l++)
        {
            arr[j++] = i;
        }
    }
}

int main()
{
    vector<int> arr = {0,5,1,2,4,5,2,1,2,3};
    count_sort(arr);
    for(auto x : arr)
        cout << x << " ";
    return 0;
}

/*
works fine
prints : 0 1 1 2 2 2 3 4 5 5
*/