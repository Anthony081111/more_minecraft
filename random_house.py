"""This module will help us build a house."""
from mcpi.minecraft import Minecraft
from walls_floors_and_ceilings_that_are_really_floors import build_walls
import time
mc = Minecraft.create()

air = 0
bedrock = 7
birchwood = 17
bricks = 45
cobblestone = 4
diamondBlock = 57
flowingLava = 10            # These may give us an error
flowingWater = 8            #
glass = 20
glassPane = 102
glassStained = 95  # use block type for colors
goldBlock = 41
grass = 2
gravel = 13
ironBlock = 42
ironDoorBlock = 71
oakDoorBlock = 64
oakWood = 17
stillWater = 9
stoneBrickStairs = 109
stoneBricks = 98
torch = 50
woolBlock = 35  # use block type for colors


def clear_area(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset):
    """clear a cubic area starting from the corner using block ID = 0 which is air """
    mc.setBlocks(x_corner, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, 0)


def build_floor(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_type):
    """ build floor at altitude y_corner using the block ID and block type attributes """
    mc.setBlocks(x_corner, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset,
                 block_type)


"""def build_walls(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_id, block_type):
    """""" build a wall starting at x_corner, y_corner, z_corner using the requested block_type attribute.
        This module will ask if player wants 0 to 2 doors.  Any doors will be placed in the middle of the wall.
        This module will ask if player wants 0 to 2 windows.  Windows will be centered on the left or right half of
        wall.""""""
    doors = int(input("Would you like 0, 1, or 2 doors?"))
    mc.postToChat(doors)
    if doors == 2:
        pass
    elif doors == 1:
        if z_offset == 0:
            door_offset = x_offset / 2
            mc.setBlocks()
    elif doors == 0:
        mc.postToChat("Have fun with your box!")
    else:
        mc.postToChat("Go touch some grass.")

"""


def build_stairs(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_type):
    """build stairs """
    pass


def main():
    # Find the location of the player
    position = mc.player.getTilePos()
    print(position)

    # get one corner of the area to build a house.  We will be using floating point numbers
    """x_corner = float(position.x) + 1.0
    y_corner = float(position.y)
    z_corner = float(position.z) + 1.0"""

    x_corner = 1008
    y_corner = 6
    z_corner = -9069
    mc.player.setTilePos(x_corner, y_corner, z_corner)
    # clear an area of all blocks
    x_offset = 20.0
    y_offset = 20.0
    z_offset = 20.0
    x_corner = x_corner + 1
    y_corner = y_corner
    z_corner = z_corner + 1
    clear_area(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset)

    # build the foundation for the house
    foundation_block_id = 133
    """x_corner = float(position.x + 1)
    y_corner = float(position.y)
    z_corner = float(position.z + 1)"""
    x_corner = x_corner + 1
    y_corner = y_corner
    z_corner = z_corner + 1
    x_offset = 20.0
    y_offset = 0.0
    z_offset = 20.0
    build_floor(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, foundation_block_id)
    x_corner = x_corner + 1
    y_corner = y_corner + 1
    z_corner = z_corner + 1
    x_offset = 10.0
    y_offset = 3.0
    z_offset = 10.0
    # build the 4 wall of the house
    block_id = bricks
    block_type = 0

    build_walls(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_id, block_type)
    build_floor(x_corner, y_corner + y_offset, z_corner, x_offset, 0, z_offset, foundation_block_id)
    build_stairs(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_type)


if __name__ == "__main__":
    main()
