from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

def main():
    
    # Load Dataset
    Dataset = pd.read_csv("student_performance_ml.csv")
    print("Dataset is:\n", Dataset)

    # Feature columns
    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    # Input and Output split
    X = Dataset[feature_cols]
    Y = Dataset["FinalResult"]

    # Split dataset into training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    # Create Decision Tree Model
    model = DecisionTreeClassifier(
        criterion='gini',
        max_depth=5,
        random_state=42
    )

    # Train model
    model.fit(X_train, Y_train)

    # Predict on test data
    Y_predict = model.predict(X_test)

    print("\nActual Output:\n", Y_test.values)
    print("Predicted Output:\n", Y_predict)

    # Accuracy (Testing Accuracy)
    Accuracy = accuracy_score(Y_test, Y_predict)
    print("\nTesting Accuracy of model is:", Accuracy * 100)

    # Confusion Matrix
    Conf_Mat = confusion_matrix(Y_test, Y_predict)
    print("\nConfusion Matrix is:\n", Conf_Mat)

    # Training Accuracy
    train_pred = model.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)
    print("\nTraining Accuracy:", train_acc * 100)

    # Testing Accuracy (again separately)
    test_pred = model.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)
    print("Testing Accuracy:", test_acc * 100)

    # Predict for New Student
    New_Student = [[6, 85, 66, 7, 7]]

    Result = model.predict(New_Student)

    print("\nNew Student Data: [6, 85, 66, 7, 7]")

    if Result[0] == 1:
        print("Prediction for new student: PASS")
    else:
        print("Prediction for new student: FAIL")


if __name__ == "__main__":
    main()