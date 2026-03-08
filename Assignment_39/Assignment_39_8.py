# ------------------------------------------------------------
# Student Performance Prediction using Decision Tree
# ------------------------------------------------------------

# 1 : Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():

    Border = "-"*50

    # ------------------------------------------------------------
    # 2 : Dataset Loading
    # ------------------------------------------------------------

    print(Border)
    print(" 2 : Dataset Loading")
    print(Border)

    print("Loading Dataset...\n")
    Dataset = pd.read_csv("student_performance_ml.csv")
    
    print("First 5 Rows of Dataset:")
    print(Dataset.head())

    print()

    # ------------------------------------------------------------
    # 3 : Data Analysis
    # ------------------------------------------------------------
    print(Border)
    print(" 3 : Data Analysis")
    print(Border)

    print("\nDataset Information:")
    print(Dataset.info())

    print()

    print("\nStatistical Summary:")
    print(Dataset.describe())

    print()

    print("\nChecking Missing Values:")
    print(Dataset.isnull().sum())

    print()


    # ------------------------------------------------------------
    # 4 : Data Visualization
    # ------------------------------------------------------------
    print(Border)
    print(" 4 : Data Visualization")
    print(Border)

    print()

    print("\nGenerating Visualizations...")

    # StudyHours vs FinalResult
    plt.figure()
    plt.scatter(Dataset["StudyHours"], Dataset["FinalResult"])
    plt.xlabel("Study Hours")
    plt.ylabel("Final Result (0=Fail, 1=Pass)")
    plt.title("Study Hours vs Final Result")
    plt.show()

    # Attendance vs FinalResult
    plt.figure()
    plt.scatter(Dataset["Attendance"], Dataset["FinalResult"])
    plt.xlabel("Attendance")
    plt.ylabel("Final Result")
    plt.title("Attendance vs Final Result")
    plt.show()


    # ------------------------------------------------------------
    # 5 : Feature Selection
    # ------------------------------------------------------------

    print(Border)
    print(" 5 : Feature Selection")
    print(Border)
    
    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = Dataset[feature_cols]
    Y = Dataset["FinalResult"]

    print()


    # ------------------------------------------------------------
    # 6 : Train-Test Split
    # ------------------------------------------------------------

    print(Border)
    print(" 6 : Train-Test Split")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("\nTraining Data Size:", X_train.shape)
    print("Testing Data Size:", X_test.shape)

    print()


    # ------------------------------------------------------------
    # 7 : Model Training
    # ------------------------------------------------------------

    print(Border)
    print(" 7 : Model Training")
    print(Border)

    model = DecisionTreeClassifier(
        criterion='gini',
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, Y_train)
    print("\nModel Training Completed.")

    print()


    # ------------------------------------------------------------
    # 8 : Prediction
    # ------------------------------------------------------------

    print(Border)
    print(" 8 : Prediction")
    print(Border)

    Y_pred = model.predict(X_test)

    print("\nActual Values:\n", Y_test.values)
    print("Predicted Values:\n", Y_pred)

    print()


    # ------------------------------------------------------------
    # 9 : Accuracy Calculation
    # ------------------------------------------------------------

    print(Border)
    print(" 9 : Accuracy Calculation")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("\nModel Accuracy:", accuracy * 100, "%")

    print()


    # ------------------------------------------------------------
    # 10 : Confusion Matrix Generation
    # ------------------------------------------------------------

    print(Border)
    print(" 10 : Confusion Matrix Generation")
    print(Border)


    conf_mat = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix:\n", conf_mat)

    print()


    # ------------------------------------------------------------
    #  Final Conclusion
    # ------------------------------------------------------------

    print(Border)
    print(" Final Conclusion")
    print(Border)

    print()    

    print("\nFinal Conclusion:")
    if accuracy >= 0.80:
        print("Model is performing well with good accuracy.")
    elif accuracy >= 0.60:
        print("Model performance is moderate.")
    else:
        print("Model performance is low. Improvement needed.")


# Driver Code
if __name__ == "__main__":
    main()