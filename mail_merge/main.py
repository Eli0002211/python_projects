from random import randint

with open(file="names.txt",mode="r") as file:
    names = file.read().splitlines()

for name in names:
    desk_phone_password = randint(100000000,999999999)
    with open("email.txt","r") as file:
        contents = file.read()
        file_data = contents.replace("[Name]",name)
        file_data = file_data.replace("[password]",str(desk_phone_password))

    with open(f".\generated_emails\{name}_email.txt","w") as file:
        file.write(file_data)

