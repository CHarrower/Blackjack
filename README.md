Blackjack Game

Welcome to the Blackjack Game! This project is a simple implementation of the popular card game Blackjack, built using Python and Tkinter for the graphical user interface.
Table of Contents

    Overview
    Installation
    Usage
    Game Rules
    Code Structure
    Screenshots
    Acknowledgements

Overview

The Blackjack Game provides an interactive interface where users can play the classic casino game against a computer dealer. The game follows the standard rules of Blackjack, with features such as hitting, standing, and automatic dealer play.
Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/blackjack-game.git

Navigate to the project directory:

bash

cd blackjack-game

Install the required dependencies:

Ensure you have Python installed on your machine. If not, download and install it from python.org.

Install Tkinter if it is not already installed. Tkinter is usually included with Python, but if you need to install it separately, you can use:

bash

sudo apt-get install python3-tk

Install Pillow for image handling:

bash

pip install pillow

Run the game:

bash

    python main.py

Usage

    Title Screen:
        Upon launching the game, you will see the title screen with the game title "Blackjack".
        Click the "Play" button to start the game.

    Game Screen:
        The game screen will display your cards, the dealer's cards, and buttons for game actions.
        You can choose to "Hit" to get another card or "Stand" to hold your total and end your turn.
        The game will then automatically handle the dealer's turn and determine the winner.

Game Rules

    Objective:
        The goal is to have a hand value as close to 21 as possible, without exceeding it.
        If your hand exceeds 21, you bust and lose the game.

    Card Values:
        Number cards (2-10) are worth their face value.
        Face cards (J, Q, K) are worth 10 points.
        Aces can be worth 1 or 11 points, whichever is more beneficial.

    Gameplay:
        Each player starts with two cards, with the dealer having one card face up and one card face down.
        Players can choose to "Hit" (take another card) or "Stand" (end their turn).
        The dealer must hit until their cards total 17 or higher.
        The player wins if their hand is closer to 21 than the dealer's hand, without going over 21.

Code Structure

    main.py: The main entry point for the game. It initializes the title screen and handles screen transitions.
    gamescreen.py: Contains the GameScreen class, which defines the main game interface and gameplay mechanics.
    gamelogic.py: Contains the GameLogic class, which handles the core game logic, such as drawing cards and calculating scores.
    titlescreen.py: Contains the TitleScreen class, which defines the title screen interface and functionality.

Screenshots

Here are some screenshots of the game:

Title Screen:
![screenshots /Screenshot 2024-06-17 at 13.53.18.png](<screenshots /Screenshot 2024-06-17 at 13.53.18.png>)

Game Screen:
![screenshots /Screenshot 2024-06-17 at 13.53.35.png](<screenshots /Screenshot 2024-06-17 at 13.53.35.png>)

(Ensure you have the screenshots saved in the screenshots folder within your project directory.)
Acknowledgements

    This project was inspired by the classic game of Blackjack.
    Thank you to the open-source community for providing resources and libraries that made this project possible.

Notes:

    Ensure that the image files for cards and buttons exist in the specified directories (main_cards and pix/button).
    The Pillow library is used for handling images. Make sure it is installed.
    Update the paths to the screenshots in the README if necessary.

Feel free to customize this README to better fit your project and add any additional information you think is necessary. Make sure to include the actual screenshots in the specified directory for the images to display correctly.