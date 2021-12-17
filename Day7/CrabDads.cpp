
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

void SetCrabPositions(vector<int>& Positions);
int VectorMax(vector<int> Pos);
int median (vector<int> &Pos);
double CalculateFuel(double CurrLocation, double Destination);
// int CalculateFuel(vector<int> Positions, int Destination);//old solution
double Equation(double x){return (0.5 * (x * x) + 0.5 * (x));}
int mean(vector<int> &Pos);
void BuildFuelSumList(map<int, double>& FuelOutcome, vector<int> Positions,int LowAv, int HighAv);

int main(int argc, char const * argv[]){
    vector<int> Positions;
    map<int, double> FuelFindings;
    SetCrabPositions(Positions);
    // Part 1 needed the Median,  Part 2 needs the Mean
//    int PosMedian = median(Positions);
//    cout << PosMedian << endl;
//    int FuelNeeded = CalculateFuel(Positions, PosMedian);
    double PosMean = mean(Positions);
    double LowMean = PosMean-5;
    double HighMean = PosMean+5;
    BuildFuelSumList(FuelFindings, Positions, LowMean, HighMean);

    for (auto FuelNum : FuelFindings){
        cout << fixed << "To get to Position "<< FuelNum.first << " You would need "
            << FuelNum.second << " Fuel" << endl;
    }
    
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

int median (vector<int> &Pos){
    size_t n = Pos.size() / 2;
    nth_element(Pos.begin(), Pos.begin()+n, Pos.end());
    return Pos[n];
}

int mean(vector<int> &Pos){
    double mean = 0;
    double sum_of_elems = 0.0;
    sum_of_elems = accumulate(Pos.begin(), Pos.end(), 0);
    mean = (sum_of_elems / Pos.size())+.5;
    return mean;
}

double CalculateFuel(double CurrLocation, double Destination){ 
    double Difference = abs(((double) CurrLocation - (double)Destination));
    return ((Difference * Difference) + Difference)/2;
}

void BuildFuelSumList(map<int, double>& FuelOutcome, vector<int> Positions,int LowAv, int HighAv){
    for (int i = LowAv; i<= HighAv; i++){
        int FuelSum = 0;
        for (auto Pos : Positions){
            FuelSum += CalculateFuel(Pos, i);
        }
        if ((FuelOutcome.find(i)) == FuelOutcome.end())
            FuelOutcome[i] = FuelSum;
    }
}

// int CalculateFuel(vector<int> Positions, int Destination){
    // Funciton for Part 1 no longer in use. needed to restructure whole code. 
//     double sum = 0;
//     for (auto Position : Positions){
        
//         /*
//         // Works for part one with Median, need to find the exponential growth. 
//         if (Position != Destination)
//             sum += abs(((double) Position - (double)Destination));
//         */
       
//     }
    
//     return (int)sum;
// }

