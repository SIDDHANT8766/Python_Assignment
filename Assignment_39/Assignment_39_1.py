from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
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


    model = DecisionTreeClassifier()     # Making object of Model 

    # Train the Dataset
    model.fit(X_train, Y_train)      


if __name__ == "__main__":
    main()