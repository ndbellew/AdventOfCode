hostFolder = "/home/ndbellew/AdventOfCode/2021/Day2/"

def main():
    Horiz = 0
    Depth = 0
    Aim = 0
    with open(f"{hostFolder}Text.txt", 'r') as file:
        for index, directions in enumerate(file):
            direction, movement = directions.split()
            if direction=="forward":
                Horiz+=int(movement)
                Depth+=(int(movement)*Aim)
            elif direction=="up":
                Aim-=(int(movement))
            elif direction=="down":
                Aim+=(int(movement))
            else:
                print("Entry does not match current list")
                quit(0)
    print(f"{Horiz=}\n{Depth=}\n{Aim=}\nans={Horiz*Depth}")


if __name__=="__main__":
    main()