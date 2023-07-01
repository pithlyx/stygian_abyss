# Stygian-Abyss

Stygian-Abyss is a text-based map exploration game. The game is played in a grid consisting of different types of rooms. The player can move through the map, interact with different room types, and battle enemies. The game includes features such as bombs, health management, leveling up, and room connections.

---

## Dependencies

**!REQUIREMENT! The following dependencies are required to run the game:**
| **Library** | **Description** |
| :----------------: | :----------------: |
|`random` | Provides random number generation functionalities.|
|`hashlib` | Allows hashing of the seed for generating a random map.|
|`collections.deque` | Provides a double-ended queue data structure.|
|`numpy` | Used for various array manipulation tasks.|
|`readchar` | Enables reading characters from the console.|
|`colorama` | Allows color formatting in the console.|

## Play the Game

> Currently the only script that does anything by itself is the game.py file.

- The game will prompt you to enter the size of the map and a seed (optional) for generating a random map. The seed can be used to reproduce the same map layout.

- During the game, you can use the following controls:

  | Hotkeys |      Type       | Action        | Enabled |
  | :-----: | :-------------: | ------------- | :-----: |
  |  W / ⇑  |     `Move`      | Up            | `True`  |
  |  A / ⇐  |     `Move`      | Left          | `True`  |
  |  S / ⇓  |     `Move`      | Down          | `True`  |
  |  D / ⇒  |     `Move`      | Right         | `True`  |
  |    R    |      `Use`      | Bomb          | `False` |
  |    F    |      `Use`      | Flashlight    | `False` |
  |    Q    |      `Use`      | Portal Scroll | `False` |
  |    E    |      `Use`      | Room Action   | `False` |
  | CTRL+R  | `Toggle` `Auto` | Bomb          | `False` |
  | CTRL+F  | `Toggle` `Auto` | Flashlight    | `False` |
  | CTRL+E  | `Toggle` `Auto` | Room Action   | `False` |

---

## Code Structure

This code consists of several classes and functions. Here's a brief overview of the code structure:

| Global Variables | Description                                                                              |
| :--------------: | ---------------------------------------------------------------------------------------- |
|    Directions    | A dictionary that maps movement directions to corresponding keys and relative movements. |
|     Commands     | A dictionary defining game commands with associated hotkeys and actions.                 |

| Classes         | Description                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------- |
| Map             | Represents the game map and manages the generation of floors.                                   |
| Floor           | Represents a single floor in the map and contains rooms.                                        |
| Room            | Base class for different room types, such as EntranceRoom, ExitRoom, EmptyRoom, EnemyRoom, etc. |
| Room subclasses | Derived classes for different room types, each with specific behavior and attributes.           |
| Controller      | Controls the game logic and manages player actions, health, bombs, etc.                         |
| game_menu()     | Function to start the game and handle user input.                                               |

## Final Word

The code uses various techniques, such as random number generation, queue-based algorithms, room connections, and console input/output.

Feel free to explore the code further and modify it to add new features or customize the game behavior (there are various scripts included including a database creation script a database menu script a login script that all work, as well as various test scripts and a CLI menu utility script).

---

## About the Author

**[Cody Roberts](https://your-website.com)**  
Software Engineer | Web Developer  
[LinkedIn](https://www.linkedin.com/in/cody-roberts-swe/) | [GitHub](https://github.com/pithlyx)

Thank you for checking out this project! If you have any questions or suggestions, feel free to reach out. Contributions and feedback are always welcome!
