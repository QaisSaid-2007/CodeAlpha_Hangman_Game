# 🎮 Hangman Game — Python OOP Project

A console-based **Hangman word-guessing game** built in Python using Object-Oriented Programming (OOP), abstract base classes, Pandas for data handling, and Matplotlib for visualizing player performance.

---

## 📖 Project Overview

This project is a fully playable command-line Hangman game that supports multiple difficulty levels, a hint system, a grading/scoring system per mode, persistent results saved to a CSV file, and visual statistics for each player. It was developed as part of a Python programming internship to demonstrate practical use of OOP, abstract classes, data handling with Pandas, and data visualization with Matplotlib.

---

## 🎯 Purpose of the Project

The purpose of this project is to:

- Build a complete, playable Hangman game in Python.
- Demonstrate clean Object-Oriented design with abstract base classes.
- Practice real-world data handling using Pandas DataFrames.
- Persist game results between sessions using CSV files.
- Visualize player statistics using Matplotlib charts.
- Apply type hints, encapsulation, and polymorphism throughout the codebase.

---

## 🕹️ Game Modes

The game offers three difficulty levels. Each mode has its own number of attempts, its own hangman drawing progression, and its own grading formula.

### 🟢 Easy Mode
- **Attempts:** 6
- **Hints:** 3
- **Word length:** Mostly 4-letter words
- **Grading formula:**
  ```
  grade = 10 - (attempts_used × 0.25) - (hints_used × 1) - (5 if failed)
  ```
- **Final score:** `(grade / 10) × 100` → percentage

### 🟡 Medium Mode
- **Attempts:** 4
- **Hints:** 3
- **Word length:** Mostly 5-letter words
- **Grading formula:**
  ```
  grade = 10 - (attempts_used × 0.5) - (hints_used × 1) - (5 if failed)
  ```
- **Final score:** `(grade / 10) × 100` → percentage

### 🔴 Hard Mode
- **Attempts:** 3
- **Hints:** 3
- **Word length:** Mostly 6-letter words
- **Grading formula:**
  ```
  grade = 10 - (attempts_used × 1) - (hints_used × 1) - (4 if failed)
  ```
- **Final score:** `(grade / 10) × 100` → percentage

### 📊 Mode Comparison Table

| Mode   | Attempts | Hints | Penalty per Wrong Attempt | Penalty per Hint | Fail Penalty |
|--------|----------|-------|---------------------------|------------------|--------------|
| Easy   | 6        | 3     | 0.25                      | 1.0              | 5.0          |
| Medium | 4        | 3     | 0.50                      | 1.0              | 5.0          |
| Hard   | 3        | 3     | 1.00                      | 1.0              | 4.0          |

---

## 🧮 Scoring System

Each game ends with a **score out of 100%** and a **PASS/FAIL status**.

- The base grade starts at **10.00**.
- Penalties are subtracted based on attempts used, hints used, and whether the word was guessed.
- The final grade is normalized to a percentage: `(grade / 10) × 100`.
- The status is **PASS** if the word was guessed, otherwise **FAIL**.

---

## 📁 Complete Project Structure

```
hangman-game/
│
├── hangman.py                  # Main game engine and entry point
├── Results.py                  # Results storage and visualization
├── blueprint.py                # Abstract base classes (blueprints)
├── Hangman_Results_table.csv   # Saved game results (auto-generated)
└── README.md                   # Project documentation
```

---

## 📂 File Descriptions

### 🕹️ `hangman.py`
The **main engine** of the game. This file contains:

- **`Data`** — builds the word database (words + hints) and assigns each word a difficulty based on its length.
- **`Game`** — loads the database and displays the game intro and rules.
- **`Mode`** — parent class for all difficulty levels. Handles shared logic:
  - Tracking guessed letters
  - Giving hints
  - Picking a random word
  - Drawing the hangman stages
- **`Easy`**, **`Medium`**, **`Hard`** — subclasses of `Mode`, each with its own attempts, grading formula, and hangman drawing.
- **`main()`** — runs the full game loop: username input → mode selection → play → save result → replay/show results/quit.

