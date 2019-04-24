#include <iostream>
#include <vector>

using namespace std;

int Partition(vector<int> arr, int low, int high){
    int pivot = arr[high];

    int i = low - 1;

    for (int j = low; j <= high- 1; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

vector<int> Quicksort(vector<int> arr, int low, int high){
    if (low < high){
        int pi = Partition(arr, low, high);

        Quicksort(arr, low, pi - 1);
        Quicksort(arr, pi + 1, high);
    }
    return arr;
}

vector<int> OptimizedQuicksort(vector<int> unsorted){ 

    return Quicksort(unsorted, 0, unsorted.size());
}

void OptimizedQuicksortTests(){
    // Test 1
    vector<int> test1 = { 1,5,3,9,2,7 };
    vector<int> result1 = OptimizedQuicksort(test1);
    if (result1 != vector<int>{1,2,3,5,7,9}){ printf("\x1b[31m" "OptimizedQuicksort Test One Failed" "\n"); }

    // Test 2
    vector<int> test2 = { 0, 1 };
    vector<int> result2 = OptimizedQuicksort(test2);
    if (result2 != vector<int>{ 0,1 }){ printf("\x1b[31m" "OptimizedQuicksort Test Two Failed" "\n"); }
}

int main(){
    OptimizedQuicksortTests();

    return 0;
}