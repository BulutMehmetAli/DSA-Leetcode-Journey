#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {2,3,5,8,12,29,30,33};
    int *s = &v[0];
    int *f = &v[v.size() - 1];

    int target = 20;
    bool found = false;

    s = &v[0];              // ilk eleman
    f = &v[v.size() - 1];   // son eleman

    cout << *(s+1) << endl;  // 3  (değeri görmek için dereference)
    cout << *s << endl;  // 2  (değeri görmek için dereference)

    cout << *f << endl;  // 33

    cout << s << endl;   // adres basar
    cout << f << endl;   // adres basar

    cout << &s << endl;
    cout << &f << endl;
    cout << "**************************************\n" << endl;
    while (s < f) {
        int sum = *s + *f;

        if (sum == target) {
            int index1 = s - &v[0];  // pointer farkı = index
            int index2 = f - &v[0];
            cout << "Bulundu! Indexler: " << index1 << " - " << index2 << endl;
            cout << "Degerler: " << *s << " + " << *f << " = " << target << endl;
            found = true;
            break;  // bulduk, döngüden çık
        }
        else if (sum < target) {
            s = s + 1;  // toplamı büyütmek için soldan ilerle
        }
        else {
            f = f - 1;  // toplamı küçültmek için sağdan geri gel
        }
    }

    if (!found) {
        cout << "Bu toplami veren cift bulunamadi" << endl;
    }

    return 0;
}
/*
-------------------------------------------------------

Diğer Çözüm:
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        // {deger, orijinal_index} ciftleri oluştur
        vector<pair<int,int>> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = {nums[i], i};
        }

        sort(arr.begin(), arr.end(),
             [](const pair<int,int>& a, const pair<int,int>& b) {
                 return a.first < b.first;
             });


        pair<int,int> *s = &arr[0];
        pair<int,int> *f = &arr[n - 1];

        while (s < f) {
            int sum = s->first + f->first;

            if (sum == target) {
                return {s->second, f->second};  // orijinal index'ler
            }
            else if (sum < target) {
                s = s + 1;
            }
            else {
                f = f - 1;
            }
        }

        return {};  // bulunamazsa
    }
};


*/