from mcpi.minecraft import Minecraft
import walls_floors_and_ceilings_that_are_really_floors as wfac
import minecraft_coordinates as minecoor
import WHERE_ARE_MY_STUPID_COORDINATES as whereCoord
mc = Minecraft.create()

coordinates = whereCoord.return_coordinates()
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
x += 1
z += 1

crater_or_possibly_nothing = input("Do you want to clear the area?(y/n) ")
x_offset = 20
y_offset = 150
z_offset = 20
if crater_or_possibly_nothing == "y":
    wfac.clear_area(x, y, z, x_offset, y_offset, z_offset)
else:
    pass

grass_floor_or_floor = input("Do you want a floor?(y/n) ")
if grass_floor_or_floor == "y":
    x_offset = 20
    y_offset = -1
    z_offset = 20
    wfac.build_floor(x, y, z, x_offset, y_offset, z_offset, 123)  # 123 is a redstone lamp(unlit)
else:
    pass
y_offset = 4
unprotected_or_protected = input("Would you like some walls?(y/n)")
if unprotected_or_protected == "y":
    wfac.build_walls(x, y, z, x_offset, y_offset, z_offset, 7, 2)  # 7 is a bed in a rock, 2 does nothing

struck_by_lightening_or_maybe_not = input("Would you like a ceiling that is really just a floor?(y/n)")
if struck_by_lightening_or_maybe_not == "y":
    wfac.build_floor(x, y, z, x_offset, y_offset, z_offset, 179)  # 179 is red sandstone
