from pprint import pprint

# Adding an global to keep track of Cavern Checks
CheckedCaverns = {}
anslist = list()

def bug(x="Bug"):
    print(f"{x}")

def main():
    SmokeInfo = getData()
    print(f"Part One Answer: {PartTwo(SmokeInfo)}")

def PartTwo(SmokeInfo):
    UncheckedCaverns = {}
    AnsNums = list()
    ans = 0
    for y in range(len(SmokeInfo)):
        for x in range(len(SmokeInfo[y])):
            if f"{x},{y}" not in CheckedCaverns:
                CheckforCavern(SmokeInfo, UncheckedCaverns, y,x)
                ans = abs(len(CheckedCaverns) - sum(AnsNums))
                if ans > 0:
                    AnsNums.append(ans)
                print(AnsNums)
    for i in AnsNums:
        if ans == 0:
            ans = i
        else:
            ans *= i
    return ans

def CheckforCavern(SmokeInfo, UncheckedCaverns, y, x):
    CurrNum = SmokeInfo[y][x]
    if CurrNum not in CheckedCaverns:
        if isEdge( SmokeInfo,x,y):
            if isCorner(SmokeInfo, x,y):
                UncheckedCaverns = Corner(SmokeInfo,x,y,UncheckedCaverns)
            else:
                UncheckedCaverns = Edge(SmokeInfo, x, y, UncheckedCaverns)
        else:
            if SmokeInfo[y-1][x] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y+1][x] > CurrNum and SmokeInfo[y][x-1] > CurrNum:
                UncheckedCaverns[f"{x},{y}"] = CurrNum
                if SmokeInfo[y-1][x] == CurrNum+1:
                    UncheckedCaverns[f"{x},{y-1}"] = SmokeInfo[y-1][x]
                if  SmokeInfo[y][x+1] == CurrNum+1:
                     UncheckedCaverns[f"{x+1},{y}"] = SmokeInfo[y][x+1]
                if SmokeInfo[y+1][x] == CurrNum:
                    UncheckedCaverns[f"{x},{y+1}"] = SmokeInfo[y+1][x]
                if SmokeInfo[y][x-1] == CurrNum:
                    UncheckedCaverns[f"{x-1},{y}"] = SmokeInfo[y][x-1]
            if f"{x},{y}" not in CheckedCaverns and f"{x},{y}" in UncheckedCaverns:
                CheckedCaverns[f"{x},{y}"] = CurrNum
        for Coord in UncheckedCaverns:
            if Coord not in CheckedCaverns:
                print(Coord)
                x,y = list(map(int,Coord.split(',')))
                CheckforCavern(SmokeInfo,UncheckedCaverns, y,x)

def isEdge(Tunnelist,x,y):
    XlengthMax = len(Tunnelist[0])-1# Min is 0
    YlengthMax = len(Tunnelist)-1# min is 0
    return x == 0 or y == 0 or x == XlengthMax or y == YlengthMax

def Edge(SmokeInfo, x,y,Nums):
    MaxX = len(SmokeInfo[0])-1
    MaxY = len(SmokeInfo)-1
    CurrNum = SmokeInfo[y][x]
    if x == 0: # Left Side of Matrix
        if SmokeInfo[y-1][x] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y+1][x] > CurrNum:
            Nums[f"{x},{y}"] = CurrNum
            # Now this has been Verified, time to check surrounding.
            if SmokeInfo[y-1][x] == CurrNum+1 and SmokeInfo[y-1][x] not in Nums:
                # Basically this will check each step away from the main point and add those points if they are 1 more than the current point. 
                Nums[f"{x},{y-1}"] = SmokeInfo[y-1][x]
            if SmokeInfo[y][x+1] == CurrNum+1 and SmokeInfo[y][x+1] not in Nums:
                Nums[f"{x+1},{y}"] = SmokeInfo[y][x+1]
            if SmokeInfo[y+1][x] == CurrNum+1 and SmokeInfo[y+1][x] not in Nums:
                Nums[f"{x},{y+1}"] = SmokeInfo[y+1][x]
    elif y == 0: # Top Side of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y+1][x] > CurrNum:
            Nums[f"{x},{y}"] = CurrNum
            if SmokeInfo[y][x-1] == CurrNum+1:
                Nums[f"{x-1},{y}"] = CurrNum+1
            if SmokeInfo[y][x+1] == CurrNum+1:
                Nums[f"{x+1},{y}"] = CurrNum+1
            if SmokeInfo[y+1][x] == CurrNum+1:
                Nums[f"{x},{y+1}"] = CurrNum+1
    elif x == MaxX: # Right Side of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y-1][x] > CurrNum and SmokeInfo[y+1][x] > CurrNum:
            Nums[f"{x},{y}"] = CurrNum
            if SmokeInfo[y][x-1] == 1+CurrNum:
                Nums[f"{x-1},{y}"] = SmokeInfo[y][x-1]
            if SmokeInfo[y-1][x] == CurrNum+1:
                Nums[f"{x},{y-1}"] = SmokeInfo[y-1][x]
            if SmokeInfo[y+1][x] == CurrNum+1:
                Nums[f"{x},{y+1}"] = SmokeInfo[y+1][x] 
    elif y == MaxY: # Bottom of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y-1][x] > CurrNum:
            Nums[f"{x},{y}"] = CurrNum
            if SmokeInfo[y][x-1] == CurrNum+1:
                Nums[f"{x-1},{y}"] = SmokeInfo[y][x-1]
            if SmokeInfo[y][x+1] == CurrNum+1:
                Nums[f"{x+1},{y}"] = SmokeInfo[y][x+1]
            if SmokeInfo[y-1][x] == CurrNum+1:
                Nums[f"{x},{y-1}"] = SmokeInfo[y-1][x]
    if f"{x},{y}" not in CheckedCaverns and f"{x},{y}" in Nums:
        CheckedCaverns[f"{x},{y}"] = CurrNum# This list says the current number has been checked and is approved. 
    return Nums

