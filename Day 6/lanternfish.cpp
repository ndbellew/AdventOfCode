/*
    Advent of Code Day 6 LanternFish
    Given the current population of Lantern fish
     and their reproduction time cycle I am tasked to 
     Simulate the reproduction of lantern fish. such that 
     I could determine how many fish are alive in 80 days.
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void bug(string x = "Bug"){printf("%s\n", x.c_str());}
void SetVector(vector<int>& V);
void NextDay(vector<int>& Lanternfish_Time_Cycles);

int main(int argc, char const * argv[]){
    vector<int> Lanternfish_Time_Cycles;
    int Day = 0;

    SetVector(Lanternfish_Time_Cycles);

    for (Day = 1; Day <= 80; Day++){
        NextDay(Lanternfish_Time_Cycles);
        // cout << "After  "<< Day << " Days:  ";
        // for (auto Num : Lanternfish_Time_Cycles){
        //      cout << Num << ",";
        // }
        // cout << endl;
    }

    printf("Number of Lanterfish currently is %lu", Lanternfish_Time_Cycles.size());

    return 0;
}

void SetVector(vector<int>& V){

    string line;
    
    ifstream inf ("input.txt");
    while (getline (inf, line)){
        stringstream ss(line);
        string Time_Cycle;
        while (getline (ss, Time_Cycle, ',')) 
            V.push_back(stoi(Time_Cycle));
    }

}

void NextDay(vector<int>& Lanternfish_Time_Cycles){
    vector<int> Temp;
    int New_Lanternfish = 0;
    for (auto& Time_Cycle : Lanternfish_Time_Cycles){
        if (Time_Cycle == 0){
            Temp.push_back(6);
            New_Lanternfish++;
        }
        else{
            Temp.push_back(Time_Cycle-1);
        }
    }
    for (int i = 0; i < New_Lanternfish; i++)
        Temp.push_back(8);
    Lanternfish_Time_Cycles = Temp;
}