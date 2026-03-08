import pandas as pd

def main():
    
    Border = "-" * 50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)
    print("\n")

    Dataset = "student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    # Count pass and fail
    pass_count = (df["FinalResult"] == 1).sum()
    fail_count = (df["FinalResult"] == 0).sum()
    total = len(df)

    # Calculate percentage
    pass_percentage = (pass_count / total) * 100
    fail_percentage = (fail_count / total) * 100

    print("Passed Students :", pass_count)
    print("Pass Percentage :", round(pass_percentage, 2), "%")

    print("\n")
    
    print("Failed Students :", fail_count)
    print("Fail Percentage :", round(fail_percentage, 2), "%")


if __name__ == "__main__":
    main()