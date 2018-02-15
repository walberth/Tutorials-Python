r"""
This script creates an empty file
"""
import datetime

filename = datetime.datetime.now().strftime("%d-%m-%Y")

#  Create empty file
def create_file():
    r""" This function an empty file """
    with open(str(filename) + ".txt", "w") as file:
        file.write("")  # Writing empty string

create_file()