from mcpi.minecraft import Minecraft
import stevetest as st
mc = Minecraft.create()

location_or_maybe_not = input("Do you want to find your location?(y/n)")
if location_or_maybe_not == "y":
    position = mc.player.getTilePos()
    mc.postToChat(position)
    x = position.x
    y = position.y
    z = position.z
else:
    pass
crater_or_possibly_nothing = input("Do you want to clear the area?(y/n)")
if crater_or_possibly_nothing == "y":
    x_offset = 20
    y_offset = 150
    z_offset = 20
    st.clear_area(x+1, y, z+1, x_offset, y_offset, z_offset)
else:
    pass

grass_floor_or_floor = input("Do you want a floor?(y/n)")
if grass_floor_or_floor == "y":
    st.build_floor(x, y, z, x_offset, y_offset, z_offset, 123)
else:
    pass
y_offset = 4
unprotected_or_protected = input("Would you like some walls?(y/n)")
if unprotected_or_protected == "y":
    st.build_walls(x, y, z, x_offset, y_offset, z_offset, 7, 2)