**Run this file to play the game.**

---

### 📊 `Results.py`
Handles everything related to **player results**:

- **`Results_Table`** class that:
  - Creates a Pandas DataFrame with columns: `Username, Mode, grade, hints_used, attempts_used, is_word_guessed`
  - `add_new_row()` — adds a new game result
  - `load_results()` — loads saved results from the CSV file
  - `save_results()` — saves results back to the CSV
  - `show_results()` — plots a **bar chart** (scores per test) and a **pie chart** (mode distribution) for a given player

---

### 🧩 `blueprint.py`
The **abstract blueprint** of the project. Defines abstract base classes that enforce structure:

- `abst_Game` — contract for the game intro
- `abst_Mode` — contract for game modes (intro, grading, hangman output)
- `abst_Data` — contract for the game database
- `abst_Results_Table` — contract for saving, loading, and showing results

Acts as the **skeleton** that other files must follow.

---

### 🗂️ `Hangman_Results_table.csv`
The **persistent results file**. Every game result is appended here, so data survives between sessions.

**Columns:**
```
Username, Mode, grade, hints_used, attempts_used, is_word_guessed
```

**Example rows:**
```
Qais,Easy,90.0,1,0,True
Said,Medium,75.0,2,1,True
Lebron,Hard,0.0,3,3,False
```

---

### 📘 `README.md`
This documentation file. It explains the purpose, structure, gameplay, technologies, and concepts demonstrated in the project.

---

## 🛠️ Technologies Used

| Technology    | Purpose                                                        |
|---------------|----------------------------------------------------------------|
| **Python 3**  | Core programming language                                      |
| **Pandas**    | DataFrames for word database and results storage               |
| **Matplotlib**| Bar and pie charts for player statistics                       |
| **CSV**       | Lightweight persistent storage for game results                |
| **ABC module**| Abstract base classes for enforcing structure                  |

### Python
The primary language. Handles game logic, OOP structure, and user interaction.

### Pandas
Used for:
- Building the word database (`Data.game_table()`)
- Filtering words by mode
- Storing and manipulating the results table

### Matplotlib
Used for:
- A **bar chart** showing scores per test
- A **pie chart** showing the distribution of modes played

### CSV
Used to **persist** results between sessions. The file is auto-created and updated after every game.

---

## 🎮 How the Game Works

### Game Flow
1. The game starts and displays the intro and rules.
2. The player enters a **username**.
3. The player selects a **mode** (Easy / Medium / Hard).
4. A countdown runs before the game starts.
5. The game picks a **random word** from the selected mode's word pool.
6. The player guesses letters one at a time, or types `HINT` to receive a hint.
7. The hangman is drawn progressively for each wrong guess.
8. The game ends when the word is guessed or attempts run out.
9. The score is calculated and the result is saved.
10. The player can **play again**, **view results**, or **quit**.

### Gameplay Explanation
- Each correct letter is revealed in the word.
- Each wrong letter costs one attempt and draws one part of the hangman.
- Hints are limited to **3 per game** and each hint costs **1 point**.
- The player wins by guessing all unique letters in the word before attempts run out.

### Results Storage
- After every game, the result dictionary is passed to `Results_Table.add_new_row()`.
- The result is appended to the DataFrame and saved to `Hangman_Results_table.csv`.
- On startup, `load_results()` reads the CSV back into memory.

### Data Visualization
- The player can choose **Show Results** after a game.
- A **bar chart** displays the player's scores across all their tests.
- A **pie chart** shows the distribution of modes they played.

### Data Stored in the CSV
| Column            | Description                                  |
|-------------------|----------------------------------------------|
| `Username`        | Player's name                                |
| `Mode`            | Easy / Medium / Hard                         |
| `grade`           | Final score as a percentage                  |
| `hints_used`      | Number of hints used in the game             |
| `attempts_used`   | Number of wrong attempts made                |
| `is_word_guessed` | True if the player guessed the word, else False |

---

## 🧠 Main Python Concepts Demonstrated

