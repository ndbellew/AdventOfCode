

def main():
    P1Pos,P2Pos = getData()
    P1Score, P2Score = 0,0
    counter = list(range(1,101))
    Turn = 1
    print(f"Behold the answer {RunGame(P1Pos, P2Pos, P1Score, P2Score, 1, Turn,0)}")

def RunGame(P1Pos, P2Pos, P1Score, P2Score, DieNum, Turn, DieCounter):
    DieMod = 3
    if (DieNum+1)%101!=0 and (DieNum+2)%101!=0:
        DiceRolls = [DieNum%101, (DieNum+1)%101, (DieNum+2)%101]
    elif (DieNum+1)%101==0:
        DiceRolls = [DieNum%101, (DieNum+2)%101, (DieNum+3)%101]
        DieMod = 4
    elif (DieNum+2)%101==0:
        DiceRolls = [DieNum%101, (DieNum+1)%101, (DieNum+3)%101]
        DieMod = 4

    Move = sum(DiceRolls)%10
    if Turn == 1:
        Turn = 2
        P1Pos = (P1Pos + Move) % 10
        if P1Pos == 0:
            P1Score+=10
        P1Score += P1Pos
        print(f"Current Die {DieNum} {DiceRolls} Player 1: Pos {P1Pos} Score {P1Score}\n")
    elif Turn == 2:
        Turn = 1
        P2Pos = (P2Pos + Move) % 10
        if P2Pos == 0:
            P2Score+=10
        P2Score += P2Pos
        print(f"Current Die {DieNum} {DiceRolls} Player 2: Pos {P2Pos} Score {P2Score}\n")

    DieNum+=DieMod
    if DieNum%101 == 0:
        DieNum+=1
    DieCounter+=3
    if P1Score>=1000:
        return "Player1", P1Score, P1Pos,P2Score,DieNum,DieCounter, f" the answer is {DieCounter*P2Score}"
    elif P2Score>=1000:
        print(f"{P1Score=}, {P1Pos=}")
        return "Player2", P2Score, P2Pos, DieNum,DieCounter, f" the answer is {DieCounter*P1Score}"
    else:
        return RunGame(P1Pos, P2Pos, P1Score, P2Score, DieNum, Turn, DieCounter)

def getData():
    file = open("input.txt")
    data = file.read().split('\n')
    return int(data[0][-1]),int(data[1][-1])


if __name__ == "__main__":
    main()