"""this module contains functions to read or write minecraft coordinates in coordinates_file.cvs"""

"""pandas is a Python package providing fast, flexible, and expressive data structures 
designed to make working with “relational” or “labeled” data both easy and intuitive. """
from mcpi.minecraft import Minecraft
import pandas as pd
import os
mc = Minecraft.create()

def save_coordinates(description, x, y, z):
    # This function saves a description of the coordinates and the coordinates
    coord_file = "coordinates_file.csv"

    # test to see if file exists
    if os.path.isfile(coord_file):
        # file exists so read the file into a pandas data frame
        df = pd.read_csv(coord_file)

        # file exists so check if the description already exists in this file before saving the data

        # Create a dictionary from the function attributes then convert the dictionary to a pandas data frame
        new_data = {"coord_description": description, "x_coord": [x], "y_coord": [y], "z_coord": [z]}
        df_cur_record = pd.DataFrame(new_data)

        # The following code compares the description in coord_file to the new description (in the dictionary)
        # A data frame is returned with a True or False for each line in coord_file that is compared
        test_df = df["coord_description"] == new_data["coord_description"]

        if test_df.any():                        # this is true if there is at least one True in test_df
            print(f"{new_data['coord_description']} already exists in the csv file")
            txt = input('do you want to change the description of this set of coordinates? (y/n):  ')
            if txt == 'y':
                txt = input('Enter a new description:  ')
                df_cur_record['coord_description'] = txt
                df = df.append(df_cur_record)
                df.to_csv(coord_file, index=False)
                return
            else:
                txt = input('do you want to replace the old description data? (y/n):  ')
                if txt == 'y':
                    # delete the old data line
                    mask = df['coord_description'] == description
                    df = df[~mask]
                    df.to_csv(coord_file, index=False)
                    # insert new data
                    df = df.append(df_cur_record)
                    df.to_csv(coord_file, index=False)
                    return
        else:
            df = df._append(df_cur_record)
            df.to_csv(coord_file, index=False)
            return

    # else if file does not exist create the file and save the first set of coordinates
    else:
        # Create a dictionary from the function attributes then convert the dictionary to a pandas data frame
        dict = {'coord_description': [description], 'x_coord': [x], 'y_coord': [y], 'z_coord': [z]}
        df = pd.DataFrame(dict)
        print("line 57(which won't happen b/c 20 errors XD)   ", df)
        df.set_index('coord_description', inplace=True)
        print("line 59(which won't happen b/c 20 errors ;])   ", df)
        df.to_csv(coord_file, index=True)
        return


if __name__ == '__main__':
    # Find the coordinates of the player
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    txt = input('Provide a description of this location:    ')
    save_coordinates(txt, x, y, z)
