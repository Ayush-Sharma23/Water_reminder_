import pygame as py
import csv
import tkinter as tk
import pytz
from datetime import datetime
import time


#INITIALIZING PYGAME
py.init()

#CREATE IST TIMEZONE
IST = pytz.timezone('Asia/Kolkata')

#MAIN LOOP
main_loop = tk.Tk()

#TITLE
main_loop.title('WATER REMINDER')

#LABELS
message = tk.Label(main_loop ,
                   compound = tk.CENTER,
                   text = "Drink your water",
                   fg="black",
                   # bg="dark green",
                   font="Helvetica 30 bold"
                   )
message.pack(fill = 'x')

Date_label = tk.Label(main_loop , fg = "red",
                   font = ("Calibri", 10 , "bold"),
                      bg = "black")
Date_label.pack()


Time_label = tk.Label(main_loop , fg = "red",
                      bg = "black",
                   font = ("Copperplate Gothic" , 10 , "bold"))
Time_label.pack()


#REAL-TIME DATE AND TIME CLOCK
def update_clock():
    ts = datetime.now(IST)
    date_now = ts.strftime("%d %b %Y")
    time_now = ts.strftime("%H:%M:%S")
    Date_label.config(text = date_now)
    Time_label.config(text = time_now)
    Time_label.after(1000 , update_clock)

update_clock()

#calling this function will play the alert audio
def alert():
    py.mixer.music.load(r'C:\Users\ayush\PycharmProjects\healthyprog\alert.wav')
    py.mixer.music.play(-1)

# define the countdown func.
def countdown(t):
    while t > 0:
        main_loop.update()
        time.sleep(1)
        t -= 1

    alert()

def if_click():
    #stop audio when button is clicked
    py.mixer.music.stop()

    #Recording Date and time
    data = [Date_label['text'] , Time_label['text']]

    #Entering date and time data in a csv file
    with open('fileformain.csv', 'a', newline='') as f:
        csv_w = csv.writer(f , delimiter = ',')
        csv_w.writerow(data)
    print("LOG ENTERED SUCCESSFULLY")
    #Count down will start again after clicking the button
    countdown(3600)

#Clicking the button will start the countdown after 3600 seconds i.e one hour
def if_start():
    countdown(3600)


#BUTTONS
Drank_button = tk.Button(main_loop , text = "Click if Drank" , command = if_click)
Drank_button.pack(side = "bottom")

start_button = tk.Button(main_loop , text = "START" ,
                         fg = 'red', command = if_start)
start_button.pack(side = "bottom")


#Executing loop
main_loop.mainloop()

