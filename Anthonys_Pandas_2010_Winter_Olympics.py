import pandas as pd


if __name__ == "__main__":
    # Olympics_2010 = "2010_Winter_Olympics.csv"
    # olympics_df = pd.read_csv(Olympics_2010)
    # print(olympics_df.head)
    # print("----------------------------------------------")
    # print(olympics_df.describe(include="all"))
    # temp = olympics_df.iloc[:, 4]
    # print(temp)
    # print(temp.describe())
    # temp2 = olympics_df.iloc[0:8, 4]
    # print(temp2)
    # print("----------------------------------------------")
    # print(temp2.describe())
    # print("----------------------------------------------")
    # olympics_df.sort_values("Sport", inplace=True)
    # print(olympics_df.head())
    Olympics_2010 = "2010_Winter_Olympics_less_NaNs.csv"
    olympics_df = pd.read_csv(Olympics_2010)
    print(olympics_df.describe())
    print("----------------------------------------------")
    temp3 = olympics_df.dropna()
    print(temp3.describe())
