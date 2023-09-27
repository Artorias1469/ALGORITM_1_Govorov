#include <iostream>
#include <vector>
using namespace std;

pair<int, int> robot_coins(vector<vector<int>>& matrix) {
    int n = matrix.size();
    vector<vector<int>> max_coins(n, vector<int>(n, 0));
    vector<vector<int>> min_coins(n, vector<int>(n, 0));

    max_coins[0][0] = min_coins[0][0] = matrix[0][0];

    for (int i = 1; i < n; i++) {
        max_coins[i][0] = min_coins[i][0] = max_coins[0][i] = min_coins[0][i] = max_coins[0][i - 1] + matrix[0][i];
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            max_coins[i][j] = max(max(max_coins[i - 1][j], max_coins[i][j - 1]), min_coins[i - 1][j]) + matrix[i][j];
            min_coins[i][j] = min(min(min_coins[i - 1][j], min_coins[i][j - 1]), max_coins[i - 1][j]) + matrix[i][j];
        }
    }
    return make_pair(max_coins[n - 1][n - 1], min_coins[n - 1][n - 1]);
}

int main() {
    vector<vector<int>> matrix;
    pair<int, int> result = robot_coins(matrix);
    cout << "Максимальная сумма: " << result.first << endl;
    cout << "Минимальная сумма: " << result.second << endl;
    return 0;
}
