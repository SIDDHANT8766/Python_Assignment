import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():

    df = pd.read_csv("student_performance_ml.csv")

    X = df[['StudyHours','Attendance','AssignmentsCompleted']]
    y = df['FinalResult']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    new_students = pd.DataFrame({
        'StudyHours':[2,5,7,4,6],
        'Attendance':[60,80,90,55,85],
        'AssignmentsCompleted':[3,6,8,2,7]
    })

    result = model.predict(new_students)

    print("Predictions : ")
    print(result)

if __name__ == "__main__":
    main()