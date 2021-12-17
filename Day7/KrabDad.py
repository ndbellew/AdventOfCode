
def main():
    KrabPositions = getData()
    # Average will not give us the correct answer
    Average = int((sum(KrabPositions)/len(KrabPositions))+0.5)
    # it will give us a close answer. 
    averageRange = (abs(Average - 5), abs(Average + 5))
    # This gives a range of 10 numbers to check against, looking for the smallest number. 
    FuelDict = BuildFuelSumList(KrabPositions, averageRange)
    
    for i in FuelDict:
        print(f"To move to Position {i} the crabs will use {FuelDict[i]} fuel")
    
    

def BuildFuelSumList(KrabPositions, averageRange):
    FuelOutcome = dict()
    for i in range(averageRange[0],averageRange[1],1):
        FuelSum = 0
        for Pos in KrabPositions:
            FuelSum += CalculateFuel(Pos, i)
        if i not in FuelOutcome:
            FuelOutcome[i] = FuelSum
    return FuelOutcome

def CalculateFuel(CurrLocation, TargetLocation):
    return (abs(CurrLocation - TargetLocation)**2 + abs(CurrLocation - TargetLocation))/2

def getData():
    File = open("input.txt")
    return list(map(int, File.read().split(',')))

if __name__ == "__main__":
    main()