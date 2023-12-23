"""Makes fields."""
from mcpi.minecraft import Minecraft
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord
mc = Minecraft.create()





if __name__ == "__main__":
    coordinates = whereCoord.return_coordinates()
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
    mc.player.setTilePos(x, y, z)

    block_type = 0                          # this sets block_type to Air
    place_blocks = True
    while place_blocks:
        block_type = int(input("what block number do you want to start with?  "))
        x += 2
        mc.setBlock(x, y, z, block_type)
        x += 2
        block_type += 1
        mc.setBlock(x, y, z, block_type)
        # Display a series of 10 block types with
        for i in range(2, 22, 2):
            for j in range(0, 16):
                mc.setBlock(x + i, y + (j * 2), z, 0, j)
                mc.setBlock(x + i, y + (j * 2), z, block_type, j)
                # try:
                #     print(f"Block number = {i}  block name = {BLOCK(i)}")
            block_type += 1


        place_blocks = False
