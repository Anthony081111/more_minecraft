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


def farm(x, y, z, offset_x, offset_z, crop_type):
    # creates a farm
    crop_dict = {"wheat": 59, "beetroot": 207, "carrot": 141, "potato": 142}
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 60)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, 0)
    mc.setBlocks(x, y, z, x+offset_x, y, z-offset_z, crop_dict[crop_type], 7)


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


def house(x, y, z, offset_x, offset_z):
    mc.setBlocks(x, y, z, x+offset_x, y+4, z-offset_z, 5)              # Build box
    mc.setBlocks(x+1, y, z-1, x+offset_x-1, y+4, z-offset_z+1, 0)      # Hollows box
    mc.setBlocks(x, y+5, z, x+offset_x, y+5, z-offset_z, 17)           # Builds roof
    mc.setBlocks(x+1, y+5, z-1, x+offset_x-1, y+5, z-offset_z+1, 123)  # Builds lamps
    mc.setBlocks(x, y+6, z, x+offset_x, y+6, z-offset_z, 151)          # Powers lamps
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 4)            # Builds floor
    mc.setBlocks(x+1, y, z-1, x+offset_x-1, y, z-offset_z+1, 171, 3)   # Builds carpet (light blue)
    mc.setBlock(x, y+1, z-3, 64, 8)                                    # Builds top of door
    mc.setBlock(x, y, z-3, 64, 0)                                      # Builds bottom of door
    mc.setBlock(x+1, y, z-3, 72)                                       # Builds door opener
    mc.setBlock(x+offset_x-1, y, z-offset_z+1, 26, 10)                 # Builds top of bed
    mc.setBlock(x+offset_x-1, y, z-offset_z+2, 26, 2)                  # Builds bottom of bed
    mc.setBlocks(x, y+1, z-6, x, y+2, z-8, 20)
    mc.setBlocks(x+2, y+1, z, x+3, y+2, z, 20)
    mc.setBlocks(x+6, y+1, z, x+7, y+2, z, 20)
    mc.setBlocks(x+2, y+1, z-offset_z, x+3, y+2, z-offset_z, 20)
    mc.setBlocks(x+6, y+1, z-offset_z, x+7, y+2, z-offset_z, 20)


def mineshaft_lighting(x, y, z):


def mineshaft(x, y, z, offset_x, offset_y, offset_z):
    mc.setBlocks(x-1, y, z, x+1, y+2, z-offset_z, 0)


def storage(x, y, z, offset_x, offset_z):
    mc.setBlocks(x, y, z, x+offset_x, y+4, z-offset_z, 5)              # Build box
    mc.setBlocks(x+1, y, z-1, x+offset_x-1, y+4, z-offset_z+1, 0)      # Hollows box
    mc.setBlocks(x, y+5, z, x+offset_x, y+5, z-offset_z, 17)           # Builds roof
    mc.setBlocks(x+1, y+5, z-1, x+offset_x-1, y+5, z-offset_z+1, 123)  # Builds lamps
    mc.setBlocks(x, y+6, z, x+offset_x, y+6, z-offset_z, 151)          # Powers lamps
    mc.setBlocks(x, y-1, z, x+offset_x, y-1, z-offset_z, 4)            # Builds floor
    mc.setBlock(x, y+1, z-3, 64, 8)                                    # Builds top of door
    mc.setBlock(x, y, z-3, 64, 0)                                      # Builds bottom of door
    mc.setBlock(x+1, y, z-3, 72)                                       # Builds door opener
    mc.setBlocks(x+1, y, z-offset_z+1, x+offset_x-1, y+3, z-offset_z+1, 54, 3)


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
    farm(x, y, z, offset_x, offset_z, "beetroot")
    fence(x, y, z, offset_x, offset_z)

    x = x - offset_x - 2
    grass_field(x, y, z, offset_x, offset_z)
    fish(x, y, z, offset_x, offset_z)
    fence(x, y, z, offset_x, offset_z)

    z = z - offset_z - 2
    grass_field(x, y, z, offset_x, offset_z)
    house(x, y, z, offset_x, offset_z)

    y -= 9
    mineshaft(x, y, z, offset_x, 9, offset_z)

    y += 9
    x = x + offset_x + 2
    grass_field(x, y, z, offset_x, offset_z)
    storage(x, y, z, offset_x, offset_z)

