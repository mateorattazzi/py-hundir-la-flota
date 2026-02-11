# Py Hundir la Flota


Final project for the first programming course  
Degree in Mathematical Engineering and Artificial Intelligence


## Description
This project is a Python implementation of the classic game *Hundir la flota* (Battleship).
Two players place their ships on a board and take turns shooting at the opponent’s board.
The winner is the first player to sink all opponent ships.


The game is played in the terminal and includes input validation, turn management,
and clear visualization of the game boards.


## Features
- Modular design with multiple Python files
- Variable number of ships chosen by the user
- Ship placement with orientation (horizontal or vertical)
- Input validation using custom exceptions
- Turn repetition when a ship is hit
- End-of-game detection and final board display


## Project structure
- `main.py` – Entry point of the program
- `estructura_del_juego.py` – Game flow and turn logic
- `funciones_juego.py` – Shooting logic and win conditions
- `funciones_inicializacion.py` – Board creation and ship placement
- `funciones_mostrar.py` – Board visualization in the terminal
- `constantes.py` – Game constants
- `errores.py` – Custom exception definitions
- `test.py` – Test cases for core functionality


## How to run
Make sure you have Python installed.  
Run the game from the terminal with:


```bash
python main.py

Follow the on-screen instructions to place ships and play the game.

Author

Mateo Rattazzi Aranda
