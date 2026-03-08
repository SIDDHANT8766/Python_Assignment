from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd

def main():

    Boreder = "-"*50
    
    Dataset = pd.read_csv("student_performance_ml.csv")

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]                    # If feature have a multiple columns
                         #      then take it into the saperate list (IMP)

    X = Dataset[feature_cols]
    Y = Dataset["FinalResult"]

    # Train the Dataset

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)


    model1 = DecisionTreeClassifier(criterion = 'gini', max_depth = 1, random_state = 42)     # Making object of Model 

    # Train the Dataset
    model1.fit(X_train, Y_train)  

    # Test the model
    Y_predict = model1.predict(X_test)

    print("Actual prediction should be for model 1 : \n",Y_test)    
    print("Predicted data for model 1 : \n",Y_predict)   

    # Calculate accuraccy in percentage
    Accuracy = accuracy_score(Y_test, Y_predict)
    print("Accuracy of model is for model 1 : ",Accuracy*100)

    # Confusion matrix of our data
    Conf_Mat = confusion_matrix(Y_test, Y_predict)     # 1 = Pass    # here in our prediction 
    print("Confusion matrix is for model 1 : \n",Conf_Mat)         # 0 = Fail    # TP = 1,TN = 5, FP = 0, FN = 0
    
    # Training accuracy
    train_pred = model1.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)

    # Testing accuracy
    test_pred = model1.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy for model 1:", train_acc)
    print("Testing Accuracy for model 1 :", test_acc)

    ###############################################################################################

    print(Boreder)
    print(Boreder)

    model2 = DecisionTreeClassifier(criterion = 'gini', max_depth = 3, random_state = 42)     # Making object of Model 

    # Train the Dataset
    model2.fit(X_train, Y_train)  

    # Test the model
    Y_predict = model2.predict(X_test)

    print("Actual prediction should be for model 2 : \n",Y_test)    
    print("Predicted data for model 2 : \n",Y_predict)   

    # Calculate accuraccy in percentage
    Accuracy = accuracy_score(Y_test, Y_predict)
    print("Accuracy of model is for model 2 : ",Accuracy*100)

    # Confusion matrix of our data
    Conf_Mat = confusion_matrix(Y_test, Y_predict)     # 1 = Pass    # here in our prediction 
    print("Confusion matrix is for model 2 : \n",Conf_Mat)         # 0 = Fail    # TP = 1,TN = 5, FP = 0, FN = 0
    
    # Training accuracy
    train_pred = model2.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)

    # Testing accuracy
    test_pred = model2.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy for model 2 :", train_acc)
    print("Testing Accuracy for model 2 :", test_acc)

    ####################################################################################################
    
    print(Boreder)
    print(Boreder)

    model3 = DecisionTreeClassifier(criterion = 'gini', random_state = 42)     # Making object of Model 

    # Train the Dataset
    model3.fit(X_train, Y_train)  

    # Test the model
    Y_predict = model3.predict(X_test)

    print("Actual prediction should be for model 3: \n",Y_test)    
    print("Predicted data for model 3 : \n",Y_predict)   

    # Calculate accuraccy in percentage
    Accuracy = accuracy_score(Y_test, Y_predict)
    print("Accuracy of model is for model 3 : ",Accuracy*100)

    # Confusion matrix of our data
    Conf_Mat = confusion_matrix(Y_test, Y_predict)     # 1 = Pass    # here in our prediction 
    print("Confusion matrix is for model 3 : \n",Conf_Mat)         # 0 = Fail    # TP = 1,TN = 5, FP = 0, FN = 0
    
    # Training accuracy
    train_pred = model3.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)

    # Testing accuracy
    test_pred = model3.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy for model 3 :", train_acc)
    print("Testing Accuracy for model 3 :", test_acc)

if __name__ == "__main__":
    main()