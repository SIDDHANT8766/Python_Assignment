from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd

def main():
    
    Dataset = pd.read_csv("student_performance_ml.csv")
    print(Dataset)

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


    model = DecisionTreeClassifier(criterion = 'gini', max_depth = 5, random_state = 42)     # Making object of Model 

    # Train the Dataset
    model.fit(X_train, Y_train)  

    # Test the model
    Y_predict = model.predict(X_test)

    print("Actual prediction should be : \n",Y_test)    
    print("Predicted data : \n",Y_predict)   

    # Calculate accuraccy in percentage
    Accuracy = accuracy_score(Y_test, Y_predict)
    print("Accuracy of model is : ",Accuracy*100)

    # Confusion matrix of our data
    Conf_Mat = confusion_matrix(Y_test, Y_predict)     # 1 = Pass    # here in our prediction 
    print("Confusion matrix is : \n",Conf_Mat)         # 0 = Fail    # TP = 1,TN = 5, FP = 0, FN = 0
    
    # Training accuracy
    train_pred = model.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)

    # Testing accuracy
    test_pred = model.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy:", train_acc)
    print("Testing Accuracy:", test_acc)

if __name__ == "__main__":
    main()