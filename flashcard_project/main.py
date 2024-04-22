#----------------------------------------------CONSTANTS---------------------------------------------------------------#
import json
from json import JSONDecodeError

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_COLOR = "#FFFFFF"
CARD_BACK_COLOR = "#91C2AF"
FONT =["Arial",40,"bold"]
games_up = 0
#----------------------------------------------IMPORTS-----------------------------------------------------------------#
from tkinter import *
import pandas
from random import choice
#----------------------------------------------FLASHCARD DATA----------------------------------------------------------#
flashcard_data = pandas.read_csv(r".\data\french_words.csv")
flashcard_dict = flashcard_data.set_index('French')['English'].to_dict()
flashcard_list = list(flashcard_dict.keys())
flashcard_choice = choice(flashcard_list)
def choose_flashcard():
    global games_up
    global flashcard_choice
    global flashcard_translation
    global right_button
    global wrong_button
    global timer
    flashcard_list = list(flashcard_dict.keys())
    flashcard_choice = choice(flashcard_list)
    flashcard_translation = flashcard_dict[flashcard_choice]
    try:
        with open(r".\data\flashcards.json", "r") as file:
            memorised_data = json.load(file)

    except JSONDecodeError:
        pass
    except FileNotFoundError:
        pass
    else:
        for key in memorised_data:
            if key == flashcard_choice:
                try:
                    choose_flashcard()
                except RecursionError:
                    word.itemconfig(word_text,text="You have\n memorized all items!")
                    games_up += 1


def memorised_flashcard():
    new_data = {flashcard_choice:flashcard_translation}
    try:
        with open(r".\data\flashcards.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except JSONDecodeError:
        with open(r".\data\flashcards.json", "w") as file:
            json.dump(new_data, file, indent=3)
    except FileNotFoundError:
        with open(r".\data\flashcards.json", "w") as file:
            json.dump(new_data, file, indent=3)
    else:
        with open(r".\data\flashcards.json", "w") as file:
            json.dump(data, file, indent=3)
    finally:
        card_reset()
#----------------------------------------------COUNTDOWN---------------------------------------------------------------#
def count_down():
    global timer_id
    timer_id = window.after(4000, card_flip)
#-----------------------------------------------CARD FLIP--------------------------------------------------------------#
def card_flip():
    global word
    global word_text
    global card_front
    global card_back
    global games_up
    canvas.create_image(400,280,image=card_back)
    if games_up > 0:
        word.itemconfig(word_text, text="You have\n memorized all items!")
    else:
        word.itemconfig(word_text,text=f"English:\n\n{flashcard_translation.title()}")
    word.config(bg=CARD_BACK_COLOR)

def card_reset():
    global word
    global word_text
    global card_back
    global card_front
    global timer_id
    global games_up
    canvas.create_image(400,280,image=card_front)
    choose_flashcard()
    if games_up > 0:
        word.itemconfig(word_text, text="You have\n memorized all items!")
    else:
        word.itemconfig(word_text,text=f"French:\n\n{flashcard_choice.title()}")
    word.config(bg=CARD_FRONT_COLOR)
    window.after_cancel(timer_id)
    count_down()
#-------------------------------------------------UI SETUP-------------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.minsize(width=900,height=680)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file=r".\images\card_front.png")
card_back = PhotoImage(file=r".\images\card_back.png")
canvas.create_image(400,280,image=card_front)
canvas.grid(column=0,row=0,columnspan=2)

word = Canvas(width=600, height=300, highlightthickness=0, bg=CARD_FRONT_COLOR)
word_text = word.create_text(300,100,text=f"French:\n\n{flashcard_choice.title()}",font=FONT)
word.grid(column=0,row=0,columnspan=2)


#------------------------------------------------BUTTONS---------------------------------------------------------------#
right_image = PhotoImage(file=r".\images\right.png")
right_button = Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=memorised_flashcard)
right_button.grid(column=1,row=1)

wrong_image = PhotoImage(file=r".\images\wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=card_reset)
wrong_button.grid(column=0,row=1)

#---------------------------------------------INITIATE-----------------------------------------------------------------#
choose_flashcard()
count_down()
window.mainloop() #keep screen open