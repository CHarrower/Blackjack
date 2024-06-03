import tkinter as tk 
from tkinter import font as tkFont 
from PIL import Image, ImageTk
import random


class GameScreen:
    def __init__(self, master, width=750, height=750):
        self.master = master
        self.master.geometry(f"{width}x{height}")
        self.frame = tk.Frame(master=self.master, width=width, height=height, bg="green")
        self.frame.pack()