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

    # Draw Boxplot
    plt.boxplot(df["Attendance"])
    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance")
    plt.show()

    

if __name__ == "__main__":
    main()