import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():

    df = pd.read_csv("student_performance_ml.csv")

    X = df[['StudyHours','Attendance']]
    y = df['FinalResult']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test,y_pred)

    print("Accuracy with StudyHours and Attendance :",acc)

if __name__ == "__main__":
    main()