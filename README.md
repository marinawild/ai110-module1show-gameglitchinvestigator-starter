# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   This is a number guessing game where the game has a selected number chosen already and the user must try and guess the number.
   The range is between 1 and 100 and the user has a predetermined number of guesses (in this case 8) are allowed. 
   The user can allow for hints to help in guessing and can choose to start a new game, if desired.
- [ ] Detail which bugs you found.
   Some bugs I discovered are that it allows for input less than 1 and greater than 100.
   It also always says to guess lower even when the minimum value (1) is reached.
   Lastly, if the game is lost of unfinished, it does not allow for a new game to be started when you click, "New Game" button.
   When the correct asnwer is input, it works, but then went a new game is started the submit guess, button does not work.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
