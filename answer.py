import sys

def Getline(i):
    
    i = int(i)
    if i == 0:
        line1 = "._."
        line2 = "|.|"
        line3 = "|_|"
    if i == 1:
        line1 = "..."
        line2 = "..|"
        line3 = "..|"
    if i == 2:
        line1 = "._."
        line2 = "._|"
        line3 = "|_."
    if i == 3:
        line1 = "._."
        line2 = "._|"
        line3 = "._|"
    if i == 4:
        line1 = "..."
        line2 = "|_|"
        line3 = "..|"
    if i == 5:
        line1 = "._."
        line2 = "|_."
        line3 = "._|"
    if i == 6:
        line1 = "._."
        line2 = "|_."
        line3 = "|_|"
    if i == 7:
        line1 = "._."
        line2 = "..|"
        line3 = "..|"
    if i == 8:
        line1 = "._."
        line2 = "|_|"
        line3 = "|_|"
    if i == 9:
        line1 = "._."
        line2 = "|_|"
        line3 = "..|"

    return [line1,line2,line3]


intIn = str(sys.stdin.readline().strip())

if intIn != "":

    resultLine1 = Getline(intIn[0])[0]
    resultLine2 = Getline(intIn[0])[1]
    resultLine3 = Getline(intIn[0])[2]

    if len(intIn) <= 1:
        print resultLine1
        print resultLine2
        print resultLine3
    else:
        for i in range(1, len(intIn)):
            resultLine1 = resultLine1 + " " + Getline(intIn[i])[0]
            resultLine2 = resultLine2 + " " + Getline(intIn[i])[1]
            resultLine3 = resultLine3 + " " + Getline(intIn[i])[2]

        print resultLine1
        print resultLine2
        print resultLine3
