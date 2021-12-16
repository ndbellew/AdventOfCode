hostFolder = "/home/ndbellew/AdventOfCode/2021/Day3/"


def Counter(BinaryNum):
    one = 0
    zero = 0
    for i in BinaryNum:
        if int(i) == 1:
            one+=1
        else:
            zero+=1
    if one>zero:
        return "1"
    else:
        return "0"

def main():
    BinaryDiagnostics = list()
    ans=""
    with open(f"{hostFolder}Text.txt", 'r') as file:
        for index, num in enumerate(file):
            if index==0:
                BinaryDiagnostics = list(num)
            else:
                for i in range(len(num)):
                    BinaryDiagnostics[i]+= num[i]
    del(BinaryDiagnostics[-1])
    for Diag in BinaryDiagnostics:
            ans+= Counter(Diag)
    Gamma = ans
    Epsilon = ''.join('1' if x == '0' else '0' for x in ans)
    print(f"{Gamma=}\n{Epsilon=}\n{int(Gamma, 2)*int(Epsilon,2)}")
       

if __name__=="__main__":
    main()