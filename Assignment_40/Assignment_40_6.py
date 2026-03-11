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

    y_pred = model.predict(X_test)

    test_data = X_test.copy()

    test_data['Actual'] = y_test
    test_data['Predicted'] = y_pred

    wrong = test_data[test_data['Actual'] != test_data['Predicted']]

    print("Misclassified Students : ")
    print(wrong)

    print("Total Misclassified :",len(wrong))

if __name__ == "__main__":
    main()