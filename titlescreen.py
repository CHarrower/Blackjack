import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk
from gamescreen import GameScreen

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
# TITLE SCREEN CLASS
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
class TitleScreen:
    def __init__(self, master, width=750, height=750, title="Blackjack"):
        self.master = master
        self.master.geometry(f"{width}x{height}")
        self.master.title(title)
        
        self.frame = tk.Frame(master=self.master, width=width, height=height, bg="green")
        self.frame.pack()
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # TITLE 
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
       
        self.create_title("BLACKJACK", "Attomic", 50)
        self.create_title_cards(["main_cards/Clubs_card_Q.png", "main_cards/Hearts_card_08.png"])
        self.create_play_button_animation(["pix/Icons/Icon_Shadow (4).png", "pix/Icons/Icon_Dark (4).png"])

   
    def create_title(self, text, font_use, font_size):
        custom_font = tkFont.Font(family=font_use, size=font_size)
        title = tk.Label(self.master, text=text, font=custom_font, fg="white", bg="green")
        title.place(x=280, y=250)
    #------------------------------------------------------------------------------------------------------------->
    
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # TITLE CARDS POSITION AND ROTATION
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def create_title_cards(self, title_cards):
        card_images = [Image.open(path).convert("RGBA").resize((45, 56)) for path in title_cards]
        rotation_angles = [-20, 20]
        rotated_cards = [image.rotate(angle, expand=True) for image, angle in zip(card_images, rotation_angles)]
        self.card_photo_list = [ImageTk.PhotoImage(image) for image in rotated_cards]

        self.card_label1 = tk.Label(master=self.frame, image=self.card_photo_list[0], bg="green", bd=0)
        self.card_label1.place(x=217, y=250)

        self.card_label2 = tk.Label(master=self.frame, image=self.card_photo_list[1], bg="green", bd=0)
        self.card_label2.place(x=453, y=250)
    #------------------------------------------------------------------------------------------------------------->
    
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # PLAY BUTTON ANIMATION
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def create_play_button_animation(self, image_paths):
        images = [Image.open(path).convert("RGBA").resize((40, 40)) for path in image_paths]
        self.photo_list = [ImageTk.PhotoImage(image) for image in images]
        self.current_image_index = 0

        self.label = tk.Label(master=self.frame, image=self.photo_list[self.current_image_index], bg="green", bd=0, cursor="pointinghand")
        self.label.place(x=350, y=350)
        self.label.bind("<Button-1>", self.button_clicked)

    def button_clicked(self, event):
        self.current_image_index = (self.current_image_index + 1) % len(self.photo_list)
        self.label.config(image=self.photo_list[self.current_image_index])
        self.label.after(100, self.reset_image)
        

    def reset_image(self):
        self.current_image_index = 0
        self.label.config(image=self.photo_list[self.current_image_index])
        self.game_screen()
    #------------------------------------------------------------------------------------------------------------->

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # GAME SCREEN
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def game_screen(self):
        self.frame.pack_forget()
        game_screen = GameScreen(self.master)
     #------------------------------------------------------------------------------------------------------------->

if __name__ == "__main__":
    win = tk.Tk()
    app = TitleScreen(win)
    win.mainloop()
