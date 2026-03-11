import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    
    CSVname = "student_performance_ml.csv"

    Dataset = pd.read_csv(CSVname)

    Feature_clos = [  
                    "StudyHours",
                    "Attendance",
                    "PreviousScore",
                    "AssignmentsCompleted",
                    "SleepHours"
                    ]
    
    X = Dataset[Feature_clos]
    Y = Dataset["FinalResult"]

    # Split the data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    # Train the model

    model = DecisionTreeClassifier(criterion = 'gini',max_depth = 5, random_state = 42)

    model.fit(X_train,Y_train)

    Myimportance = model.feature_importances_      # calculate all feature score in variable  

    print(Myimportance)           # 

    print("Feature Importance Scores")

    for name,score in zip(X.columns,Myimportance):       # IMP
        print(name,"=",score)

if __name__ == "__main__":
    main()