"""Read a csv file"""
import pandas as pd

# Read a csv file into a dataframe

my_blocks_df = pd.read_csv("blocks_that_work.csv")


def get_block_description(block_number):
    # Return the description of the block number
    block_data = my_blocks_df[my_blocks_df["Block_Number"] == str(block_number)]
    desc = block_data["Block_Description"].values[0]
    return desc


if __name__ == "__main__":
    block_description = get_block_description(3)
    print(block_description)
