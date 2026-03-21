import math 
###################################################

def EucDistance(P1, P2):
    return math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)


######################################################

def SiddhantKNN():

    Border = "-"*50

    data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
        {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}
       ]
    
    print(Border)
    print("--------------- User Defined KNN ---------------")
    print(Border)

    print()

    print("Dataset for training : ")
    for i in data:
        print(i)

    print(Border)

    New_Point = {'X' : 3, 'Y' : 3}

    ###################################################

    for d in data:
        d['distance'] = EucDistance(d, New_Point)
    
    print(Border)

    print("Calculated distanxce are : ")
    
    for d in data:
        print(d)

    print(Border)

    print()

    #############################################

    sorted_data = sorted(data , key = lambda item : item['distance'])

    print(Border)
    print("Sorted data is : ")

    for d in sorted_data:
        print(d)

    print(Border)

    ##############################################
    print()
    print("========================================================")
    print("For k = 3")


    k = 3

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    ###############################################

    Votes = {}

    
    for neibour in nearest:
        label = neibour['label']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting Result : ")

    for d in Votes:
        print("Votes : ",d," Number of votes : ",Votes[d])

    print(Border)

    print()

    #############################################

    predicted_class = max(Votes, key = Votes.get)
    print("Predicted class of (3,3) is : ",predicted_class)

    #===========================================================
    print()
    print("========================================================")
    print("For k = 1")

    k1 = 1

    nearest1 = sorted_data[:k1]

    print(Border)
    print("Nearest 1 elements are : ")
    print(Border)

    for d in nearest1:
        print(d)

    print(Border)

    ###############################################

    Votes1 = {}

    
    for neibour1 in nearest1:
        label1 = neibour1['label']
        Votes1[label1] = Votes1.get(label1,0) + 1

    print(Border)
    print("Voting Result for k = 1 : ")

    for d in Votes1:
        print("Votes : ",d," Number of votes : ",Votes1[d])

    print(Border)

    print()

    #############################################

    predicted_class1 = max(Votes1, key = Votes1.get)
    print("Predicted class of (3,3) is : ",predicted_class1)

    #===========================================================
    print()
    print("========================================================")
    print("For k = 5")


    k2 = 5

    nearest5 = sorted_data[:k2]

    print(Border)
    print("Nearest 1 elements are : ")
    print(Border)

    for d in nearest5:
        print(d)

    print(Border)

    ###############################################

    Votes5 = {}

    
    for neibour5 in nearest5:
        label5 = neibour5['label']
        Votes5[label5] = Votes5.get(label5,0) + 1

    print(Border)
    print("Voting Result for k = 5 : ")

    for d in Votes5:
        print("Votes : ",d," Number of votes : ",Votes5[d])

    print(Border)

    print()

    #############################################

    predicted_class5 = max(Votes5, key = Votes5.get)
    print("Predicted class of (3,3) is : ",predicted_class5)
 

############################################################

def main():
    SiddhantKNN()

if __name__ == "__main__":
    main()