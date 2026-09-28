# 🎮 Hangman Game - Python Internship Project

## 📌 Project Overview

This project is a **Hangman word-guessing game** developed in Python as part of my Python programming internship.

The player must guess a hidden word one letter at a time. The game includes **three difficulty levels**, hints, a grading system, result storage, and graphical result visualization.

The project was designed to practice and demonstrate Python programming concepts such as:

- Object-Oriented Programming (OOP)
- Inheritance
- Abstract Classes
- Encapsulation
- Type Hints
- Python Data Structures
- Pandas
- DataFrames
- CSV files
- Random selection
- Matplotlib
- Exception Handling
- Basic Data Visualization

---

## 🎯 Purpose of the Project

The main purpose of this project is to create an interactive Hangman game while applying Python programming concepts in a practical project.

The project also keeps track of the player's performance, including:

- Username
- Game mode
- Score
- Hints used
- Attempts used
- Whether the word was successfully guessed

The stored results can then be displayed and visualized using charts.

---

## 🎮 Game Modes

The game has three difficulty levels:

| Mode | Attempts | Hints |
|------|----------|-------|
| Easy | 6 | 3 |
| Medium | 4 | 3 |
| Hard | 3 | 3 |

Each mode also has its own grading system.

### Easy Mode

The player starts with **6 attempts**.

Each incorrect attempt reduces the score by `0.25`.

### Medium Mode

The player starts with **4 attempts**.

Each incorrect attempt reduces the score by `0.5`.

### Hard Mode

The player starts with **3 attempts**.

Each incorrect attempt reduces the score by `1`.

Using a hint also reduces the score.

---

## 🧩 Project Structure

```text
Hangman-Project/
│
├── Hangman.py
├── Results.py
├── blueprint.py
├── Hangman_Results_table.csv
└── README.md
