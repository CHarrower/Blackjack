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
        self.card_values = self.load_card_values()

        self.dealer_frame = tk.Frame(master=self.frame, bg="green")
        self.dealer_frame.place(x=50, y=50)

        self.player_frame = tk.Frame(master=self.frame, bg="green")
        self.player_frame.place(x=50, y=605)

        self.dealer_cards = []
        self.player_cards = []

        self.back_of_card_p = "main_cards/back/back_4.png"
        self.back_of_card_img = Image.open(self.back_of_card_p).convert("RGBA").resize((55, 66))
        self.back_of_card_phot = ImageTk.PhotoImage(self.back_of_card_img)

        self.dealer_total_label = tk.Label(master=self.frame, text="Dealer: 0", bg="green", font=("Attomic", 40))
        self.dealer_total_label.place(x=50, y=115)

        self.player_total_label = tk.Label(master=self.frame, text="Player: 0", bg="green", font=("Attomic", 40))
        self.player_total_label.place(x=50, y=555)

        self.player_points_label = tk.Label(master=self.frame, text="Points: 1000", bg="green", font=("Attomic", 40))
        self.player_points_label.place(x=50, y=675)

        self.play_again_button = None
        self.current_image_index = [0]
        self.play_again_images = [
            ImageTk.PhotoImage(Image.open("pix/button/Button_White (4).png").resize((200, 50))),
            ImageTk.PhotoImage(Image.open("pix/button/Button_White (5).png").resize((200, 50)))
        ]

        self.player_total = 0
        self.dealer_total = 0
        self.show_cards()
        self.hit_button = None
        self.stand_button = None
        self.create_hit_stand_buttons()

    # LOAD CARD IMAGES
    def load_card_images(self, directory, extension):
        card_images = []
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                 card_images.append(os.path.join(directory, filename))
        return card_images
    
    # LOAD CARD VALUES
    def load_card_values(self):
        card_values = {}
        for filename in os.listdir("main_cards"):
            if filename.endswith(".png"):
                card_name = filename.split(".")[0]
                value = self.get_card_value(card_name)
                card_values[os.path.join("main_cards", filename)] = value
        return card_values
    
    # GET CARD VALUE
    def get_card_value(self, card_name):
        parts = card_name.split("_")
        if len(parts) != 2:
            raise ValueError(f"Unexpected card name format: {card_name}")

        value_str = parts[1]

        if value_str in ['J', 'Q', 'K']:
            return 10
        elif value_str == 'A':
            return 11
        else:
            return int(value_str)
    
    # SHOW RANDOM CARD
    def show_random_card(self, frame, faceup=True):
        if faceup:
            random_card_path = random.choice(self.card_images)
            card_image = Image.open(random_card_path).convert("RGBA").resize((55, 66))
            card_photo = ImageTk.PhotoImage(card_image)
            card_value = self.card_values[random_card_path]
        else:
            card_photo = self.back_of_card_phot
            card_value = 0

        card_label = tk.Label(master=frame, image=card_photo, bg="green", bd=0)
        card_label.photo = card_photo
        card_label.pack(side=tk.LEFT)
        return card_label, card_value
    
    # SHOW CARDS
    def show_cards(self):
        # Show dealer's cards
        self.show_random_card(self.dealer_frame, faceup=False)
        _, value = self.show_random_card(self.dealer_frame, faceup=True)
        self.dealer_total += value

        # Show player's cards
        _, value = self.show_random_card(self.player_frame, faceup=False)
        self.player_total += value
        _, value = self.show_random_card(self.player_frame, faceup=True)
        self.player_total += value
        self.update_totals()
    
    # CREATE HIT AND STAND BUTTONS
    def create_hit_stand_buttons(self):
        # Image paths for button states
        hit_image_paths = ["pix/button/Button_White (8).png", "pix/button/Button_White (1).png"]
        stand_image_paths = ["pix/button/Button_Dark (8).png", "pix/button/Button_Dark (1).png"]

        # Check if the image paths are correct and files exist
        for path in hit_image_paths + stand_image_paths:
            if not os.path.exists(path):
                print(f"Image not found: {path}")

        # Button coordinates
        h_button_x, h_button_y = 544, 350
        s_button_x, s_button_y = 645, 350

        # Text coordinates
        h_text_x, h_text_y = 553, 295
        s_text_x, s_text_y = 631, 295

        # Create button animations
        self.hit_button = self.create_button_animation(hit_image_paths, h_button_x, h_button_y, self.hit_action, h_text_x, h_text_y, "Hit")
        self.stand_button = self.create_button_animation(stand_image_paths, s_button_x, s_button_y, self.stand_action, s_text_x, s_text_y, "Stand")
    
    # CREATE BUTTON ANIMATION
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

        button = tk.Label(master=self.frame, image=photo_list[0], bg="green", bd=0, cursor="pointinghand")
        button.place(x=x, y=y)
        button.bind("<Button-1>", button_clicked)
        button.photo_list = photo_list  # Keep a reference to prevent garbage collection

        label = tk.Label(master=self.frame, text=text, bg="green", font=("Attomic", 45))
        label.place(x=text_x, y=text_y)
        
        return button  # Return the button widget
    
    # UPDATE TOTALS
    def update_totals(self):
        self.player_total_label.config(text=f"Player: {self.player_total}")
        self.dealer_total_label.config(text=f"Dealer: {self.dealer_total}")
        self.check_game_over()
    
    # HIT ACTION
    def hit_action(self, event):
        print("Hit button pressed")
        _, value = self.show_random_card(self.player_frame, faceup=True)
        self.player_total += value
        self.update_totals()
    
    # STAND ACTION
    def stand_action(self, event):
        print("Stand button pressed")
        self.play_dealer_turn()
    
    # DEALER TURN
    def play_dealer_turn(self):
        if self.dealer_total < 17:
            _, value = self.show_random_card(self.dealer_frame, faceup=True)
            self.dealer_total += value
            self.update_totals()
            self.master.after(1000, self.play_dealer_turn)  # Delay of 1 second between dealer hits
        else:
            self.check_game_over(player_standing=True)
    
    # CHECK GAME OVER
    def check_game_over(self, player_standing=False):
        if self.player_total == 21:
            print("Player wins with 21!")
        elif self.player_total > 21:
            print("Player busts!")
            self.show_win_screen("Dealer wins!")
        elif self.dealer_total > 21:
            print("Dealer busts! Player wins!")
            self.show_win_screen("Player wins!")
        elif player_standing:
            if self.dealer_total > self.player_total:
                print("Dealer wins!")
                self.show_win_screen("Dealer wins!")
            elif self.dealer_total < self.player_total:
                print("Player wins!")
                self.show_win_screen("Player wins!")
            else:
                print("It's a tie!")
                self.show_win_screen("It's a tie!")

    # SHOW WIN SCREEN
    def show_win_screen(self, winner_text):
        # Hide hit and stand buttons
        self.hit_button.place_forget()
        self.stand_button.place_forget()

        # Display the winner text
        winner_label = tk.Label(master=self.frame, text=winner_text, bg="green", font=("Attomic", 45))
        winner_label.place(x=50, y=350)

        # Define play_again_clicked and reset_play_again_image here
        current_image_index = [0]

        def play_again_clicked(event):
            current_image_index[0] = (current_image_index[0] + 1) % len(self.play_again_images)
            play_again_button.config(image=self.play_again_images[current_image_index[0]])
            play_again_button.after(100, reset_play_again_image)

        def reset_play_again_image():
            current_image_index[0] = 0
            play_again_button.config(image=self.play_again_images[current_image_index[0]])

        play_again_button = tk.Button(master=self.frame, image=self.play_again_images[0], bd=0, command=self.reset_game, bg="green")
        play_again_button.place(x=50, y=450)
        play_again_button.bind("<Button-1>", play_again_clicked)

 # RESET GAME
    
    def reset_game(self):
        print("Resetting game...")
        # Clear dealer and player cards from the screen
        dealer_children = self.dealer_frame.winfo_children()
        player_children = self.player_frame.winfo_children()
        for card_label in dealer_children:
            card_label.destroy()
        for card_label in player_children:
            card_label.destroy()

        # Reset dealer and player total values to 0
        self.dealer_total = 0
        self.player_total = 0
        self.dealer_total_label.config(text="Dealer: 0")
        self.player_total_label.config(text="Player: 0")

        # Show new cards for the dealer and the player
        self.show_cards()

        # Hide the play again button
        self.play_again_button.place_forget()




# MAIN FUNCTION
if __name__ == "__main__":
    win = tk.Tk()
    app = GameScreen(win)
    win.mainloop()

