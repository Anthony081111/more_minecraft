"""Read a csv file"""
import pandas as pd
import warnings

# Read a csv file into a dataframe

warnings.filterwarnings("ignore")

my_blocks_df = pd.read_csv("blocks_that_work_v3.csv")
for i in range(20):
    print(f"{my_blocks_df['block_number'][i], my_blocks_df['block_description'][i]}")


def get_block_description(block_number):
    # Return the description of the block number
    for i in range(len(my_blocks_df)):
        if my_blocks_df["block_number"][i] == block_number:
            description = my_blocks_df["block_description"][i]
            status = my_blocks_df["status"][i]
            # print(description, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            return description, status
    return "Go do something productive", "Doesn't exist"


def change_detail(block_number, block_status, block_description):
    """Go through the list in our dataframe and change the block status and/or description"""
    for i in range(len(my_blocks_df)):
        if my_blocks_df["block_number"][i] == block_number:
            my_blocks_df["block_description"][i] = block_description
            my_blocks_df["status"][i] = block_status
            try:
                save_csv()
            except:
                save_csv()
            return


def save_csv():
    my_blocks_df.to_csv("blocks_that_work_v3.csv", index=False)


if __name__ == "__main__":
    block_description = get_block_description(3)
    print(block_description)
    change_detail(404, "my favorite color is seven", "test block")
