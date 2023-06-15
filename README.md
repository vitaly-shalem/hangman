# Hangman (The game)
Solo one day project @ BeCode: ARAI 5

## Description

### Objective
Gain practical knowledge about Python OOP programming.

### Goal
Build a Terminal version of **Hangman** game. 

### Approach
- First thing first, convince yourself not to pannick. This way or another everything going to be just fine!
- Once calmed down, start working...
- Break the project to smaller tasks and build it task by task.
- Learn while doing, because it's the best learning.
- Once you have a stable working version, push to *main* and tag.
- Keep improving, but don't for get to work on a branch to keep stable version clean.
- Stable again, go *main* and tag.

## Game logic
- A random word is selected from the list of available words and presented to a player with undescores representing each letter.
- A player is asked to enter a letter:
    - Only A-Z letter can be accepted,
    - If a player enters a wrong character or more than one character, the question is repeated,
    - If a player enters a letter that has been played already, a message is presented and the question is repeated.
- A letter enterred is checked in the list of the letters that construct this word:
    - If a letter entered by a player does not appear in the word, a meesage stating that the guess was *wrong* appears,
    - If a letter entered appears in the word, a meesage stating that the guiess was *right* appears,
    - The *word* is presented again:
        - In case any letters guessed right, they appear in the right positions,
        - The intro message is adjusted to the situation:
            - *You haven't guessed any letters* in case of no correct guesses,
            - *You guessed these letters correctly* in case of at leas one correct guess.
        - If all letters are guessed correctly, the game stops and the winning message is presented.
    - The list of wrongly guessed letters is presented,
    - Player's status message is presented with:
        - Number of played turns,
        - Total number of turns available (a.k.a *lives*),
        - Number of errors made so far.
- At the end of each turn, if a player guessed at leas one letter correctly, he is presented with an option to guess the whole word:
    - A player has a choice to continue without taking this attemp or try to guess the whole word,
    - If a player guesses correctly, the game is over and the *winning* message is presented,
    - Else the game continues, if and only if any turns left.
- If a player runs out of turns, the *loosing* message is presented.
- The *winning* message present the **word** and the game summary:
    - Total number if turns used,
    - Total number of errors made.
- Please note! When a player fails to guess the whole word, it doesn **not** count as an error.

## Installation
The gameto be played in Terminal:
- Comand line
- Power Shell
- Git Bash
Anything works!

Just make sure you have Python v3.6 or higher installed on your machine.

## Usage
- Open Terminal.
- Move to the project directory.
- Run *python main.py*
- Enjoy the game!

## Timeline
- The first working version has to be submitted end of the day 2023-06-14.
- The final version to be submitted on 2023-06-15.

## Personal
This project is part of BeCode's **AI Bootscamp** training, group **ARAI 5**.
