

def main():
    Paths = getData()

def PartOne(Paths):
    Counter = 0
    for Path in Paths["Start"]:
        Paths, Counter = RunCounter(Paths[Path], Counter)


def getData():
    Dict = dict()
    with open("input.txt") as File:
        for index, PositionMarker in enumerate(File):
            Pos, Conn = PositionMarker.split("-")
            if Pos not in Dict:
                Dict[Pos] = [Conn]
            else:
                Dict[Pos].append(Conn)

def RunCounter(Path, Counter):

    return Path, Counter
    

if __name__ == "__main__":
    main()