import readchar
from game.classes.map_classes import Map

def menu():
    seed = input("Enter a seed for the map (leave blank for random): ")
    game_map = Map(int(input("Enter the size of the map: ")), seed if seed else None)
    bomb = False  # Initialize bomb as False

    while True:
        print("\n--- Menu ---")
        print("1. Move")
        print("2. List rooms")
        print("3. List path")
        print("4. Exit")
        print(f"You have {game_map.bombs} bombs.")

        choice = input("Enter your choice: ")

        if choice == "1":
            game_map.display()
            while True:
                key = readchar.readkey()
                if key == " ":
                    if game_map.bombs > 0:
                        bomb = not bomb
                        print("Bomb is now", "active" if bomb else "inactive")
                    else:
                        print("No bombs left!")
                    continue

                direction = {
                    "\x1b[A": "up",  # Up arrow key
                    "\x1b[B": "down",  # Down arrow key
                    "\x1b[C": "right",  # Right arrow key
                    "\x1b[D": "left"  # Left arrow key
                }.get(key)

                if direction is None:
                    break

                room = game_map.move(direction, bomb)
                if room:
                    print("Moved successfully!")
                    print(room.get_info())
                    game_map.display()
                else:
                    print("Cannot move in that direction. Invalid position!")

        elif choice == "2":
            game_map.list_rooms()

        elif choice == "3":
            game_map.list_path()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

# Run the menu
if __name__ == "__main__":
    menu()