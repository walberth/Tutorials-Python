file = open("/home/walberth/Downloads/Python/PythonFIle_Handling.txt", 'r')
print(type(file))

content = file.read()  #  Get the lines in that file
print(content)

file.seek(0)

content_v2 = file.readlines()
print(content_v2)

content_v2 = [i.rstrip("\n") for i in content_v2]
print(content_v2)

file_fruits = open("/home/walberth/Downloads/Python/fruits.txt", 'r')

fruits = file_fruits.readlines()
for line in fruits:
    print(len(line.strip()))

new_file = open("new_file.txt", 'w')
lines = ["walberth", "felipe", "gutierrez", "telles"]
for item in lines:
    new_file.write(item + "\n")
new_file.close()

new_file_two = open("new_file_two.txt", 'w')
numbers = [1, 2, 3, 4]
for num in numbers:
    new_file_two.write(str(num) + "\n")
new_file_two.close()

#  Appending new line in file
new_file_two = open("new_file_two.txt", 'a')
new_file_two.write("5")
new_file_two.close()

# r -> Opens a file for reading only. The file pointer is placed at the beginning of the line. Default mode.
    # new_file_two = open("new_file_two.txt", 'r')
# r+ -> Opens a file for reading and writing. The file pointer is placed at the beginning of the line.
    # new_file_two = open("new_file_two.txt", 'r+')
# w -> Opens a file for writing. Overrides the file if exists, if not create a new one
    # new_file_two = open("new_file_two.txt", 'w')
# w+ -> Opens a file for writing and reading. Overrides the file if exists, if not create a new one
    # new_file_two = open("new_file_two.txt", 'w+')
# a -> Opens a file for appending if exists, if not create a new one
    # new_file_two = open("new_file_two.txt", 'a')
# a+ -> Opens a file for appending and reading if exists, if not create a new one
    # new_file_two = open("new_file_two.txt", 'a+')

#  With for working with file without closed every time
with open("new_file_with.txt", 'a+') as file:
    file.seek(0)
    body = file.read()
    file.write("\nAnother line bitch")
