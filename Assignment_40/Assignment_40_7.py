import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def TrainModel(state):

    df = pd.read_csv("student_performance_ml.csv")

    X = df[['StudyHours','Attendance','AssignmentsCompleted']]
    y = df['FinalResult']
                                                                                        ####
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = state)

    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test,y_pred)

    print("Random State :",state," Accuracy :",acc)


def main():

    TrainModel(0)
    TrainModel(10)
    TrainModel(42)

if __name__ == "__main__":
    main()