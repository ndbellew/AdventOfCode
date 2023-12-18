from pprint import pprint
from statistics import median

def main():
    Syntax = list()
    Syntax = getdata()
    print(f"The answer to Part 1 is: {PartOne(Syntax)}")
    print(f"The answer to Part 2 is: {PartTwo(Syntax)}")

def PartOne(Syntax):
    ans = list()
    for Line in Syntax:
        ErrorScore, Illegal = ParseLine(Line)
        if Illegal == "Illegal":
            ans.append(ErrorScore)
    return sum(ans)

def PartTwo(Syntax):
    ans = list()
    for Line in Syntax:
        MissingScore, Missing = ParseLine(Line)
        if Missing == "Missing":
            ans.append(MissingScore)
    return median(ans)

def ParseLine(Chars):
    Head = [] # Head implementation will be a Stack FILO so that the most recent addition will be what is looked for. 
    BracketDictionary = {
        "(":")", # This will tell you what the character means if the character is not in the list, then it is for closing. 
        "[":"]", # If the closing character does not match the Head then we have a syntax error. 
        "{":"}",
        "<":">"
    }
    IllegalScore = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
    MissingScoreDict = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
    }
    MissingScore = 0
    for Char in Chars:
        if Head == []:
            Head.append(Char)
            continue
        else:
            headChar = Head.pop()
        if Char in BracketDictionary:
            Head.append(headChar)
            Head.append(Char)
            continue
        elif Char not in BracketDictionary:
            if Char == BracketDictionary[headChar]:
                continue
            else:
                #print(f"Expected {BracketDictionary[headChar]} but found {Char} instead.")
                return IllegalScore[Char], "Illegal"
    # Getting here means there are either missing characters or the line is complete.
    # Since  the problem statement says all lines are messed up we can assume all lines here are all missing pieces.
    # The headchar should be completed at this point and does not need to be re-added. 
    # Got to take this and build the opposite side. Ex. Head = ['<', '['] we need to make ['>', ']'] Then score that
    for i in range(len(Head)):
        headchar = Head.pop()
        Missing = MissingScoreDict[BracketDictionary[headchar]]
        MissingScore = (5* MissingScore)+Missing
    return MissingScore, "Missing"

def getdata():
    data = list()
    file = open("input.txt")
    for index, line in enumerate(file):
        data.append(line.replace('\n',''))
    return data

if __name__ == "__main__":
    main()