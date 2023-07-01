import random
import uuid

class Room:
    TYPES = {
        "wall": "|||",
        "fountain": "{~}",
        "enemy": "!-!",
        "boss": ">-<",
        "empty": "[ ]"
    }

    def __init__(self, x, y, room_id, room_type=None):
        self.x, self.y, self.room_id = x, y, room_id
        self.type = room_type if room_type else self.random_type()

    def __str__(self):
        return self.TYPES[self.type]

    def get_info(self):
        return f"Room ID: {self.room_id}, Position: ({self.x}, {self.y}), Type: {self.type}"

    @staticmethod
    def random_type():
        return random.choices(
            population=list(Room.TYPES.keys()),
            weights=[30, 5, 40, 5, 20],
            k=1
        )[0]

    def interact(self):
        if self.type == "fountain":
            return 1
        return 0

class Map:
    DIRECTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

    def __init__(self, size, seed=None):
        self.size = size
        self.rooms = [[None] * size for _ in range(size)]
        self.path = "0"
        self.visited_rooms = [0]
        self.bombs = 3  # Player starts with 3 bombs
        self.seed = seed if seed else str(uuid.uuid4())
        random.seed(self.seed)
        self._current_room = self.generate_rooms()

    def generate_rooms(self):
        initial_room = self.create_room(self.size // 2, self.size // 2, 0)
        self.check_adjacent_rooms(initial_room)
        return initial_room

    def create_room(self, x, y, room_id, room_type=None):
        if self.is_valid_position(x, y) and self.rooms[x][y] is None:
            room = Room(x, y, room_id, room_type)
            self.rooms[x][y] = room
            return room
        return None

    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, room):
        if room is not None:
            self._current_room = room
            self.path += f",{room.room_id}"
            self.check_adjacent_rooms(room)

    def check_adjacent_rooms(self, room):
        for (x_offset, y_offset) in self.DIRECTIONS.values():
            new_x, new_y = room.x + x_offset, room.y + y_offset
            if self.is_valid_position(new_x, new_y) and self.rooms[new_x][new_y] is None:
                room_id = len(self.visited_rooms)
                self.create_room(new_x, new_y, room_id)
                self.visited_rooms.append(room_id)

    def move(self, direction, bomb=False):
        x_offset, y_offset = self.DIRECTIONS.get(direction, (0, 0))
        new_x, new_y = self.current_room.x + x_offset, self.current_room.y + y_offset
        if not self.is_valid_position(new_x, new_y):
            return None
        room = self.rooms[new_x][new_y]
        if room and (room.type != "wall" or (bomb and self.bombs > 0)):
            if room.type == "wall" and bomb:
                room.type = "empty"
                self.bombs -= 1
            self.bombs += room.interact()
            self.current_room = room
        return room


    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def display(self):
        for y in range(self.size):
            for x in range(self.size):
                room = self.rooms[x][y]
                print("[X]" if room == self.current_room else " - " if not room else str(room), end="")
            print()

    def list_rooms(self):
        for room_id in self.visited_rooms:
            room = self.get_room_by_id(room_id)
            print(f"Room ID: {room.room_id} - Position: ({room.x}, {room.y}) - Type: {room.type}")

    def list_path(self):
        print("Path:", self.path)

    def get_room_by_id(self, room_id):
        for row in self.rooms:
            for room in row:
                if room and room.room_id == room_id:
                    return room
        return None
