import tkinter as tk 
from PIL import Image, ImageTk
import random
import os

class GameScreen:
    def __init__(self, master, width=750, height=750):
        self.master = master
        self.master.geometry(f"{width}x{height}")
        self.frame = tk.Frame(master=self.master, width=width, height=height, bg="green")
        self.frame.pack()

        self.card_images = self.load_card_images("main_cards", ".png")

        self.faceup_card_label = tk.Label(master=self.frame, bg="green", bd=0)
        self.faceup_card_label.place(x=100, y=50)

        self.back_of_card_p = "main_cards/back_4.png"
        self.back_of_card_img = Image.open(self.back_of_card_p).convert("RGBA").resize((45, 56))
        self.back_of_card_phot = ImageTk.PhotoImage(self.back_of_card_img)

        self.back_of_card_label = tk.Label(master=self.frame, bg="green", bd=0)
        self.back_of_card_label.place(x=50, y=50)

        self.show_cards()

    def load_card_images(self, directory, extension):
        card_images = []
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                 card_images.append(os.path.join(directory, filename))
        return card_images

    def show_random_faceup(self):
        random_card_path = random.choice(self.card_images)
        card_image = Image.open(random_card_path).convert("RGBA").resize((45, 56))
        card_photo = ImageTk.PhotoImage(card_image)
        self.faceup_card_label.config(image=card_photo)
        self.faceup_card_label.image = card_photo

    def show_back_of_card(self):
        self.back_of_card_label.config(image=self.back_of_card_phot)
        self.back_of_card_label.image = self.back_of_card_phot

    def show_cards(self):
        self.show_random_faceup()
        self.show_back_of_card()

if __name__ == "__main__":
    win = tk.Tk()
    app = GameScreen(win)
    win.mainloop()
