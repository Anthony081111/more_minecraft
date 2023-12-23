"""This module will help us build a house."""
from mcpi.minecraft import Minecraft
import time
import os
import random

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


def roundDown(n):
    return int("{:.0f}".format(n))


def clear_area(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset):
    """clear a cubic area starting from the corner using block ID = 0 which is air """
    mc.setBlocks(x_corner, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, 0)


def build_floor(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_type):
    """ build floor at altitude y_corner using the block ID and block type attributes """
    mc.setBlocks(x_corner, y_corner + y_offset, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset,
                 block_type)


def build_walls(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_id, grounded_floor_or_maybe_not,
                block_type=""):
    """ build a wall starting at x_corner, y_corner, z_corner using the requested block_type attribute.

    A wall must have an offset >= to 3 to have windows or doors

        This module will ask if player wants 0 to 2 doors.  Any doors will be placed in the middle of the wall.
        This module will ask if player wants 0 to 2 windows.  Windows will be centered on the left or right half of
        wall."""

    # When the wall_flag is true you can build or rebuild walls
    wall_flag = True
    while wall_flag:
        # determine which wall and direction we are building
        input_flag = True
        wall_direction = 0
        if grounded_floor_or_maybe_not:
            while input_flag == True:
                mc.postToChat("enter a number from 1 to 4 from this list to give direction of wall")
                wall_direction = int(input("""enter a number from one to four from this list to give direction of wall
                                              1 for x axis wall from x_corner,y_corner,z_corner                                 
                                              2 for x axis wall from x_corner,y_corner,z_corner + z_offset
                                              3 = z axis wall from x_corner,y_corner,z_corner
                                              4 = z axis wall from x_corner + x_offset,y_corner,z_corner ---  """))
                if wall_direction > 0 and wall_direction < 5:
                    input_flag = False
        else:
            mc.setBlocks(x_corner, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner, block_id)
            mc.setBlocks(x_corner, y_corner, z_corner + z_offset, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, block_id)
            mc.setBlocks(x_corner, y_corner, z_corner, x_corner, y_corner + y_offset, z_corner + z_offset, block_id)
            mc.setBlocks(x_corner + x_offset, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, block_id)
            wall_direction == 5

        if wall_direction == 1:
            mc.setBlocks(x_corner, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner, block_id)
        elif wall_direction == 2:
            mc.setBlocks(x_corner, y_corner, z_corner + z_offset, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, block_id)
        elif wall_direction == 3:
            mc.setBlocks(x_corner, y_corner, z_corner, x_corner, y_corner + y_offset, z_corner + z_offset, block_id)
        elif wall_direction == 4:
            mc.setBlocks(x_corner + x_offset, y_corner, z_corner, x_corner + x_offset, y_corner + y_offset, z_corner + z_offset, block_id)
        else:
            pass

        # determine how many doors to put in the current wall
        # for a wall to have 1 or 2 doors the wall offset must be >= 4
        input_flag = True
        if (wall_direction == 1 or wall_direction == 2) and x_offset < 4:
            mc.postToChat("This wall will have no window or doors")
            input_flag = False
        if (wall_direction == 3 or wall_direction == 4) and z_offset < 4:
            mc.postToChat("This wall will have no window or doors")
            input_flag = False

        # Get number of doors for this wall
        if grounded_floor_or_maybe_not:
            while input_flag:
                mc.postToChat("Would you like 0, 1, or 2 doors?")
                doors = int(input("Would you like 0, 1, or 2 doors?"))
                mc.postToChat(doors)
                if doors >= 0 and doors <= 4:
                    input_flag = False
        else:
            doors = 0
        # place doors in wall
        if doors == 1 and wall_direction == 1 and x_offset > 3:
            door_location = roundDown(x_offset / 2)
            mc.setBlocks(x_corner + door_location, y_corner, z_corner,
                         x_corner + door_location, y_corner + 1, z_corner,
                         64, 0)
            mc.setBlocks(x_corner + door_location, y_corner, z_corner,
                         x_corner + door_location, y_corner + 1, z_corner,
                         64, 8)
        elif doors == 2 and wall_direction == 1 and x_offset > 3:
            door_location = roundDown(x_offset / 2)
            mc.setBlocks(x_corner + door_location, y_corner, z_corner,
                         x_corner + door_location + 1, y_corner + 1, z_corner,
                         64, 0)
        elif doors == 1 and wall_direction == 2 and x_offset > 3:
            door_location = roundDown(x_offset / 2)
            mc.setBlocks(x_corner + door_location, y_corner, z_corner + z_offset,
                        x_corner + door_location, y_corner + 1, z_corner + z_offset,
                        64, 0)
        elif doors == 2 and wall_direction == 2 and x_offset > 3:
            door_location = roundDown(x_offset / 2)
            mc.setBlocks(x_corner + door_location, y_corner, z_corner + z_offset,
                         x_corner + door_location + 1, y_corner + 1, z_corner + z_offset,
                         64, 0)
        elif doors == 1 and wall_direction == 3 and z_offset > 3:
            door_location = roundDown(z_offset / 2)
            mc.setBlocks(x_corner, y_corner, z_corner + door_location,
                         x_corner, y_corner + 1, z_corner + door_location,
                         64, 0)
        elif doors == 2 and wall_direction == 3 and z_offset > 3:
            door_location = roundDown(z_offset / 2)
            mc.setBlocks(x_corner, y_corner, z_corner + door_location,
                         x_corner, y_corner + 1, z_corner + door_location + 1,
                         64, 0)
        elif doors == 1 and wall_direction == 4 and z_offset > 3:
            door_location = roundDown(z_offset / 2)
            mc.setBlocks(x_corner + x_offset, y_corner, z_corner + door_location,
                         x_corner + x_offset, y_corner + 1, z_corner + door_location,
                         64, 0)
        elif doors == 2 and wall_direction == 4 and z_offset > 3:
            door_location = roundDown(z_offset / 2)
            mc.setBlocks(x_corner + x_offset, y_corner, z_corner + door_location,
                         x_corner + x_offset, y_corner + 1, z_corner + door_location +1,
                         64, 0)
        elif doors == 0:
            mc.postToChat("Have fun with your doorless wall!")
        else:
            mc.postToChat("Go touch some grass.")

        # Place windows in walls
        # Walls need to be wide enough to allow doors and windows
        #    example 1: wall must be at least 3 blocks wide for 1 window
        #    example 2: wall must be at least 6 blocks wide to have 2 doors and 2 windows
        # Get number of windows for this wall
        input_flag = False
        if wall_direction == 1 or wall_direction == 2 and x_offset > 3:
            input_flag = True
        if wall_direction == 3 or wall_direction == 4 and x_offset > 3:
            input_flag = True

        if grounded_floor_or_maybe_not:
            while input_flag:
                mc.postToChat("Would you like 0 1 or 2 windows")
                windows = int(input("Would you like 0, 1, or 2 windows?"))
                mc.postToChat(windows)
                if windows == 0 or windows == 2 or windows == 1:
                    input_flag = False
                else:
                    input_flag = True
        else:
            windows = random.randint(0, 2)
            print(f"{doors}    {windows}    {wall_direction}")
        if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 1 and windows == 1 and x_offset > 3:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + window_location, y_corner + 1, z_corner, 20)
        elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 1 and windows == 2 and x_offset > 4:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + window_location, y_corner + 1, z_corner, 20)
            mc.setBlock(x_corner + x_offset - window_location, y_corner + 1, z_corner, 20)
        if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 2 and windows == 1 and x_offset > 3:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + window_location, y_corner + 1, z_corner + z_offset, 20)
        elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 2 and windows == 2 and x_offset > 4:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + window_location, y_corner + 1, z_corner + z_offset, 20)
            mc.setBlock(x_corner + x_offset - window_location, y_corner + 1, z_corner + z_offset, 20)
        if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 3 and windows == 1 and x_offset > 3:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner, y_corner + 1, z_corner + window_location, 20)
        elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 3 and windows == 2 and x_offset > 4:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner, y_corner + 1, z_corner + window_location, 20)
            mc.setBlock(x_corner, y_corner + 1, z_corner + z_offset - window_location, 20)
        if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 4 and windows == 1 and x_offset > 3:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset + window_location, 20)
        elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 4 and windows == 2 and x_offset > 4:
            window_location = roundDown(x_offset / 4)
            mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset + window_location, 20)
            mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset - window_location, 20)

        if not grounded_floor_or_maybe_not:
            for wall_direction in range(1, 5):
                windows = random.randint(0, 2)
                if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 1 and windows == 1 and x_offset > 3:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + window_location, y_corner + 1, z_corner, 20)
                elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 1 and windows == 2 and x_offset > 4:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + window_location, y_corner + 1, z_corner, 20)
                    mc.setBlock(x_corner + x_offset - window_location, y_corner + 1, z_corner, 20)
                if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 2 and windows == 1 and x_offset > 3:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + window_location, y_corner + 1, z_corner + z_offset, 20)
                elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 2 and windows == 2 and x_offset > 4:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + window_location, y_corner + 1, z_corner + z_offset, 20)
                    mc.setBlock(x_corner + x_offset - window_location, y_corner + 1, z_corner + z_offset, 20)
                if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 3 and windows == 1 and x_offset > 3:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner, y_corner + 1, z_corner + window_location, 20)
                elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 3 and windows == 2 and x_offset > 4:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner, y_corner + 1, z_corner + window_location, 20)
                    mc.setBlock(x_corner, y_corner + 1, z_corner + z_offset - window_location, 20)
                if (doors == 1 or doors == 2 or doors == 0) and wall_direction == 4 and windows == 1 and x_offset > 3:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset + window_location, 20)
                elif (doors == 1 or doors == 2 or doors == 0) and wall_direction == 4 and windows == 2 and x_offset > 4:
                    window_location = roundDown(x_offset / 4)
                    mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset + window_location, 20)
                    mc.setBlock(x_corner + x_offset, y_corner + 1, z_corner + z_offset - window_location, 20)
            wall_flag = False


        # Determine if more work is to be done on walls
        if grounded_floor_or_maybe_not:
            mc.postToChat("Do you want to continue building or re-building walls y or n")
            more_walls = input("Do you want to continue building or re-building walls? y or n ---  ")
            if more_walls != "y":
                wall_flag = False


