from mcpi.minecraft import Minecraft
import stevetest as st
import minecraft_coordinates as minecoor
mc = Minecraft.create()

saved_location_or_maybe_not = input("Do you want to save your location?(y/n) ")
if saved_location_or_maybe_not == "y":
    position = mc.player.getTilePos()
    mc.postToChat(position)
    x = position.x
    y = position.y
    z = position.z
    description = input("What is your location name? ")
    minecoor.save_coordinates(description, x, y, z)
else:
    travel_to_saved_location_or_maybe_not = input("Do you want to travel to a previous location?(y/n) ")
    if travel_to_saved_location_or_maybe_not == "y":
        description = input("Which location would you like to travel to? ")
        df = minecoor.get_coordinates(description)
        print(df)
        x = int(df.loc["x_coord"])
        y = int(df.loc["y_coord"])
        z = int(df.loc["z_coord"])
        mc.player.setTilePos(x, y, z)
        quit()
crater_or_possibly_nothing = input("Do you want to clear the area?(y/n) ")
if crater_or_possibly_nothing == "y":
    x_offset = 20
    y_offset = 150
    z_offset = 20
    st.clear_area(x+1, y, z+1, x_offset, y_offset, z_offset)
else:
    pass

grass_floor_or_floor = input("Do you want a floor?(y/n) ")
if grass_floor_or_floor == "y":
    st.build_floor(x, y, z, x_offset, y_offset, z_offset, 123)
else:
    pass
y_offset = 4
unprotected_or_protected = input("Would you like some walls?(y/n)")
if unprotected_or_protected == "y":
    st.build_walls(x, y, z, x_offset, y_offset, z_offset, 7, 2)
