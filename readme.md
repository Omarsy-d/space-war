# Space War

**Space War** is a simple arcade-style space shooter game built using Python and the Turtle graphics library. Defend Earth by shooting down alien invaders before they reach the ground! Move your spaceship with the arrow keys and fire bullets with the spacebar.

## Game Overview

- **Objective:** Eliminate all alien invaders without letting them reach the bottom of the screen.
- **Controls:**
  - **Arrow keys:** Move the spaceship left and right.
  - **Spacebar:** Shoot bullets to eliminate enemies.
- **Game Over:** The game ends if an alien invader reaches the bottom of the screen or collides with your spaceship.

## Installation

### Requirements

- **Python**: Version 3.x installed on your computer
- **Turtle Graphics Library**: Pre-installed with Python

### Steps

1. **Clone or Download the Project:**

   Download or clone the project from your preferred location.

2. **Set Up Image Files**:

   You'll need to place images for the background, spaceship, and enemies at the following paths:

   - **Background Image**: `C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/background.gif`
   - **Spaceship Image**: `C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/spaceship.gif`
   - **Enemy Image**: `C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/invader2.gif`

   > **Note:** You can replace these images with your own, but be sure to update the paths in the code if needed.

3. **Run the Game**:

   Open a terminal, navigate to the project directory, and execute:

   ```bash
   python space_war.py
   ```

## Gameplay Instructions

1. **Move** your spaceship left or right using the **Arrow keys**.
2. **Fire** bullets using the **Spacebar** to hit enemies.
3. **Score Points** for each enemy you destroy.
4. Avoid collisions with enemies, and don't let any invader reach the ground!

## Code Explanation

The game is implemented using Python's Turtle module with the following core elements:

- **Game Setup**: The screen, background, and spaceship images are set, and instructions for gameplay are displayed.
- **Player Controls**: Functions for moving left and right and shooting bullets.
- **Enemy Movements**: Aliens move in a specific pattern and speed up when they reach screen edges.
- **Collisions**: Both player and enemies are checked for bullet and player collisions.
- **Score Tracking**: Increments score by 10 points for each enemy destroyed.

## Customization

- **Enemy Speed**: Modify `enemyspeed` in the code to adjust difficulty.
- **Bullet Speed**: Modify `bulletspeed` to change how fast the bullet moves.

---

### License

This project is open-source and can be modified or distributed under any terms you prefer.

---

Enjoy defending Earth in **Space War**!