def build_stairs(block_id3, x, y, z, x_offset, y_offset, z_offset, num_stairs, direction=None):
    steps = 0
    while steps < num_stairs:
        mc.setBlock(x+steps, y+steps, z, block_id3)
        steps += 1
    mc.setBlock(x+steps-2, y+steps-1, z, 0)
    mc.setBlock(x+steps-3, y+steps-1, z, 0)
    mc.setBlock(x+steps-4, y+steps-1, z, 0)


def save_coordinates(x, y, z, description):
    # open file or create file if it does not already exist
    try:
        file_size = os.getsize('coordinates_file.txt')
        coord_file = open('coordinates_file.txt', 'a')
    except:
        # this probably means the file does not exist
        # coord_file = open('coordinates_file.txt', 'a')
        print(' File does not exist ')

    # read file to see if description is already in file


def main():
    # Find the location of the player
    position = mc.player.getTilePos()
    # Anthony's Dec 3  location
    """ position.x = 394
    position.y = 1

    position.z = 48"""

    # Steve's Dec 17 location of the player
    position.x = 269
    position.y = -26
    position.z = 126

    mc.player.setTilePos(position.x, position.y, position.z)

    print(position)

    # clear an area of all blocks
    x_offset = 20.0
    y_offset = 20.0
    z_offset = 20.0
    clear_area(position.x + 1.0, position.y, position.z + 1.0, x_offset, y_offset, z_offset)

    # build the foundation for the house
    foundation_block_id = diamondBlock
    x_corner = float(position.x)
    y_corner = float(position.y)
    z_corner = float(position.z)
    x_offset = 20.0
    y_offset = 20.0
    z_offset = 20.0
    build_floor(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, foundation_block_id)

    # build the 4 wall of the house
    # get one corner of the area to build a house.  We will be using floating point numbers
    x_corner = float(position.x) + 1.0
    y_corner = float(position.y) + 1.0
    z_corner = float(position.z) + 1.0

    x_offset = 10.0
    y_offset = 3.0
    z_offset = 10.0
    block_id = bricks
    block_type = 0
    build_walls(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_id, block_type)
    build_floor(x_corner, y_corner + 4, z_corner, x_offset, y_offset, z_offset, oakWood)
    # build_stairs(x_corner, y_corner, z_corner, x_offset, y_offset, z_offset, block_type)


if __name__ == "__main__":
    main()
