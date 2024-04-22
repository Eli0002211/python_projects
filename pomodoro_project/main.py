# --------------------------import modules-------------------------------#
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Courier",40,"bold")
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #
def button_reset():
    global reps
    global timer_id
    window.after_cancel(timer_id)
    canvas.itemconfig(tomato_text, text="00:00")
    timer.itemconfig(timer_text, text="Timer", fill=PINK)
    reps = 0
    reset_checkmark()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        reset_checkmark()
        timer.itemconfig(timer_text, text="Work", fill=RED)
        count_down(work_sec)
    elif reps % 7 == 0:
        timer.itemconfig(timer_text, text="Break",fill=GREEN)
        count_down(long_break_sec)
        add_checkmark()
    elif reps % 2 == 0:
        timer.itemconfig(timer_text, text="Work",fill=RED)
        count_down(work_sec)
    else:
        timer.itemconfig(timer_text, text="Break",fill=GREEN)
        count_down(short_break_sec)
        add_checkmark()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer_id
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = (f"0{count_min}")
    count_sec = count % 60
    if count_sec < 10:
        count_sec = (f"0{count_sec}")
    canvas.itemconfig(tomato_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_id = window.after(1000, count_down, count -1)
    if count == 0:
        reps += 1
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk() #window setup
window.title("Pomodoro")
window.minsize(400,400)
window.config(padx=60,pady=20,bg=YELLOW)

canvas = Canvas(width=203,height=224,bg=YELLOW,highlightthickness=0) #tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
tomato_text = canvas.create_text(103, 150, text="00:00", font=FONT, fill="white")
canvas.grid(column=1,row=1)

timer = Canvas(width=203,height=100,bg=YELLOW,highlightthickness=0) #timer display
timer_text = timer.create_text(103,50,text="Timer",font=FONT,fill=PINK)
timer.grid(column=1,row=0)

start_button = Button(text="Start",command=start_timer) #start button
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=button_reset) #reset button
reset_button.grid(column=2,row=2)

checkmark = Canvas(width=203,height=60,bg=YELLOW,highlightthickness=0) #checkmarks
checkmark_text = "✔ "

#-------------------------------------add checkmarks-----------------------------------#
def add_checkmark():
    global reps
    global checkmark
    global checkmark_text
    if reps == 1:
        check_xcor = 80
    if reps == 3:
        check_xcor = 100
    if reps == 5:
        check_xcor = 120
    if reps == 7:
        check_xcor = 140
    checkmark.create_text(check_xcor,30,text=checkmark_text,font=("Courier",12,"bold"),fill="GREEN")
    checkmark.grid(column=1,row=2)

#-------------------------------------remove all checkmarks--------------------------------#
def reset_checkmark():
    global checkmark
    checkmark.delete("all")


window.mainloop() #keep display open