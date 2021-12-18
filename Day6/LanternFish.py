import time
from collections import defaultdict

def main():
    LanternFish_Time_Cycles = SetFishList()
    for Day in range(256):
        LanternFish_Time_Cycles = NextDay(LanternFish_Time_Cycles)
    
    print(sum(LanternFish_Time_Cycles.values()))

def SetFishList():
    x = defaultdict(int)
    file = open("input.txt")
    temp = list(map(int, file.read().split(',')))
    for t in temp:
        if t not in x:
            x[t] = 0
        x[t]+=1
    return x

def NextDay(Lanternfish_Time_Cycles):
    Temp = defaultdict(int)
    for Time_Cycle, Count in Lanternfish_Time_Cycles.items():
        if Time_Cycle == 0:
            Temp[6] += Count
            Temp[8] += Count
        else:
            Temp[Time_Cycle-1] += Count
    return Temp

if __name__ == "__main__":
    main()
   