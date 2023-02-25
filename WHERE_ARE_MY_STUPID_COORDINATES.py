"""You shall never get lost... as long as you have your STUPID COORDINATES"""
from mcpi.minecraft import Minecraft
import pandas as pd
import os
mc = Minecraft.create()
coord_file = "coordinates_file.csv"


def list_coordinate_names():
    if os.path.isfile(coord_file):
        df = pd.read_csv(coord_file)
        names = df.coord_description
        print(names)
        return df
    else:
        print(f"The {coord_file} is missing. Please get your eyes checked.")
        exit()


def return_coordinates():
    data_frame = list_coordinate_names()
    while True:
        coordinate_name = input("What is your randomé coordinate name?(CaSE SenSITIvE)")
        if coordinate_name in data_frame.values:
            coordinates = get_coordinates(coordinate_name, data_frame)
            x = coordinates._get_value(0, "x_coord")
            y = coordinates._get_value(0, "y_coord")
            z = coordinates._get_value(0, "z_coord")
            position = [coordinates.x_coord, coordinates.y_coord, coordinates.z_coord]
            mc.player.setTilePos(position)
            return x, y, z


def get_coordinates(coordinate_names, a_df):
    coordinates = a_df.loc[a_df.coord_description == coordinate_names]
    coordinates.reset_index(inplace=True)
    return coordinates


if __name__ == "__main__":
    data_frame = list_coordinate_names()
    while True:
        coordinate_name = input("What is your randomé coordinate name?(CaSE SenSITIvE)")
        if coordinate_name in data_frame.values:
            coordinates = get_coordinates(coordinate_name, data_frame)
            print(coordinates)
            position = [coordinates.x_coord, coordinates.y_coord, coordinates.z_coord]
            mc.player.setTilePos(position)
            exit()





    # position = mc.player.getTilePos()
    # mc.postToChat(position)
