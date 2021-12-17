from pprint import pprint
from collections import Counter
import re 

class Submarine_Number:

    def GetNum(self):
        NumDef = {0:["Top", "HL", "HR", "LL", "LR", "Bot"], 
                2: ["Top", "HR", "Mid", "LL", "Bot"],
                3: ["Top", "HR", "Mid", "LR", "Bot"],
                5: ["Top", "HL", "Mid", "LR", "Bot"],
                6: ["Top", "HL", "Mid","LL", "LR", "Bot"],
                9: ["Top", "HL", "HR", "Mid", "LR", "Bot"]}
        NumList = list()

        Top, HL, HR, Mid, LL, LR, Bot = self.Structure 
        if Top in self.Value:
            NumList.append("Top")
        if HL in self.Value:
            NumList.append("HL")
        if HR in self.Value:
            NumList.append("HR")
        if Mid in self.Value:
            NumList.append("Mid")
        if LL in self.Value:
            NumList.append("LL")
        if LR in self.Value:
            NumList.append("LR")
        if Bot in self.Value:
            NumList.append("Bot")

        for i in NumDef:
            if NumList == NumDef[i]:
                return i
        print(f"FAILURE\n{self.Structure=}\n{self.Value=}")
        return quit(0)

    def __init__(self, Value, Structure):
        self.Value = Value # Should be a string
        self.Structure = Structure
        if len(Value) == len(Structure):
            self.Num = "8"
        elif len(Value) == 3:
            self.Num = "7"
        elif len(Value) == 4:
            self.Num = "4"
        elif len(Value) == 2:
            self.Num = "1"
        else:
            self.Num = str(self.GetNum())

        


def main():
    Segments = getSegments()
    print(f"Answer to Part 1 {PartOne(Segments)}")
    print(f"Answer to part 2: \n{PartTwo(Segments)}")
    
    

def getSegments():
    ListOfSegments = list()
    with open(f"input.txt", 'r') as file:
        for index, note in enumerate(file):
            Temp = note.split (' | ')
            ListOfSegments.append({"SignalPatterns":Temp[0].split(),"OutputValues":Temp[1].split()})
    return ListOfSegments

def PartOne(Segments):# count how many segments are 1,4,7,8
    UniqueNums = {2:1, 4:4, 3:7, 7:8} # Length of Num wires : Corresponding number
    total = 0
    for Segment in Segments:
        for value in Segment["OutputValues"]:# check if unique num
            if len(value) in UniqueNums:
                total += 1# if its 1,4,7,8 add one to total.
    return total

def PartTwo(Segments):
    GrandTotal = 0
    for Segment in Segments:
        Top, HL, HR, Mid, LL, LR, Bot = "","","","","","","" 
        FiveLength = list()
        SixLength = list()
        # ---------------------------------------------------------------------------------------------
        #Structure will equal Top, HL, HR, Mid, LL, LR, and Bot pushed together ("".join(list(allthatshit))) so that it looks like any other value but is ordered
        # in the same way that the numbers work. DO NOT SORT
        # So the goal is to find each of these values using what we know of 1, 4, 7, and 8
        for Pattern in Segment["SignalPatterns"]:
            if len(Pattern) == 2:
                One = "".join(sorted(Pattern))
            elif len(Pattern) == 3:
                Seven = "".join(sorted(Pattern))
            elif len(Pattern) == 4:
                Four = "".join(sorted(Pattern))
            elif len(Pattern) == 5:
                # Could be 2, 3, or 5
                FiveLength.append("".join(sorted(Pattern)))
            elif len(Pattern) == 6:
                # Could be 0, 6, or 9
                SixLength.append("".join(sorted(Pattern)))
            elif len(Pattern) == 7:
                Eight = "".join(sorted(Pattern))
        # Now to solve for 0,6,9 which i think is the easiest.

        for numPattern in SixLength:
            if StringinString(numPattern, Four):
                Nine = numPattern
            elif StringinString(numPattern, Seven):
                Zero = numPattern
            else:
                Six = numPattern

        # This should give me 0,6, and 9 I hope. now i can use 0,6, and 9 to find the remaining numbers.
        # Time to look for 2,3,or 5
        for numPattern in FiveLength:
            if StringinString(numPattern, Seven):
                Three = numPattern
            elif StringinString(Six, numPattern):
                Five = numPattern
            else:
                Two = numPattern

        # now to build the structure by finding Top, HL, HR, Mid, LL, LR, Bot
        Top = DiffStrings(Seven, One)[0] #expecting a single response. 
        HL = DiffStrings(Nine, Three)[0] 
        HR = DiffStrings(Eight, Six)[0]
        Mid = DiffStrings(Eight, Zero)[0]
        LL = DiffStrings(Eight, Nine)[0]
        LR = DiffStrings(One, HR)[0]
        Temp = "".join(DiffStrings(Nine, Four))
        Bot = DiffStrings(Temp, Top)[0]
        # ---------------------------------------------------------------------------------------------
        Structure = "".join([Top, HL, HR, Mid, LL, LR, Bot])
        StrNum = ""
        for Value in Segment["OutputValues"]:
            Val = Submarine_Number(Value, Structure)
            StrNum+=Val.Num
        GrandTotal += int(StrNum)
    return GrandTotal

def StringinString(Larger, Smaller):
    for i in Smaller:
        if i not in Larger:
            return False
    return True

def DiffStrings(Larger, Smaller):
    return list((Counter(list(Larger))-Counter(list(Smaller))).elements())



if __name__ == "__main__":
    main()