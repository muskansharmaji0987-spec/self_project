# 📄 Project Statement — Flappy Bird Game (Python + Pygame)

## 1. Introduction
This project is a simple recreation of the classic **Flappy Bird** game, developed using the **Python Pygame** library.  
The game demonstrates fundamental concepts of 2D game development, including physics-based movement, event handling, real-time rendering, collision detection, and procedural obstacle generation.

---

## 2. Objective
The primary objective of the player is to control the movement of a bird and navigate it through a series of vertically aligned pipes without colliding.  
The player's score increases each time the bird successfully passes a pair of pipes.

---

## 3. Game Mechanics

### 3.1 Bird Movement
- The bird is represented by a simple rectangular `pygame.Rect` object.
- Gravity is applied continuously by increasing the bird’s vertical velocity (`bird_movement`).
- Pressing the **SPACE** key applies an upward force, simulating a flap.

### 3.2 Pipes
- Pipes are generated at fixed time intervals using a custom event (`SPAWNPIPE`).
- Each pipe pair consists of:
  - A top pipe of randomized height.
  - A bottom pipe placed at a fixed gap below the top pipe.
- Pipes move from right to left across the screen at constant speed.

### 3.3 Scoring
- A score point is awarded when the bird passes the left edge of a pipe pair.
- The program tracks the highest score achieved during the session.

### 3.4 Collision Detection
The game ends if:
- The bird collides with any pipe.
- The bird moves beyond the top or bottom boundaries of the game window.

---

## 4. Game Flow

### Active Gameplay State:
- Bird responds to gravity and player input.
- Pipes continuously move across the screen.
- Score counter updates in real-time.

### Game Over State:
- Gameplay stops immediately on collision.
- “Game Over” and high score are displayed.
- Pressing SPACE resets the game state, score, and pipes.

---

## 5. Technical Summary

### Libraries Used
- **pygame**: For rendering graphics, handling input, and managing game loops.
- **sys**: For clean program exit.
- **random**: For generating dynamic pipe heights.

### Important Variables
- `bird_movement`: Controls vertical velocity.
- `gravity`: Constant acceleration applied downward.
- `pipes`: List storing active pipe objects.
- `score` and `high_score`: Track player performance.

### Frame Rate
- The game runs at a stable **60 FPS** using `clock.tick(60)` for smooth animation.

---

## 6. Purpose and Educational Value
This project serves as:
- A beginner-friendly introduction to Pygame.
- A demonstration of real-time rendering and user interaction.
- A foundation for building more complex 2D games.
- A practical example of game loops, physics, and event-driven programming.

Students and developers are encouraged to extend the game by adding:
- Sprites and animations  
- Sound effects  
- Background images  
- Difficulty scaling  
- Menus and UI elements  

---

## 7. Conclusion
The Flappy Bird project represents a complete and functional mini-game built using straightforward concepts and clean logic.  
It is suitable for learning, experimentation, and expanding programming skills in Python game development.