def isCorner(Tunnelist, x,y):
    XlengthMax = len(Tunnelist[0])# Min is 0
    if (x == 0 and y == 0):
        return True
    elif (x == 0 and y == (len(Tunnelist))-1):
        return True
    elif (x == (len(Tunnelist[0])-1) and y == 0):
        return True
    elif (x == (len(Tunnelist[0])-1) and y == (len(Tunnelist)-1)):
        return True     
    else:
        return False

def Corner(SmokeInfo, x,y, Nums):
    CurrNum = SmokeInfo[y][x]
    if (x == 0 and y == 0): #Top left corner
        if SmokeInfo[y][x+1] > SmokeInfo[y][x] and SmokeInfo[y+1][x] > SmokeInfo[y][x]:
            Nums[f"{x},{y}"] = SmokeInfo[y][x]
            if SmokeInfo[y][x+1] == CurrNum+1:
                Nums[f"{x+1},{y}"] = SmokeInfo[y][x+1]
            if SmokeInfo[y+1][x] == CurrNum+1:
                Nums[f"{x},{y+1}"] = SmokeInfo[y+1][x]
    elif (x == len(SmokeInfo[0])-1 and y == 0): # Top Right Corner
        if SmokeInfo[y][x-1] > SmokeInfo[y][x] and SmokeInfo[y+1][x] > SmokeInfo[y][x]:
            Nums[f"{x},{y}"] = SmokeInfo[y][x]
            if SmokeInfo[y][x-1] == CurrNum+1:
                Nums[f"{x-1},{y}"] = SmokeInfo[y][x-1]
            if SmokeInfo[y+1][x] == CurrNum+1:
                Nums[f"{x},{y+1}"] = SmokeInfo[y+1][x]
    elif (x == 0 and y == len(SmokeInfo)-1):# Bottom Left Cornere
        if SmokeInfo[y][x+1] > SmokeInfo[y][x] and SmokeInfo[y-1][x] > SmokeInfo[y][x]:
            Nums[f"{x},{y}"] = SmokeInfo[y][x]
            if SmokeInfo[y][x+1] == CurrNum+1:
               Nums[f"{x+1},{y}"] = SmokeInfo[y][x+1]
            if SmokeInfo[y-1][x] == CurrNum+1:
                Nums[f"{x},{y-1}"] = SmokeInfo[y-1][x]
    else:# Bottom Right Corner
        if SmokeInfo[y][x-1] > SmokeInfo[y][x] and SmokeInfo[y-1][x] > SmokeInfo[y][x]:
            Nums[f"{x},{y}"] = SmokeInfo[y][x]
            if SmokeInfo[y][x-1] == CurrNum + 1:
                Nums[f"{x-1},{y}"] = SmokeInfo[y][x-1]
            if SmokeInfo[y-1][x] == CurrNum + 1:
                Nums[f"{x},{y-1}"] = SmokeInfo[y-1][x]
    if f"{x},{y}" not in CheckedCaverns and f"{x},{y}" in Nums:
        CheckedCaverns[f"{x},{y}"] = CurrNum
    return Nums
 
def getData():
    Data = list()
    with open(f"input.txt", 'r') as file:
        for index, note in enumerate(file): 
            Data.append(list(map(int, note.replace("\n",""))))
    return Data

if __name__ == "__main__":
    main()