#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int>> activitySelection(vector<pair<int,int>>& activities) {
    // bitiş zamanına göre sırala
    sort(activities.begin(), activities.end(),
         [](const pair<int,int>& a, const pair<int,int>& b) {
             return a.second < b.second;
         });

    vector<pair<int,int>> selected;
    selected.push_back(activities[0]);
    int lastEnd = activities[0].second;

    for (int i = 1; i < activities.size(); i++) {
        if (activities[i].first >= lastEnd) {
            selected.push_back(activities[i]);
            lastEnd = activities[i].second;
        }
    }

    return selected;
}

int main() {
    vector<pair<int,int>> activities = {{1,2}, {3,4}, {0,6}, {5,7}, {8,9}, {5,9}};

    auto result = activitySelection(activities);
    cout << result.size() << " adet etkinlik secilmistir." << endl;
    cout << "Secilen etkinlikler:\n";
    for (auto& [start, end] : result) {
        cout << "(" << start << ", " << end << ")\n";
    }

    return 0;
}