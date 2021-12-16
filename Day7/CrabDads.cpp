
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void SetCrabPositions(vector<int>& Positions);
int VectorMax(vector<int> Pos);

int main(int argc, char const * argv[]){
    int MaxNum = 0;
    int sum = 0;
    vector<int> Positions;
    SetCrabPositions(Positions);
    MaxNum =  VectorMax(Positions);
    for (auto num : Positions)
        sum += num;

    cout << sum - (Positions.size()*MaxNum) << endl;

    return 0;
}

void SetCrabPositions(vector<int>& Positions){
    string line;
    ifstream inf ("input.txt");
    while (getline (inf, line)){
        stringstream ss(line);
        string StrPos;

        while (getline (ss, StrPos, ',')) Positions.push_back(stoi(StrPos));
    }
}

int VectorMax(vector<int> Pos){
    map<int, int> Counters;
    int currentMax = 0;
    unsigned arg_max = 0;
    for (auto i: Pos)
        Counters[i]++;
    for(auto it = Counters.cbegin(); it != Counters.cend(); ++it ) 
    if (it ->second > currentMax) {
        arg_max = it->first;
        currentMax = it->second;
    }
    return arg_max;
}