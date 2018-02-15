import datetime
import time

"""Script for resolve the section 7 exercise"""

file_One = open("/home/walberth/Downloads/Python/Section7_Exercise/file1.txt", 'r')
file_Two = open("/home/walberth/Downloads/Python/Section7_Exercise/file2.txt", 'r')
file_Three = open("/home/walberth/Downloads/Python/Section7_Exercise/file3.txt", 'r')

data = [file_One.readline(), file_Two.readline(), file_Three.readline()]

fileName = str(datetime.datetime.now().strftime("%Y-%m-%d")) + ".txt"

with open("/home/walberth/Downloads/Python/Section7_Exercise/" + fileName, 'a+') as new_file:
    new_file.seek(0)
    for string in data:
        new_file.write(string + "\n")

file_One.close()
file_Two.close()
file_Three.close()
new_file.close()




