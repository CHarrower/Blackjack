import tkinter as tk 
from PIL import Image, ImageTk
import random
import os

class GameScreen:
    def __init__(self, master, width=750, height=750):
        self.master = master
        self.width = width
        self.height = height
        self.master.geometry(f"{width}x{height}")
        self.frame = tk.Frame(master=self.master, width=width, height=height, bg="green")
        self.frame.pack()

        self.card_images = self.load_card_images("main_cards", ".png")

        self.dealer_frame = tk.Frame(master=self.frame, bg="green")
        self.dealer_frame.place(x=50, y=50)

        self.player_frame = tk.Frame(master=self.frame, bg="green")
        self.player_frame.place(x=50, y=605)

        self.dealer_cards = []
        self.player_cards = []

        self.back_of_card_p = "main_cards/back_4.png"
        self.back_of_card_img = Image.open(self.back_of_card_p).convert("RGBA").resize((55, 66))
        self.back_of_card_phot = ImageTk.PhotoImage(self.back_of_card_img)

        self.show_cards()
        self.create_hit_stand_buttons()

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # LOAD CARD IMAGES
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def load_card_images(self, directory, extension):
        card_images = []
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                 card_images.append(os.path.join(directory, filename))
        return card_images
    #------------------------------------------------------------------------------------------------------------->
    

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # SHOW RANDOM CARD
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def show_random_card(self, frame, faceup=True):
        if faceup:
            random_card_path = random.choice(self.card_images)
            card_image = Image.open(random_card_path).convert("RGBA").resize((55, 66))
            card_photo = ImageTk.PhotoImage(card_image)
        else:
            card_photo = self.back_of_card_phot

        card_label = tk.Label(master=frame, image=card_photo, bg="green", bd=0)
        card_label.photo = card_photo
        card_label.pack(side=tk.LEFT)
        return card_label
    #------------------------------------------------------------------------------------------------------------->


    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # SHOW CARDS
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def show_cards(self):
        # Show dealer's cards
        self.show_random_card(self.dealer_frame, faceup=False)  
        self.show_random_card(self.dealer_frame, faceup=True)  

        # Show player's cards
        self.show_random_card(self.player_frame, faceup=False)  
        self.show_random_card(self.player_frame, faceup=True)  
    #------------------------------------------------------------------------------------------------------------->


    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # CREATE HIT AND STAND BUTTONS
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def create_hit_stand_buttons(self):
        # Image paths for button states
        hit_image_paths = ["pix/button/Button_White (8).png", "pix/button/Button_White (1).png"]
        stand_image_paths = ["pix/button/Button_Dark (8).png", "pix/button/Button_Dark (1).png"]

        # Check if the image paths are correct and files exist
        for path in hit_image_paths + stand_image_paths:
            if not os.path.exists(path):
                print(f"Image not found: {path}")

        # Button coordinates
        h_button_x, h_button_y = 544, 500
        s_button_x, s_button_y = 645, 500

        # Text coordinates
        h_text_x, h_text_y = 553, 560
        s_text_x, s_text_y = 631, 560

        # Create button animations
        self.create_button_animation(hit_image_paths, h_button_x, h_button_y, self.hit_action, h_text_x, h_text_y, "Hit")
        self.create_button_animation(stand_image_paths, s_button_x, s_button_y, self.stand_action, s_text_x, s_text_y, "Stand")
    #------------------------------------------------------------------------------------------------------------->


    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # CREATE BUTTON ANIMATION
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def create_button_animation(self, image_paths, x, y, action, text_x, text_y, text):
        images = [Image.open(path).convert("RGBA").resize((60, 60)) for path in image_paths]
        photo_list = [ImageTk.PhotoImage(image) for image in images]
        current_image_index = [0]

        def button_clicked(event):
            current_image_index[0] = (current_image_index[0] + 1) % len(photo_list)
            button.config(image=photo_list[current_image_index[0]])
            button.after(100, reset_image)
            action(event)

        def reset_image():
            current_image_index[0] = 0
            button.config(image=photo_list[current_image_index[0]])

        button = tk.Label(master=self.frame, image=photo_list[0], bg="green", bd=0)
        button.place(x=x, y=y)
        button.bind("<Button-1>", button_clicked)
        button.photo_list = photo_list  # Keep a reference to prevent garbage collection

        label = tk.Label(master=self.frame, text=text, bg="green", font=("Attomic", 45))
        label.place(x=text_x, y=text_y)
    
    #------------------------------------------------------------------------------------------------------------->

    
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # HIT ACTION
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def hit_action(self, event):
        # Print statement for debugging
        print("Hit button pressed")
    #------------------------------------------------------------------------------------------------------------->


    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # STAND ACTION
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def stand_action(self, event):
        # Print statement for debugging
        print("Stand button pressed")
    #------------------------------------------------------------------------------------------------------------->


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
# MAIN FUNCTION
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    win = tk.Tk()
    app = GameScreen(win)
    win.mainloop()
#------------------------------------------------------------------------------------------------------------->
