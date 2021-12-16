
hostFolder = "/home/ndbellew/AdventOfCode/2021/Day1/"

def evaluateDepths(Depths):
    ans = 0
    for i in range(1, len(Depths)):
        if Depths[i]>Depths[i-1]:
            ans+=1
    return ans

def setDepths(depths):
    temp = list()
    for depth in range(len(depths)-3+1):
        temp.append(sum(depths[depth: depth+3]))
    return temp

def main():
    subdepths = list()
    
    with open(f"{hostFolder}subtext.txt") as file:
        for index, subdepth in enumerate(file):
            subdepths.append(int(subdepth))
    Depths = setDepths(subdepths)
    print(evaluateDepths(Depths))


if __name__=="__main__":
    main()