- **OOP** — Classes for `Game`, `Mode`, `Data`, `Results_Table`, etc.
- **Inheritance** — `Easy`, `Medium`, `Hard` inherit from `Mode`.
- **Abstract Classes** — `blueprint.py` uses `ABC` and `@abstractmethod`.
- **Encapsulation** — Private attributes like `self.__DataBase` in `Game`.
- **Type Hints** — Used extensively across functions and methods.
- **Pandas** — DataFrames for the word database and results.
- **Matplotlib** — Bar and pie charts for visualization.
- **File Handling** — Reading/writing CSV with `pd.read_csv` and `to_csv`.
- **Randomization** — `random.randint` picks a random word.
- **Exception Handling** — `try/except FileNotFoundError` when loading results.
- **Match/Case** — Modern Python pattern matching for mode and stage selection.
- **Static Methods** — Used for the `grading_system` in each mode.

---

## 🎬 Example Gameplay

```
********** Hangman Game **********
** Hello and welcome to the Hangman Game please read the game instructions carefully **

Hangman is a word-guessing game where you have to guess a hidden word one letter at a time
How to play:
1: A secret word is chosen.
2: You guess one letter at a time.
3: If the letter is in the word, it will be revealed.
4: If the letter is incorrect, you lose one attempt.
5: Use the available hints if you get stuck.
6: Guess the complete word before you run out of attempts!

Before starting the game please enter your name to save your game results
Username: Qais
Welcome Qais
Enter 1 -> Easy or 2 -> Medium or 3 -> Hard
Game Mode: 1

********** Easy Mode **********
attempts: 6
Hints: 3
Game starts on 5...
Game starts on 4...
Game starts on 3...
Game starts on 2...
Game starts on 1...

********** HANGMAN GAME - EASY MODE - GAME ON **********
Enter (HINT) for a hint otherwise enter your letter: HINT
-> I am a fruit.
***** HINTS LEFT: 2 *****
Enter (HINT) for a hint otherwise enter your letter: A
-> Correct choice WELL DONE !!!
_ A _ _ _
***** HINTS LEFT: 2 *****
***** CHANCES LEFT: 6 *****

********** SCORE REPORT & CALCULATIONS **********
***** Username: Qais *****
***** Hints used: 1 *****
***** Attempts used: 0 *****
>>>>> SCORE = 90.0%   status = PASS <<<<<
```

---

## ⚙️ Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hangman-game.git
   cd hangman-game
   ```

2. **Install required libraries:**
   ```bash
   pip install pandas matplotlib
   ```

3. **Ensure all project files are in the same directory:**
   - `hangman.py`
   - `Results.py`
   - `blueprint.py`

---

## ▶️ How to Run the Project

Run the main game file:

```bash
python hangman.py
```

Follow the on-screen prompts to:
- Enter your username
- Choose a game mode
- Play the game
- View your results as charts

---

## 🎓 Learning Outcomes

By building this project, the following skills were developed:

- Designing software using **Object-Oriented Programming**.
- Using **abstract classes** to enforce structure across modules.
- Handling structured data with **Pandas DataFrames**.
- Persisting data with **CSV files**.
- Visualizing data with **Matplotlib**.
- Writing clean, typed, and modular Python code.
- Structuring a multi-file Python project.

---

## 🚀 Future Improvements

- Add a **GUI** using Tkinter or PyQt.
- Add **more word categories** and larger datasets.
- Add **online leaderboard** support with a database.
- Add **sound effects** and animations.
- Implement **multiplayer** mode.
- Allow **custom word lists** loaded from user files.
- Add **unit tests** for all classes.
- Package the game as an **executable** with PyInstaller.

---

## 👤 Author

**Developed as part of a Python Programming Internship Project.**

This project demonstrates practical application of Python OOP, abstract classes, Pandas, Matplotlib, and CSV file handling in a complete, playable game. It is intended as a learning portfolio piece showcasing clean code structure and modular design.

---

## 📜 License

This project is open-source and free to use for educational purposes.
