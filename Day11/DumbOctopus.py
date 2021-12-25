"""
    Day 11 Advent of Code:
    P1 Goal is to count the octopi that are lying at the bottom of some cavern. They flash every few steps and flashing sets off other octopi.
    P2 See when all octopi have flashed at the same time. it is the same as p1 but you go for longer than 100 steps. 
    The Code contains some added functions like PrintGraph, which is just used in the testing process. 
    Step 1: Increment all Octopi
    Step 2: Check for flash and increment surrounding flash.
    Step 3: Count all Flashes and Restore flashed Octopi to 0.
"""
from pprint import pprint

def main():
    OctoGraph = getdata()
    PrintGraph(OctoGraph, f"Graph number: Initial")
    print(f" Number of Flashes in this Octopi Set: {PartOne(OctoGraph)}")
    print(f"Syncronization Discovered at: {PartTwo(getdata())}")

def PartTwo(OctoGraph):
    Flashes = 0
    for Round in range(500): # A guess
        OctoGraph = IncrementOctopi(OctoGraph)
        OctoGraph, Flashes = CountFlashes(OctoGraph, Flashes)
        #PrintGraph(OctoGraph, f"Graph number: {Round+1}")
        if Flashes < 0:
            return Round+1
    return f"No Sync after {Round+1} Rounds"

def PartOne(OctoGraph):
    Flashes = 0
    for i in range(100):
        OctoGraph = IncrementOctopi(OctoGraph)
        OctoGraph, Flashes = CountFlashes(OctoGraph, Flashes)
        #PrintGraph(OctoGraph, f"Graph number: {i+1}")
    return Flashes

def getdata():
    Data = dict()
    with open("input.txt") as file:
        for index, EnergyLevelsRows in enumerate(file):
            EnergyLevelsRows = EnergyLevelsRows.replace("\n","")
            for subIndex, EnergyLevel in enumerate(EnergyLevelsRows):
                x = subIndex+1
                y = index+1
                Data[(x,y)] = int(EnergyLevel)
    return Data

def IncrementOctopi(OctoGraph):
    for Octo in OctoGraph:
        OctoGraph[Octo] += 1
    return OctoGraph

def CountFlashes(OctoGraph, Flashes):
    Flashed = False
    for Octo in OctoGraph:
        if OctoGraph[Octo] > 9:
            # Count Flashes
            Flashed = True
            x,y = Octo
            SurroundingCoords = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
                                (x-1, y+1), (x+1, y), (x+1, y+1), (x, y+1)]
            for Coord in SurroundingCoords:
                if Coord in OctoGraph:
                    OctoGraph[Coord] += 1
            OctoGraph[Octo] = -100000
            # Reset Flashed Value
    if Flashed:
        return CountFlashes(OctoGraph, Flashes)
    else:
        TempFlashes = 0
        for Octo in OctoGraph:
            if OctoGraph[Octo] < 0:
                Flashes += 1
                TempFlashes+=1
                OctoGraph[Octo] = 0
        if TempFlashes == len(OctoGraph):
            return OctoGraph, -1 # Part 2
        return OctoGraph, Flashes

def PrintGraph(Graph, Verbage):
    ListofLists, Final = list(), list()
    for xy in Graph:
        x,y = xy
        try:
            ListofLists[y-1].append(Graph[xy])
        except Exception as E:
            ListofLists.append([Graph[xy]])
    for i in ListofLists:
        Final.append("".join(list(map(str, i))))
    print(Verbage)
    pprint(Final)

if __name__ == "__main__":
    main()