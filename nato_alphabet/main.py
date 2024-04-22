import pandas #import pandas module

def nato_convert(): #function contains the program to make recursion easier
    name = input("What word do you need to spell?").upper() #obtain the word to spell and convert to upper case

    new_list = [letter for letter in name] #create a list from the letters in the word


    nato_data = pandas.read_csv("nato_alphabet.csv") #read from nato alphabet csv file
    nato_data_dict = nato_data.set_index('Letter')['Word'].to_dict() #convert the data into a dictionary with the letters and words as key value pairs

    try:
        nato_list = [nato_data_dict[letter] for letter in new_list] #create a list of nato words for each letter in the given word

    except KeyError: #error handling
        print("Sorry, only letters in the alphabet please!")
        nato_convert()
    else:
        print(nato_list) #print the list

        repeat = input("translate another word?[y/n]").lower() #ask user if they want to go again
        if repeat == "y": #if yes, call the function again
            nato_convert()

nato_convert() #initial function call