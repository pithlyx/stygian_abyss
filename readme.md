```
# Class 1: Map
class Map:
    def __init__(self):
        # Initialize an empty list of floors
        self.floors = []
        # Create a floor at floors[0] on init
        self.create_floor()

    def create_floor(self):
        # Method to create a floor and append it to the floors list
        pass

    def connect_floors(self):
        # Method to connect floors
        pass

# Class 2: Floor
class Floor:
    def __init__(self):
        # Store the exit of the previous floor and the entrance of the next floor if it exists
        self.prev_floor_exit = None
        self.next_floor_entrance = None
        # Initialize an empty matrix of rooms
        self.rooms = []
        # Initialize a tuple to store the entrance x and y coordinates
        self.ent_x = None
        self.ent_y = None

    def generate_key_rooms(self):
        # Method to generate key rooms (entrance, exit, boss)
        pass

    def fill_rooms(self):
        # Method to fill the rest of the rooms with different room types
        pass

    def get_adjacent_rooms(self, room):
        # Method to get the rooms orthogonally adjacent to a room passed in
        pass

    def connect_rooms(self):
        # Method to try to connect all rooms to adjacent rooms
        pass

# Class 3: Room
class Room:
    def __init__(self, x, y):
        # Initialize booleans for room status
        self.is_occupied = False
        self.is_discovered = False
        self.is_locked = False
        # Initialize room coordinates
        self.x = x
        self.y = y
        # Initialize an empty list of connections
        self.connections = [None, None, None, None]

    def set_room(self, position, room):
        # Method to set a given room to a position in connections
        pass

    def on_enter(self):
        # Method to set the room to occupied when entered
        self.is_occupied = True

    def on_exit(self):
        # Method to set the room to unoccupied when exited
        self.is_occupied = False

# Class 4: Controller
class Controller:
    def __init__(self):
        # Initialize a Map and set the current floor and room
        self.map = Map()
        self.current_floor = self.map.floors[0]
        self.current_room = self.current_floor.rooms[0][0]  # Assuming start room is at 0,0
        # Enter the start room
        self.current_room.on_enter()

    def get_room(self, direction):
        # Method to get a room in a direction from the current room's connections
        pass
```
