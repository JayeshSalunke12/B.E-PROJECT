import tkinter as tk
from tkinter import *
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

_label = tk.Label(text="Bbroccoli", width=85, font=("bold", 25), bg='black', fg='white')
_label.place(x=0, y=0)
_label = tk.Label(root, text="* Plant broccoli during the cool weather of early spring and fall. Grow it in containers or an in-ground garden.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-115, y=45)
_label = tk.Label(root, text="* Space broccoli plants according to the label (usually 18 inches apart). Choose a location with full sun, easy access to water, \n and fertile soil with a pH between 6.0 and 7.0 (amend soil with lime if necessary).", width=100, font=("bold", 18), bg='white', fg='black',justify=LEFT)
_label.place(x=-20, y=80)
_label = tk.Label(root, text="* Before planting, improve native soil by working in several inches of compost or other rich organic material.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-120, y=140)
_label = tk.Label(root, text="* Keep soil moist by giving broccoli plants 1 to 1.5 inches of water per week.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-293, y=180)
_label = tk.Label(root, text="* Make the most of your broccoli growing efforts by regularly feeding with a continuous-release plant food.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-130, y=220)
_label = tk.Label(root, text="* Lay down a thick layer of organic mulch made from finely ground leaves or bark to preserve soil moisture and prevent weeds.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-20, y=260)
_label = tk.Label(root, text="* Timing and temperature are critical for successful growth. The ideal growing temperature range is 65 to 80° F.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-100, y=300)
_label = tk.Label(root, text="* Harvest broccoli when the center crown is full of tiny, green, tightly-packed buds.", width=100, font=("bold", 18), bg='white', fg='black')
_label.place(x=-250, y=340)

_label = tk.Label(text="Onion", width=85, font=("bold", 25), bg='black', fg='white')
_label.place(x=0, y=400)
_label = tk.Label(root, text="* Soak the onion seeds in water for one day. Drain and keep them in the open for the next 2-3 days. Later, sow the seeds in the soil in a tray.", width=130, font=("bold", 18), bg='white', fg='black')
_label.place(x=-150, y=445)
_label = tk.Label(root, text="* The seeds take about 6-8 weeks to sprout. In the meanwhile, prepare the place where you intend to sow the saplings. It could be your balcony,\n backyard or a grow bag. You will need fertilisers to nourish the plant. ", width=170, font=("bold", 18), bg='white', fg='black',justify=LEFT)
_label.place(x=-410, y=485)
_label = tk.Label(text="* Monitor the saplings on the tray. Water regularly to ensure the soil is moist to facilitate growth. Once the saplings in your tray sprout, plant them\n in the demarcated space.", width=140,font=("bold", 18), bg='white', fg='black',justify=LEFT)
_label.place(x=-200,y=550)
_label = tk.Label(root, text="* The seeds take about 6-8 weeks to sprout. In the meanwhile, prepare the place where you intend to sow the saplings. It could be your balcony,\n backyard or a grow bag. You will need fertilisers to nourish the plant. ", width=170, font=("bold", 18), bg='white', fg='black',justify=LEFT)
_label.place(x=-410, y=485)

root.mainloop()