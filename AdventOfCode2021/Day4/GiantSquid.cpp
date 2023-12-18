#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
//--------------------------------------------------------
// PROTOTYPES:
bool iswinner(vector<int> winners, int m);
bool Has_A_Bingo(vector<int> board);
int sum_unmarked(vector<int> *board);
//--------------------------------------------------------
// MAIN:
int main(int argc, char const * argv[]){
    vector<vector<int>> boards;
    vector<int> board, nums, winners, *boardp;
    string line;
    bool Bingo_Nums_Read = false;
    ifstream fid("GS.txt");
    int result1, result2;

    int nb = 0;
    //--------------------------------------------------------
    while(getline(fid, line)){
        if(line.empty()){
            board.clear();
            continue;
        }
        stringstream ss(line);
        string value;
        if(!Bingo_Nums_Read){
            while(getline(ss, value, ',')) nums.push_back(stoi(value));
            Bingo_Nums_Read = true;
        }
        else{
            while(ss >> value) board.push_back(stoi(value));
            if (board.size() == 25 ){
                boards.push_back(board);
                nb++;
                board.clear();
            }
        }
    }
    //--------------------------------------------------------
    /*
        begin running through the numbers and replace the number
        in the boards with a -1, then check if the sum of numbers in a line 
        equal -5. 
    */
    
    for (auto& num: nums){
        for (int i = 0; i < nb; i++){
            boardp = &boards[i];
            int row = 0;
            for (auto& num : boards[i]){
                
                row+=1;
                if (row== 5){
                    row = 0;
                } 
                
            }
            //cout << endl << endl;
            if (iswinner(winners, i)) continue;
            replace(boardp->begin(),boardp->end(),num,-1);
            if(Has_A_Bingo (*boardp)){
                if (winners.size() == 0) {                
                result1 = sum_unmarked(&boards[i]) * num;
                }   
                if (winners.size() == (nb - 1)) result2 = sum_unmarked(boardp) * num;
                winners.push_back(i);
            }
        }
    }
    //--------------------------------------------------------
    printf("Part 1: %d\n", result1);
    printf("Part 2: %d\n", result2);
    return 0;
}
//-------------------------------------------------------
// FUNCTIONS:
bool iswinner(vector<int> winners, int m){
    for (auto num: winners){
        if (num == m) return true;
    }
    return false;
}
//--------------------------------------------------------
bool Has_A_Bingo (vector<int> board){
    int sum = 0;
    // this should look through rows 
    for (int i = 0; i < 5; i++){
        sum = 0;
        for (int j = 0; j < 5; j++){
           // cout<<board[i*5+j]<<endl;
            sum += board[i*5+j];
        }
        if (sum == -5) return true;
    }
    sum = 0;
    // checks bingos through columns
    for (int i = 0; i < 5; i++){
        sum = 0;
        for (int j = 0; j < 5; j++){
          //  cout<<board[i+5*j]<<endl;
            sum += board[i+5*j];
        }
        if (sum == -5) return true;
    }
    return false;
}
//--------------------------------------------------------
int sum_unmarked(vector<int> *board){
    int sum = 0;
    for (auto num: *board){
        if (num != -1) 
        sum += num;
    }
    return sum;
}
//--------------------------------------------------------