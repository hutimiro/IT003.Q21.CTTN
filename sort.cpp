#include <bits/stdc++.h>
#include <algorithm>
#include <chrono>
#include <vector>
using namespace std;

int print_first_n(const vector<float> &data, int n) {
    for (int i = 0; i < n && i < data.size(); ++i) {
        cout << data[i] << " ";
    }
    cout << endl;
    return 0;
}


void read_column_csv(const string &filename, float column_index, vector<float> &data) {
    ifstream file(filename);
    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string cell;
        float current_index = 0;
        while (getline(ss, cell, ',')) {
            if (current_index == column_index) {
                try {
                    data.push_back(stof(cell));
                } catch (const invalid_argument& e) {
                } catch (const out_of_range& e) {
                }
                break;
            }
            current_index++;
        }
    }
}

int main() {
    vector<float> data;


    for (int i = 0; i < 10; ++i) {

        read_column_csv("random_numbers.csv", i, data); 


        vector<float> data_copy = data; 

        auto start = chrono::high_resolution_clock::now();

        sort(data_copy.begin(), data_copy.end());

        auto end = chrono::high_resolution_clock::now();

        float duration = chrono::duration_cast<chrono::milliseconds>(end - start).count();

        cout << "Run " << (i + 1) << ": " << duration << " ms" << endl;
        
        print_first_n(data_copy, 5); 
        data.clear();

    }


    return 0;
}
