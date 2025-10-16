# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python. You will practice string manipulation, loops, conditionals, and random selection while learning how to manage game state and interact with users.

## 📝 Tasks

### 🛠️	Hangman Game Implementation

#### Description
Create a Hangman game where the player tries to guess a hidden word by suggesting letters, with a limited number of incorrect guesses allowed.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (at least 10 words)
- Accept letter guesses from the user and display current progress (e.g., `_ a _ _ m a n`)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts are exhausted
- Display appropriate win or lose messages

**Example Input/Output:**
```plaintext
Word: _ a _ _ m a n
Guess a letter: g
Incorrect guesses left: 4
Word: h a n g m a n
Congratulations! You won!
```

### 🛠️	Word List Setup

#### Description
Prepare a list of words for the Hangman game. The game should randomly select one word from this list at the start.

#### Requirements
Completed program should:

- Include a list of at least 10 words
- Randomly choose a word for each new game
- Ensure words are not revealed until correctly guessed
