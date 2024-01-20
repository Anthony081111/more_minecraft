"""Creates a cycle of blocks starting at block id 0"""
from mcpi.minecraft import Minecraft
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord
import read_csv_files

mc = Minecraft.create()

coordinates = whereCoord.return_coordinates()
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
mc.player.setTilePos(x, y, z)

keep_going = True
current_id = int(input("What is your starting id?"))
original_id = current_id
while keep_going:
    blocks_that_work = []
    for i in range(0, 10):
        x = x+2
        mc.setBlock(x, y, z, 0)                                      # Replace what is at location with a block of air
        mc.setBlock(x, y, z, current_id)                             # Place a block with block number = current_id
        invalid_block_id = True
        while invalid_block_id:
            try:
                description, status = read_csv_files.get_block_description(current_id)
                invalid_block_id = False
            except:
                current_id += 1
                invalid_block_id = False
        print(f"block_id_cycle line 30:  Id:  {current_id}   Description:  {description}   Status:  {status}")
        blocks_that_work.append(current_id)
        current_id += 1
    for item in blocks_that_work:
        description, status = read_csv_files.get_block_description(current_id)
        print("block_id_cycle line 36:  \n", blocks_that_work)
        invalid_answer = True
        while invalid_answer:
            valid = input(f"Was id {item} valid?(y is valid, n needs research, ? does not exist)")
            if valid == "y" or valid == "n" or valid == "?":
                invalid_answer = False
        if valid == "y":
            read_csv_files.change_detail(item, "valid description", description)
        elif valid == "n":
            print(f"block_id_cycle line 45: block id = {item} description = {description}" )
            read_csv_files.change_detail(item, "needs research", description)
        elif valid == "?":
            read_csv_files.change_detail(item, "doesn't exist", description)
    stop = input("Do you want to keep going?")
    if stop == "n":
        keep_going = False
