# #file not found
# try:
#     file =  open("a_file.txt")
#     # key error
#     new_dict = {"key":"value"}
#     value = new_dict["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise KeyError("This is an error i made up")
#key error
# new_dict = {"key":"value"}
# value = new_dict["non_existent_key"]

#index error
# fruit_list = ["banana","apple","orange"]
# print(fruit_list[3])

#type error
# text = "abc"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 metres")

bmi = weight / height **2
print(f"BMI: {bmi}")
