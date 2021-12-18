/*
    Advent of Code Day 5
    Given a bunch of points that create a Vector.
    Part 1, check to see how many lines intersect on the same point where the X1 or Y1 coord
    is the same as x2 or Y2 respectively. This reads in from a file, manipulates the data to
    be easily handled by the code. Then it takes the numbers and runs them through a vector 
    ensuring to check and see whether another line intersects. If it does it counts once, the 
    counter tells us how many lines intersect. 

*/
// ----------------------------------------------------------
// Includes
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
// ----------------------------------------------------------
// Prototypes:
void bug(string x = "Bug"){printf("%s\n", x.c_str());}
void replaceAll(std::string& str, const std::string& from, const std::string& to);
vector<int> tokenizer(std::string s);
void GetLowHigh(int num1, int num2, int& high, int& low);
void PrintAllPoints(vector<string> AllPoints);
// ----------------------------------------------------------
// MAIN
int main(int argc, char const * argv[]){
    // ----------------------------------------------------------
    //init
    vector<vector<int>>  coordinates;
    int x1, x2, y1, y2;
    string line;
    int low, high;
    ifstream fid("input.txt");
    vector<int> Points;
    vector<string> AllPoints, CountedPoints;
    vector<vector<int>> LineSegments;
     int Counter = 0;
    string Temp;
    // Map will be the Graph of each point
    // ----------------------------------------------------------
    // Read from File
    while(getline(fid, line)){
 
        replaceAll(line, " -> ", " ");
        replaceAll(line,",", " ");

        LineSegments.push_back(tokenizer(line));
    }
    // ----------------------------------------------------------
    // Loop through data points, separating each individual point to be analyzed. 
    for (auto Points : LineSegments){

        x1 = Points[0];
        y1 = Points[1];
        x2 = Points[2];
        y2 = Points[3];
        // P1 criteria only care about pieces of X1 and X2 are same. 
        if (x1 == x2){
            high = 0;
            low = 0;
            GetLowHigh(y1,y2, high, low);

            for (int i = low; i<=high;i++){
                // check if Point has already been aded to AllPoints at least once. 
                if (std::count(AllPoints.begin(), AllPoints.end(), (to_string(x1)+","+to_string(i)))==1)
                Counter++;
                // iif the Point is part of AllPoints then Counter increments. 
                AllPoints.push_back(to_string(x1)+","+to_string(i));
            }
        }
        // P1 criteria only care about pieces of Y1 and Y2 are same. 
        else if (y1 == y2){

            GetLowHigh(x1,x2, high, low);

            for (int i = low; i<=high;i++){
                // check if Point has already been aded to AllPoints at least once. 
                if (std::count(AllPoints.begin(), AllPoints.end(), (to_string(i)+","+to_string(y1)))==1)
                Counter++;
                // iif the Point is part of AllPoints then Counter increments. 
                AllPoints.push_back(to_string(i)+","+to_string(y1));
            }
        }
        // Y/Y and X/X are not the same, Math happens. 
        else{
            /*
                calculating all points between two coordinates, bets way to do it is to use a line and calculate each point from x1 to x2. using y1 and y2 to calculate the slope. 
                I will use the Formula Y = (C - Ax)/B where A = Y2 - Y1, B = X1-X2, and C = Ax1 + By1. 
            */
            GetLowHigh(x1,x2, high, low); // Using X as the delimiter as you would in any graphing scenario. if the equation is right then Both Y's should be accounted for. 
            int A, B, C, X, Y;
            A = y2-y1;
            B = x1-x2;
            C = A*x1 + B*y1;
            // Loop through each X from X1 (low) to X2 (high)
            for (X = low; X<=high;X++){
                Y = (C - A*X)/B;
                // Great with Y and X its time to add it to the list. 
                if (std::count(AllPoints.begin(), AllPoints.end(), (to_string(X)+","+to_string(Y)))==1)
                Counter++;
                // if the Point is part of AllPoints then Counter increments. 
                AllPoints.push_back(to_string(X)+","+to_string(Y));
            }

        
        }
    }
    // Print Counter which is the answer. 
    cout << "Counter: " << Counter << endl;
    return 0;
}
// ------------------------------------------------------------------------
/*
    Function will loop through given string (str) and find given string (from). Then 
    it replaces the given string (from) with its replacement (to). This function does so to
    ALL strings that match the given string (from).
*/
void replaceAll(std::string& str, const std::string& from, const std::string& to) {
    if(from.empty())
        return;
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
    }
}
// ------------------------------------------------------------------------
/* 
Function will determine what number is higher or lower for the X1, X2 or Y1, Y2 Coordinates
Changes passed in variables high and low depending on what num is higher. 
*/
void GetLowHigh(int num1, int num2, int& high, int& low){
    if (num1>num2){
        high = num1;
        low = num2;
    }
    else{
        high = num2;
        low = num1;
    }
    
}
// ------------------------------------------------------------------------
/*
Found online, this is function mimics the python .split() functionality (but only with 
Spaces).
*/
vector<int> tokenizer(std::string s){
    stringstream ss(s);
    vector<int> Points;
    string word;
    while(ss >> word){
        Points.push_back(stoi(word));
    }

    return Points;
}
// ------------------------------------------------------------------------
/*
Loops and Prints all Points in a given vector, made primarliy for the vector AllStrings. 
*/
void PrintAllPoints(vector<string> AllPoints){
    for (auto& value : AllPoints){
        cout << value << endl;
    }
}
// ------------------------------------------------------------------------