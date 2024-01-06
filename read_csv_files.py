"""Read a csv file"""
import pandas as pd

# Read a csv file into a dataframe

my_blocks_df = pd.read_csv("blocks_that_work_v2.csv")


def get_block_description(block_number):
    # Return the description of the block number
    block_data = my_blocks_df[my_blocks_df["block_number"] == str(block_number)]
    desc = block_data["block_description"].values[0]
    status = block_data["status"].values[0]
    return desc, status


def change_detail(block_number, block_status):
    selected_row = my_blocks_df.loc[my_blocks_df["block_number"] == block_number]
    my_blocks_df.loc[my_blocks_df["block_number"] == block_number, 'block_status'] = block_status


def save_csv():
    my_blocks_df.to_csv("blocks_that_work_v2.csv", index=False)


if __name__ == "__main__":
    block_description = get_block_description(3)
    print(block_description)
