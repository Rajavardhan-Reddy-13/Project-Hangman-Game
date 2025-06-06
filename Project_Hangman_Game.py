# Import required modules
from tkinter import messagebox        # For showing message popups (win/lose)
from tkinter import *                 # Import all tkinter classes (for GUI)
import random                         # For selecting random word from list
from string import ascii_uppercase    # For getting list of A-Z uppercase letters

# Setting up the main game window
window = Tk()                         # Initialize the Tkinter window
window.title("Hangman")               # Set the window title
window.resizable(0, 0)                # Disable window resizing

# List of possible words for the game
word_list = ['VAMPIREDIARIES','THEORIGINALS','GAMEOFTHRONES','MONEYHEIST','THEFAMILYMAN','STRANGERTHINGS','PEAKYBLINDERS']

# Load hangman images to show progress (12 images for 12 stages)
photos = [PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang0.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang1.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang2.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang3.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang4.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang5.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang6.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang7.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang8.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang9.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang10.png"),
          PhotoImage(file="C:/Users/sreed/OneDrive/Pictures/hang11.png")]

# Function to start a new game
def newGame():
    global the_word_withSpaces        # Declare global variables for word and guesses
    global numberOfGuesses
    numberOfGuesses = 0               # Reset number of wrong guesses
    imgLabel.config(image=photos[0])  # Reset image to first (empty gallows)
    
    # Select a random word from the word list
    the_word = random.choice(word_list)
    
    # Create a version of the word with spaces between each letter (for display purposes)
    the_word_withSpaces = " ".join(the_word)
    
    # Set lblWord variable to show underscores (_) for each letter
    lblWord.set(" ".join("_" * len(the_word)))

# Function to handle when player guesses a letter
def guess(letter):
    global numberOfGuesses            # Use global numberOfGuesses variable
    if numberOfGuesses < 11:          # Allow only up to 11 wrong guesses (12 images)
        
        # Convert current displayed word and correct word into lists
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        
        # If guessed letter is in the word
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):                 # Loop through each letter
                if txt[c] == letter:                   # If letter matches, reveal it
                    guessed[c] = letter
            lblWord.set("".join(guessed))              # Update displayed word
            
            # If player has guessed all letters correctly (no more '_')
            if lblWord.get() == the_word_withSpaces:
                messagebox.showinfo("Hangman", "You guessed it!")  # Show success message
                newGame()                             # Start a new game
        else:
            numberOfGuesses += 1                      # Increase number of wrong guesses
            imgLabel.config(image=photos[numberOfGuesses])  # Update image
            
            # If reached max number of wrong guesses → Game Over
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game over")   # Show Game Over message

# Create label to show current hangman image
imgLabel = Label(window)               # Create empty Label for image
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)  # Place image label in grid
imgLabel.config(image=photos[0])       # Set initial image to hang0.png

# Create StringVar to store/display the word with underscores or correct letters
lblWord = StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
# Display lblWord on the right of the image, large bold font

# Create buttons for all letters A-Z
n = 0                                  # Initialize button counter
for c in ascii_uppercase:              # Loop through A-Z letters
    # Create a Button for each letter:
    # text=c → button shows letter A-Z
    # command=lambda c=c: guess(c) → when clicked, call guess(c)
    # font → set font style/size
    # width=4 → button width
    
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1 + n // 9, column=n % 9)
    
    n += 1                             # Move to next button position

# Create button to start a new game (New Game button)
Button(window, text="New\nGame", command=lambda: newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")
# The button is multi-line ("New\nGame") and is placed in row 3 column 8
# sticky="NSWE" → button expands to fill cell

# Start first game automatically
newGame()

# Start Tkinter main event loop
window.mainloop()
# Keeps the window running and responsive to user interaction
