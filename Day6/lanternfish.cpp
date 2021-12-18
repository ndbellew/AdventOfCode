/*
    Advent of Code Day 6 LanternFish
    Given the current population of Lantern fish
     and their reproduction time cycle I am tasked to 
     Simulate the reproduction of lantern fish. such that 
     I could determine how many fish are alive in 80 days.
*/
// ----------------------------------------------------------
// Includes
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <string>

using namespace std;
// ----------------------------------------------------------
// Prototypes
void bug(string x = "Bug"){printf("%s\n", x.c_str());}
void SetMap(map<int, long long int>& M);
void NextDay(map<int, long long int>& Lanternfish_Time_Cycles);
// ----------------------------------------------------------
// MAIN
int main(int argc, char const * argv[]){
    // ----------------------------------------------------------
    // Init
    long long int sum = 0;
    map <int, long long int> Lanternfish_Time_Cycles;
    int Day = 0;
    // Set the Map to the first set of fish data.
    SetMap(Lanternfish_Time_Cycles);
    // Part one checks for 80 days, 
    // Part two checks for 256 Days
    for (Day = 1; Day <= 256; Day++){
        // Iterate the days which updates the LanternFish Life Cycles. 
        NextDay(Lanternfish_Time_Cycles);
    }
    // get sum of all fish 
    for (auto Num : Lanternfish_Time_Cycles){
        sum+= Num.second;
    }
    // Print out the answer        
    cout << "Number of Lanterfish currently is " << sum << endl;
    // ----------------------------------------------------------
    // END OF MAIN
    return 0;
}
// ----------------------------------------------------------
/*
    Set Map initializes the LanternFish_Life_Cycles map using data pulled in
    from the input.txt file provided by Advent of Code. 
*/
void SetMap(map<int, long long int>& EmptyMap){
    // Init
    string line;
    ifstream inf ("input.txt");
    // Run through input. 
    while (getline (inf, line)){
        stringstream ss(line);
        string Time_Cycle;
        // convert input of strings into integers delimiting by a comma. 
        while (getline (ss, Time_Cycle, ',')){
            // check if the value is already a key in the Map. 
            if ((EmptyMap.find(stoi(Time_Cycle)) == EmptyMap.end()))
            // if its not a key make it a key
            // this only works if all numbers are included in the input. 
                EmptyMap[stoi(Time_Cycle)] = 0;
            // increment the current key by 1. 
            EmptyMap[stoi(Time_Cycle)] +=1;
        }
            
            //V.push_back(stoi(Time_Cycle));
    }

}
// ----------------------------------------------------------
/*
    Next day function increments the Lanternfish Time Cycles, as each
    day passes they come closer to creating offspring. This keeps
    track of each fish as they produce offspring by incrementing
    a new fish (delimited by 8 day cycle) and an old fish post offspring
    (delimited by a 6). 
*/
void NextDay(map<int, long long int>& Lanternfish_Time_Cycles){
    map<int, long long int> Temp;
    for (auto Time_Cycle : Lanternfish_Time_Cycles){
        if (Time_Cycle.first == 0){
            // if Lanternfish is ready to reproduce, it goes back to 6 days
            // and its offsprings starts at 8.
            Temp[6] += Time_Cycle.second;
            Temp[8] += Time_Cycle.second;
        }
        else{
            // Lanternfish is not ready to reproduce so it decrements. 
            Temp[Time_Cycle.first-1] += Time_Cycle.second;
        }
    }
    // Pass by reference updates the Lanternfish Map with the Temp map. 
    Lanternfish_Time_Cycles = Temp;
}
// ----------------------------------------------------------