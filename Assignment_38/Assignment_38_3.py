import pandas as pd

def main():
    
    Border = "-"*50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)

    print("\n")

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("Average Study Hours : \n",df["StudyHours"].mean())

    print()

    print("Average Attendence : \n",df["Attendance"].mean())

    print()

    print("Maximum PreviousScore : \n",df["PreviousScore"].max())

    print()

    print("Maximum SleepHours : \n",df["SleepHours"].max())


if __name__ == "__main__":
    main()