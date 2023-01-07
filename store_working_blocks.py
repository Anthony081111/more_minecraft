"""This module will help identify working Minecraft blocks and store the in a file."""
from mcpi.minecraft import Minecraft
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


# set up a location to test blocks
# Steve's Dec 17 location of the player
x = 273
y = -25
z = 130

mc.player.setTilePos(x, y, z)

block_type = [324, 330]
# ?nput_flag = True
# while input_flag:
    # filename = 'blocks_that_work.txt'
#for b_type in block_type:
for i in range(41):
    mc.setBlocks(x + 4, y, z + 4, x + 4, y + 4, z + 4, i)
    # block_description = input("description for block  " + str(i) + "--  ")
    # bd = str(i), "  xxx  ", block_description
    # with open (filename,'a') as out_put:
    #     out_put.write(str(i) + "  xxx  " + block_description)
    mc.postToChat(str(i))
    time.sleep(3)

# mc.setBlocks(x + 6, y, z + 4, 431, 1)
# mc.setBlocks(x + 8, y, z + 4, 431, 1)
# mc.setBlocks(x + 10, y, z + 4, 431, 1)
# mc.setBlocks(x + 14, y, z + 4, 431, 1)
# mc.setBlocks(x + 16, y, z + 4, 431, 1)
# mc.setBlocks(x + 18, y, z + 4, 431, 1)

# mc.postToChat(str(b_type))

time.sleep(10)


zz = mc.pollChatPosts(self, *args)
print (zz)