"""Makes fields."""
from mcpi.minecraft import Minecraft
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord
import random

mc = Minecraft.create()


def grass_field(x, y, z, offset_x, offset_z):
    # creates a grass field w/ flowers(hopefully)
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 2)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)


def plant_flowers(x, y, z, offset_x, offset_z):
    flowers = {'lilac': '175:1', 'blue orchid': '38:1', 'allium': '38:2', 'red tulip': '38:4', 'white tulip': '38:6',
               'rose bush': '175:4'}
    possible_flowers = list(flowers.keys())
    flower_key = random.choice(possible_flowers)
    flower_item = flowers.get(flower_key)
    flower_type = flower_item.split(":")
    for i in range(0, offset_x):
        for j in range(0, offset_z):
            w = random.randint(0, 1)
            if w == 1:
                mc.setBlock(x+i, y, z-j, int(flower_type[0]), int(flower_type[1]))


if __name__ == "__main__":
    coordinates = whereCoord.return_coordinates()
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
    mc.player.setTilePos(x, y, z)
    offset_x = 10
    offset_z = 10
    # grass is 2
    grass_field(x, y, z, offset_x, offset_z)
    plant_flowers(x, y, z, offset_x, offset_z)
