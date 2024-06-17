from titlescreen import TitleScreen
from gamescreen import GameScreen
import tkinter as tk 

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Main function
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():
    win = tk.Tk()
    title_app = TitleScreen(win, title="Blackjack")
    title_app.on_play_button_clicked = lambda: show_game_screen(win)
    win.mainloop()

def show_game_screen(master):
    master.withdraw()  # Hide the title screen window
    game_win = tk.Toplevel(master)
    game_screen = GameScreen(game_win)
    game_win.protocol("WM_DELETE_WINDOW", lambda: close_game_screen(master, game_win))

def close_game_screen(master, game_win):
    game_win.destroy()
    master.deiconify()  # Show the title screen window again
#------------------------------------------------------------------------------------------------------------->
if __name__ == "__main__":
    main()

