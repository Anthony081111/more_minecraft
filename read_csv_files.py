"""Read a csv file"""
import pandas as pd

# Read a csv file into a dataframe

my_blocks_df = pd.read_csv("blocks_that_work_v3.csv")
for i in range(20):
    print(f"{my_blocks_df['block_number'][i], my_blocks_df['block_description'][i]}")


def get_block_description(block_number):
    # Return the description of the block number
    for items in my_blocks_df:
        print(items)
        if my_blocks_df[my_blocks_df["block_number"] == str(block_number)]:
            print(items)
    quit()

    block_data = my_blocks_df[my_blocks_df["block_number"] == str(block_number)]
    print(block_data)
    desc = block_data['block_description'][block_number]
    status = block_data['status'][block_number]
    return desc, status


def change_detail(block_number, block_status):
    selected_row = my_blocks_df.loc[my_blocks_df["block_number"] == block_number]
    my_blocks_df.loc[my_blocks_df["block_number"] == block_number, 'status'] = block_status


def save_csv():
    my_blocks_df.to_csv("blocks_that_work_v3.csv", index=False)


if __name__ == "__main__":
    block_description = get_block_description(3)
    print(block_description)
