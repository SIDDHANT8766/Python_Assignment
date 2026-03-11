import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():

    df = pd.read_csv("student_performance_ml.csv")

    X = df[['StudyHours','Attendance','AssignmentsCompleted']]
    y = df['FinalResult']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

    model = DecisionTreeClassifier(max_depth = None)

    model.fit(X_train,y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train,train_pred)
    test_acc = accuracy_score(y_test,test_pred)

    print("Training Accuracy :",train_acc)
    print("Testing Accuracy :",test_acc)

if __name__ == "__main__":
    main()