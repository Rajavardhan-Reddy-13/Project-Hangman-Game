# 🎮 Hangman Game in Python with Tkinter — Full Code Explanation

This is a fully functional **Hangman Game** implemented in Python using the **Tkinter GUI library**. The game provides an interactive interface where a player can guess the letters of a randomly selected word. The game visually represents incorrect guesses by progressively updating a **hangman image**. The player can restart the game at any time using a **New Game** button.

---

## 🚀 How the Code Works — Full Flow Explanation

### 1️⃣ Importing Modules

The code imports:
- `tkinter` and `messagebox` for GUI and popup dialogs
- `random` to randomly select the word
- `ascii_uppercase` to create buttons for A-Z letters automatically

---

### 2️⃣ Main Window Setup

- `window = Tk()` creates the main window.
- The window title is set to `"Hangman"`.
- The window is made non-resizable.
- The game loads a predefined list of words (`word_list`).

---

### 3️⃣ Hangman Images

- The game loads **12 images**:
  - hang0.png → empty gallows (start of game)
  - hang1.png to hang11.png → hangman progressively drawn
- These images are stored in the `photos` list.
- The image updates based on the number of wrong guesses.

---

### 4️⃣ Global Variables Used

- `numberOfGuesses`: Tracks how many wrong guesses have been made.
- `the_word_withSpaces`: Stores the current word, but with spaces between letters (example: `'H A N G M A N'`).
- `lblWord`: A `StringVar()` used to display the current state of the guessed word (underscores and/or correct letters).

---

### 5️⃣ Starting a New Game — `newGame()`

When the player starts a new game (at app launch or by clicking **New Game** button), the following happens:

- `numberOfGuesses` is reset to 0.
- The first image (empty gallows) is displayed.
- A random word is selected from `word_list`.
- `the_word_withSpaces` is created by adding spaces between each letter of the word.
- The display (`lblWord`) is set to show the same number of underscores (with spaces), e.g. `"_" "_" "_" "_" ...`.

---

### 6️⃣ The Guess Function — `guess(letter)`

When the player clicks any **A-Z button**, this function runs:

- If `numberOfGuesses < 11` (still have attempts left):
  - The code compares the clicked letter (`letter`) with `the_word_withSpaces`.
  - If the letter is in the word:
    - All matching positions in `lblWord` are updated to show the correct letter.
    - If the player has completed the word (all letters revealed), a popup is shown saying `"You guessed it!"` and a new game starts.
  - If the letter is not in the word:
    - `numberOfGuesses` is incremented.
    - The hangman image is updated to the corresponding stage.
    - If `numberOfGuesses == 11` → player has lost → `"Game over"` popup is shown.

---

### 7️⃣ Display Components

#### Image Label

- `imgLabel` displays the current hangman image.
- It updates after every wrong guess.

#### Word Display

- `lblWord` is a `StringVar()` displayed in a large bold label.
- Initially shows underscores.
- As correct letters are guessed, those positions are filled with the correct letter.

---

### 8️⃣ Letter Buttons (A-Z)

- The code uses a **loop over `ascii_uppercase`** to create 26 buttons.
- Each button:
  - Has the corresponding letter as its label.
  - Calls `guess(c)` with that letter when clicked.
- The buttons are placed on the grid in 3 rows.

---

### 9️⃣ New Game Button

- Clicking this button calls `newGame()`, resetting the game.

---

### 10️⃣ Main Loop

- `newGame()` is called once initially to start the game.
- Finally, `window.mainloop()` starts the Tkinter event loop to keep the window open and responsive.

---

## 🔄 Summary of Game Flow

1️⃣ A random word is selected and displayed as underscores `_ _ _`.  
2️⃣ The player clicks letter buttons (A-Z) to guess letters of the word.  
3️⃣ If the guessed letter is correct → it is revealed in the word display.  
4️⃣ If the guessed letter is incorrect → the hangman image progresses one step.  
5️⃣ The player wins if all letters are correctly guessed → "You guessed it!" popup.  
6️⃣ The player loses if 11 wrong guesses are made → "Game Over" popup.  
7️⃣ The player can start a new game anytime by clicking the **New Game** button.  
8️⃣ The game window runs continuously until the player closes the window (mainloop). 
