import tkinter as tk
from PIL import Image, ImageTk

class EndGameScreen(tk.Frame):
    def __init__(self, master, winner_text, play_again_callback):
        super().__init__(master)
        self.master = master
        self.configure(bg="green")
        self.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self, text=winner_text, font=("Arial", 24), bg="green")
        label.pack(pady=20)

        self.play_again_images = [
            ImageTk.PhotoImage(Image.open("pix/button/Button_White (4).png").resize((200, 50))),
            ImageTk.PhotoImage(Image.open("pix/button/Button_White (5).png").resize((200, 50)))
        ]

        self.play_again_button = tk.Button(self, image=self.play_again_images[0], bd=0, command=play_again_callback, bg="green")
        self.play_again_button.pack()

        self.animate_button()

    def animate_button(self, idx=0):
        idx = (idx + 1) % 2
        self.play_again_button.config(image=self.play_again_images[idx])
        self.after(500, self.animate_button, idx)

# If you want to run this module separately, you can include this part:

if __name__ == "__main__":
     win = tk.Tk()
     endgame = EndGameScreen(win, "Player Wins!")
     win.mainloop()
