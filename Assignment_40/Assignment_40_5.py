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

    y_pred = model.predict(X_test)      # it returns a list

    correct = 0
    total = len(y_test)    

    y_test = list(y_test)

    for i in range(total):

        if(y_test[i] == y_pred[i]):
            correct = correct + 1

    accuracy = correct / total

    print("Manual Accuracy :",accuracy*100)     

if __name__ == "__main__":
    main()