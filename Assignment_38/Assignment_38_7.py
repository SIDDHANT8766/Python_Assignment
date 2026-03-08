import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    
    Border = "-" * 50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)
    print("\n")

    Dataset = "student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    sns.scatterplot(x = df["StudyHours"], y = df["PreviousScore"])

    plt.show()

if __name__ == "__main__":
    main()