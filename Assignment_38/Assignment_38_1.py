import pandas as pd

def main():
    
    Border = "-"*50

    print(Border)
    print("--------------- Student Performance ----------------")
    print(Border)

    print("\n")

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("First 5 record : \n",df.head())       # display first 5 rows
    print()
    print("Last 5 record : \n",df.tail())       # display last 5 rows

    print()

    print("Total number of rows and column : \n",df.shape) # display total like (30,6) 
                                                            #  where 30 rows and 6 columns

    print()

    print("List of columns are : \n",list(df.columns))    # list the all of the columns

    print()

    print("Datatype of each column is : \n",df.dtypes)    # show the datatype of all the columns




if __name__ == "__main__":
    main()