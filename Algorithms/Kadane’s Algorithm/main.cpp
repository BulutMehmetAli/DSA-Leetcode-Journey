#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers = {-2,1};
    int current_sum=0;
    int max_sum = INT_MIN;
    for (int i = 0; i < numbers.size(); i++) {
        current_sum += numbers[i];
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
        if (current_sum< 0) {
            current_sum = 0;
        }
    }
    cout << max_sum;

    return 0;
}