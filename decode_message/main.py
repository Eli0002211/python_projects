
def decode(message_file):
    # create a dictionary from each number and word as key value pairs
    with open(message_file, "r") as file:
        words = file.readlines()
    word_dict = {}
    for word in words:
        key = word.split()[0]
        value = word.split()[1]
        word_dict[key] = value


    # sort the keys numerically and put them into a list
    nums = []
    for word in word_dict:
        nums.append(word)
    nums = sorted(nums, key=int)

    # create the pyramid of keys
    step = 1
    pyramid = []
    while len(nums) != 0:
        if len(nums) >= step:
            pyramid.append(nums[0:step])
            nums = nums[step:]
            step += 1

    # create a message from the value for the last key in each row of the pyramid
    message = ""
    for row in pyramid:
        word = word_dict[row[-1]]
        message += f"{word} "
    return message

decoded_message = decode(message_file="coding_qual_input.txt")
print(decoded_message)

