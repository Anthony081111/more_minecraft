"""Creates a cycle of blocks starting at block id 0"""
from mcpi.minecraft import Minecraft
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord

mc = Minecraft.create()

coordinates = whereCoord.return_coordinates()
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
mc.player.setTilePos(x, y, z)

keep_going = True
current_id = int(input("What is your starting id?"))
while keep_going:
    x = x+2
    mc.setBlock(x, y, z, current_id)
    current_id += 1
    stop = input("Keep going?(n to stop)")
    if stop == "n":
        keep_going = False