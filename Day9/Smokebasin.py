from pprint import pprint

def main():
    SmokeInfo = getData()
    print(f"Part One Answer: {PartOne(SmokeInfo)}")


def PartOne(SmokeInfo):
    Nums = list()
    corners = 0
    for y in range(len(SmokeInfo)):
        for x in range(len(SmokeInfo[y])):
            CurrNum = SmokeInfo[y][x]
            if isEdge( SmokeInfo,x,y):
                if isCorner(SmokeInfo, x,y):
                    Nums = Corner(SmokeInfo,x,y,Nums)
                    corners+=1
                else:
                    Nums = Edge(SmokeInfo, x, y, Nums)
            else:
                if SmokeInfo[y-1][x] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y+1][x] > CurrNum and SmokeInfo[y][x-1] > CurrNum:
                    Nums.append(CurrNum)
    return sum(Nums)+(len(Nums)*1)# *1 is for risk level


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
            Nums.append(CurrNum)
    elif y == 0: # Top Side of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y+1][x] > CurrNum:
            Nums.append(CurrNum)
    elif x == MaxX: # Right Side of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y-1][x] > CurrNum and SmokeInfo[y+1][x] > CurrNum:
            Nums.append(CurrNum)
    elif y == MaxY: # Bottom of Matrix
        if SmokeInfo[y][x-1] > CurrNum and SmokeInfo[y][x+1] > CurrNum and SmokeInfo[y-1][x] > CurrNum:
            Nums.append(CurrNum)
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
    if (x == 0 and y == 0): #Top left corner
        if SmokeInfo[y][x+1] > SmokeInfo[y][x] and SmokeInfo[y+1][x] > SmokeInfo[y][x]:
            Nums.append(SmokeInfo[y][x])
    elif (x == len(SmokeInfo[0])-1 and y == 0): # Top Right Corner
        if SmokeInfo[y][x-1] > SmokeInfo[y][x] and SmokeInfo[y+1][x] > SmokeInfo[y][x]:
            Nums.append(SmokeInfo[y][x])
    elif (x == 0 and y == len(SmokeInfo)-1):# Bottom Left Cornere
        if SmokeInfo[y][x+1] > SmokeInfo[y][x] and SmokeInfo[y-1][x] > SmokeInfo[y][x]:
            Nums.append(SmokeInfo[y][x])
    else:# Bottom Right Corner
        if SmokeInfo[y][x-1] > SmokeInfo[y][x] and SmokeInfo[y-1][x] > SmokeInfo[y][x]:
            Nums.append(SmokeInfo[y][x])
    return Nums
 
def getData():
    Data = list()
    with open(f"input.txt", 'r') as file:
        for index, note in enumerate(file): 
            Data.append(list(map(int, note.replace("\n",""))))
    return Data

if __name__ == "__main__":
    main()