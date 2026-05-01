# Rock Paper Scissors Game

A simple Rock Paper Scissors web application built with **Python Flask**, HTML, CSS, and JavaScript.  
The player competes against the computer for 3 rounds, and the game shows the final winner based on points.

## Features

- Play Rock, Paper, Scissors in the browser.
- Computer chooses a random move.
- Score is tracked for both player and computer.
- Game runs for 3 rounds only.
- Final winner is declared after 3 rounds.
- Restart the game anytime.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

```
rock-paper-scissors/
│
├── app.py
├── RPS_Game.py    # this is extra file without frontend and you can run this individually. 
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## How It Works

1. The player clicks one of the buttons: Rock, Paper, or Scissors.
2. The computer randomly selects its move.
3. The winner of the round is decided.
4. Scores are updated on the screen.
5. After 3 rounds, the final result is shown.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install Flask

```bash
pip install flask
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

Go to:

```bash
http://127.0.0.1:5000/
```

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choices result in a tie

## Example Gameplay

- Player chooses: Rock
- Computer chooses: Scissors
- Result: Player wins the round

## Screenshot

Add a screenshot of your project here.

## Future Improvements

- Add sound effects
- Add animations
- Add difficulty levels
- Add multiplayer mode
- Save game history

## Author

Ketakshi Koshti
