
# Square Game

## Introduction
Square Game is a simple yet addictive game built using Pygame. In this game, you control a rectangle that moves around the screen, consuming edible squares to grow in size. However, beware of the poisonous squares that will shrink your rectangle if eaten. The goal is to grow your rectangle large enough to win the game while avoiding shrinking to a critical size.

## Installation
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/square-game.git
   cd square-game
Install the required Python packages:
Ensure you have Python and pip installed. Then, install the required packages using:
bash
Copy code
pip install pygame
Run the Game:
bash
Copy code
python square_game.py
How to Play
Your objective is to move the rectangle around the screen to consume edible squares (green) while avoiding poisonous squares (purple).
As you eat edible squares, your rectangle will grow larger. Eating poisonous squares will shrink your rectangle.
Controls
W/A/S/D: Move the rectangle up, left, down, or right.
Spacebar: Change the color of the rectangle.
M: Change the background color.
K: Shrink the rectangle slightly.
1: Increase the movement speed.
2: Decrease the movement speed.
ESC: Quit the game.
Winning and Losing
Win: If your rectangle grows larger than 150x225 pixels, you win the game. A victory message will appear, and you can press the down arrow key to play again.
Lose: If your rectangle shrinks below 20x30 pixels, you lose the game. A defeat message will appear, and you can press the down arrow key to play again.
