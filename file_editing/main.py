# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
import os
# Specify the file path
desktop_path = r"C:\Users\Eli\Desktop"

# Write to a new file
with open(os.path.join(desktop_path, "my_file.txt"), mode="w") as file:
    file.write("New Text")

# Read from the same file
with open(os.path.join(desktop_path, "my_file.txt"), mode="r") as file:
    contents = file.read()
    print(contents)