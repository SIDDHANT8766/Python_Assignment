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
 

############################################################

def main():
    SiddhantKNN()

if __name__ == "__main__":
    main()