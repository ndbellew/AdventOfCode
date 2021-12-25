"""
    Advent of Code Day 1
    Part 1 and 2
    P1: The goal is to take the input of submarine depths and iterate through the list. 
    Each iteration you must determine if the number is higher than the previous number (increased)
    then count how many increases have been made. 
    P2: iterating the exact same way except you take the sum of the current depth and the next two depths. 
    Then taking all of the sums into a new depths list and performing the same task as form P1. 
"""
def main():
    subdepths = list()
    # Read the input file into a list of depths called subdepths. 
    with open(f"input.txt") as file:
        for index, subdepth in enumerate(file):
            subdepths.append(int(subdepth))
    # for P2 Create a new list of Depths that are the sums of three depths in the weird order described.
    print(f"Day 1: {evaluateDepths(subdepths)}")
    print(f"Day 2: {evaluateDepths(setDepths(subdepths))}")
    # For P1 just send the list into evaluate Depths and get the answer.
    
def evaluateDepths(Depths):
    ans = 0
    # ans will increment if the current depth is higher than the previous. 
    for i in range(1, len(Depths)):
        # Loop starts at 1 because the first location can't be an increase. 
        if Depths[i]>Depths[i-1]:
            ans+=1
    return ans

def setDepths(depths):
    temp = list()
    # loop through depths be ensure that the loop stops 2 before the end. Since every three are added into the loop.
    # So the last two will only be part of a single group. 
    for depth in range(len(depths)-3+1):
        # this uses a python slice to include the current position and the next two positions. 
        temp.append(sum(depths[depth: depth+3]))
    return temp


if __name__=="__main__":
    main()