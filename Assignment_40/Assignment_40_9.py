import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


def main():

    df = pd.read_csv("student_performance_ml.csv")

    df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

    X = df[['StudyHours','Attendance','AssignmentsCompleted','PerformanceIndex']]
    y = df['FinalResult']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test,y_pred)

    print("Accuracy with PerformanceIndex :",acc)

    plt.figure(figsize=(10,6))

    plot_tree(model,feature_names = X.columns,filled=True)

    plt.show()

if __name__ == "__main__":
    main()