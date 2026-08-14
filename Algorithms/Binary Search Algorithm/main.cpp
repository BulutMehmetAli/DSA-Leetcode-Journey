#include <iostream>
using namespace std;
#include <vector>

int binarySearch(vector<int> arr, int targetValue) {
    int size = arr.size();
    int lower = 0 , upper = size -1;
    while (lower <= upper) {
        int mid = lower + (upper - lower) / 2;

        if (arr[mid] == targetValue) {
            return mid;
        }
        if (arr[mid] < targetValue) {
            lower = mid + 1;
        }
        else{
            upper = mid - 1;
        }
    }
    return -1;
}
int main() {
    vector<int> arr = { 2 , 5 , 8 , 12 , 16 , 23 , 38 , 56 , 72 , 91 };
    int x = 38;
    int result = binarySearch(arr, x);
    if (result == -1) {
        cout << "Element is not present in array" << endl;
    }else {
        cout << "Element is present in array: " << result << endl;
    }


    return 0;

}