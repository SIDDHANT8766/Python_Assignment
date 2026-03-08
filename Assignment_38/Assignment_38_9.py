import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)
    print("\n")

    Dataset = "student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    # Scatter Plot
    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])
    plt.title("AssignmentsCompleted vs FinalResult")
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult (0 = Fail, 1 = Pass)")
    plt.show()


if __name__ == "__main__":
    main()