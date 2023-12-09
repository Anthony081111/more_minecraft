"""Makes fields."""
from mcpi.minecraft import Minecraft
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord
import random

mc = Minecraft.create()


def grass_field(x, y, z, offset_x, offset_z):
    # creates a grass field
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 2)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)


def fish(x, y, z, offset_x, offset_z):
    # creates an artificial pond w/ fish
    mc.setBlocks(x+1, y-1, z-1, x+offset_x-1, y-3, z-offset_z+1, 9)
    mc.setBlocks(x, y-4, z, x+offset_x, y-4, z-offset_z, 3)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)
    for i in range(1, 6):
        mc.spawnEntity(x+3, y, z-3, 94)


def farm(x, y, z, offset_x, offset_z):
    # creates a farm
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 60)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 59, 7)


def animals(x, y, z, offset_x, offset_z, animal_type):
    # creates a podzol field w/ animals
    # Pig = 90 Sheep = 91 Cow = 92 chicken = 93
    animal_dict = {"pig": 90, "sheep": 91, "cow": 92, "chicken": 93, "horse": 100, "donkey": 31, "mule": 32}
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 3, 2)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)
    for i in range(1, 6):
        mc.spawnEntity(x+3, y, z-3, animal_dict[animal_type])


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


def fence(x, y, z, offset_x, offset_z):
    # Create a fence around a field
    # 85 is fence, 107 is fence gate
    mc.setBlocks(x, y, z, x+offset_x, y, z, 85, 2)
    mc.setBlocks(x, y, z, x, y, z-offset_z, 85, 2)
    mc.setBlocks(x+offset_x, y, z, x+offset_x, y, z-offset_z, 85, 2)
    mc.setBlocks(x, y, z-offset_z, x+offset_x, y, z-offset_z, 85, 2)
    mc.setBlock(x+offset_x/2, y, z-offset_z, 107)
    mc.setBlocks(x, y, z-offset_z-1, x+offset_x, y, z-offset_z-1, 42)
    mc.setBlocks(x, y, z-offset_z-1, x+offset_x, y, z-offset_z-1, 0)
    mc.setBlock(x+offset_x+1, y, z-offset_z+1, 42)
    mc.setBlock(x+offset_x+1, y, z-offset_z+1, 0)
    mc.setBlock(x+1, y, z+1, 42)
    mc.setBlock(x+1, y, z+1, 0)
    mc.setBlock(x-1, y, z-offset_z+1, 42)
    mc.setBlock(x-1, y, z-offset_z+1, 0)
    mc.setBlock(x+offset_x-1, y, z+1, 42)
    mc.setBlock(x+offset_x-1, y, z+1, 0)


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
    fence(x, y, z, offset_x, offset_z)
    x = x + offset_x + 2
    grass_field(x, y, z, offset_x, offset_z)
    animals(x, y, z, offset_x, offset_z, "cow")
    fence(x, y, z, offset_x, offset_z)
    z = z - offset_z - 2
    grass_field(x, y, z, offset_x, offset_z)
    farm(x, y, z, offset_x, offset_z)
    fence(x, y, z, offset_x, offset_z)
    x = x - offset_x - 2
    grass_field(x, y, z, offset_x, offset_z)
    fish(x, y, z, offset_x, offset_z)
    fence(x, y, z, offset_x, offset_z)
