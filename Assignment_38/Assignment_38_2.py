import pandas as pd

def main():
    
    Border = "-"*50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)

    print("\n")

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("Total number of student : \n",len(df))

    print()

    print("Passed student are : \n",(df["FinalResult"] == 1).sum())

    print()

    print("Failed student are : \n",(df["FinalResult"] == 0).sum())




if __name__ == "__main__":
    main()