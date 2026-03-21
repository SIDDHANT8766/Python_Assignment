import math

###################################################

def EucDistance(P1, P2):
    return math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

###################################################

def SiddhantKNN():

    Border = "-"*50

    data = [
        {'student':'A','X':2,'Y':60,'label':'Fail'},
        {'student':'B','X':5,'Y':80,'label':'Pass'},
        {'student':'C','X':6,'Y':85,'label':'Pass'},
        {'student':'D','X':1,'Y':50,'label':'Fail'}
    ]

    print(Border)
    print("----------- Student Pass Fail Prediction -----------")
    print(Border)

    print()
    print("Training Dataset : ")

    for i in data:
        print(i)

    print(Border)

    ###################################################

    StudyHours = int(input("Enter Study Hours : "))
    Attendance = int(input("Enter Attendance : "))

    New_Point = {'X':StudyHours,'Y':Attendance}

    ###################################################

    for d in data:
        d['distance'] = EucDistance(d,New_Point)

    print(Border)
    print("Calculated Distance : ")

    for d in data:
        print(d)

    print(Border)

    ###################################################

    sorted_data = sorted(data , key = lambda item : item['distance'])

    print("Sorted Data : ")
    print(Border)

    for d in sorted_data:
        print(d)

    print(Border)

    ###################################################

    k = 3
    nearest = sorted_data[:k]

    print("Nearest 3 Neighbours : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    ###################################################

    Votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label,0) + 1

    print("Voting Result : ")
    print(Border)

    for v in Votes:
        print("Class :",v," Votes :",Votes[v])

    print(Border)

    ###################################################

    predicted_class = max(Votes , key = Votes.get)

    print("Predicted Result :",predicted_class)

###################################################

def main():
    SiddhantKNN()

if __name__ == "__main__":
    main()