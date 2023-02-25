"""This will help us build a house."""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


def build_floor(block_id, x, y, z, x_offset, z_offset):
    mc.setBlocks(x, y, z, x + x_offset, y, z + z_offset, block_id)


def build_wall(block_id2, x, y, z, x_offset, y_offset, z_offset):
    mc.setBlocks(x, y, z, x + x_offset, y + y_offset, z + z_offset, block_id2)


def build_stairs(block_id3, x, y, z, x_offset, y_offset, z_offset, num_stairs, direction=None):
    steps = 0
    while steps < num_stairs:
        mc.setBlock(x+steps, y+steps, z, block_id3)
        steps += 1


position = mc.player.getTilePos()
mc.postToChat(position)
"""# coordinates: -5013, -8, 6109
x = -5013
y = -8
z = 6109
mc.player.setTilePos(x, y, z)
a = x + 10
b = z - 10
c = x - 10
d = z + 10
print(a, b)
build_floor(4, a, y, b, -20, 30)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
# build_wall(0, a, y, b, -20, 3, 0)                 # Use this to clear a mistake
"""
"""# coordinates: -5258, -4, 6388
x = -5258
y = -4
z = 6388
build_wall(108, x-6, y+2, z+6, -3, 1, 3)"""
x = 6001
y = -9
z = -1314
build_stairs(108, x, y, z, 0, 0, 0, 10)
rc = 152
lc = 133
pc = 41
wall = [[rc, lc, pc, lc, lc, rc, pc, rc, pc],
        [rc, rc, rc, lc, lc, pc, lc, pc, pc],
        [rc, pc, rc, pc, rc, pc, lc, lc, lc],
        [lc, rc, lc, pc, lc, rc, pc, rc, pc]]
blah = 0
blah_blah = 0
while int(blah) <= 3:
    blah_blah = 0
    while int(blah_blah) <= 8:
        blockType = wall[blah][blah_blah]
        a = x+blah_blah
        b = y+blah
        print(blah, "   ", blah_blah)
        mc.setBlock(a, b, z, blockType)
        blah_blah += 1
    blah += 1
