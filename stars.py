import pandas as pd
if __name__ == "__main__":
    star_info_file = "Star Info.csv"
    star_df = pd.read_csv(star_info_file)
    print(star_df)
    print("----------------------------------------------")
    print(star_df.describe(include="all"))
    temp = star_df.iloc[:, 1]
    print(temp)
    print(temp.describe())
