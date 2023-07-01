import random
import hashlib
from collections import deque
import numpy as np
import readchar
from colorama import Fore, Style

DIRECTIONS = {
    'n': {
        'hotkeys': ['w', '\x1b[A'],  # 'w' and up arrow key
        'relative': (-1, 0),
        'opposite': 's',
    },
    'e': {
        'hotkeys': ['d', '\x1b[C'],  # 'd' and right arrow key
        'relative': (0, 1),
        'opposite': 'w',
    },
    's': {
        'hotkeys': ['s', '\x1b[B'],  # 's' and down arrow key
        'relative': (1, 0),
        'opposite': 'n',
    },
    'w': {
        'hotkeys': ['a', '\x1b[D'],  # 'a' and left arrow key
        'relative': (0, -1),
        'opposite': 'e',
    }
}
COMMANDS = {
    'quit': {
        'hotkeys':['q', '\x03', '\x1b'],
        'on_press': 'quit',
        'on_release': None
        },
    'bomb': {
        'hotkeys':['b', ' '],
        'on_press': 'enable_bomb',
        'on_release': 'disable_bomb'
        },
    'attack': {
        'hotkeys':['q'],
        'on_press': 'attack',
        },
}


class Map:
    def __init__(self, size, seed):
        self._seed = seed
        self.width = size
        self.floors = []
        self.new_floor()
    @property
    def seed(self):
        return self._seed

    @seed.setter
    def set_seed(self, new_seed):
        if type(new_seed) is not str:
            new_seed = str(new_seed)
        hashed = hashlib.md5(new_seed.encode()).hexdigest()
        self._seed = int(hashed, 16)
        random.seed(self._seed)

    def new_floor(self):
        if len(self.floors) == 0:
            new_floor = Floor(self.width, 2, 3)
        else:
            prev_floor = self.floors[-1]
            new_floor = Floor(self.width, prev_floor.exit_room.x, prev_floor.exit_room.y)
            new_floor.prev_floor = prev_floor
            prev_floor.next_floor = new_floor
        self.floors.append(new_floor)
        return new_floor


class Floor:
    def __init__(self, width, x, y):
        self.width = width
        self.floor_entrance = (x, y)
        self.entrance_room = None
        self.exit_room = None
        self.boss_room = None
        self.prev_floor = None
        self.next_floor = None
        self.rooms = [[None for _ in range(self.width)] for _ in range(self.width)]
        self.init_rooms()
        self.set_unique()
        self.fill_rooms()
        self.connect_rooms()
    def init_rooms(self):
        # Initialize all rooms as empty rooms
        for x in range(self.width):
            for y in range(self.width):
                self.rooms[x][y] = EmptyRoom(self, x, y)

    def set_unique(self):
        # Set the entrance room
        entrance_x, entrance_y = self.floor_entrance
        print(entrance_x, entrance_y)
        self.entrance_room = EntranceRoom(self, entrance_x, entrance_y)
        self.rooms[entrance_x][entrance_y] = self.entrance_room

        # Set the exit room
        while True:
            exit_x = random.randint(0, self.width - 1)
            exit_y = random.randint(0, self.width - 1)
            distance = abs(entrance_x - exit_x) + abs(entrance_y - exit_y)
            if distance >= max(8, self.width * 0.8):
                break
        self.exit_room = ExitRoom(self, exit_x, exit_y)
        self.rooms[exit_x][exit_y] = self.exit_room

        # Set the boss room
        while True:
            boss_x = random.randint(0, self.width - 1)
            boss_y = random.randint(0, self.width - 1)
            distance = abs(entrance_x - boss_x) + abs(entrance_y - boss_y)
            if distance >= max(4, self.width * 0.2):
                break
        self.boss_room = BossRoom(self, boss_x, boss_y)
        self.rooms[boss_x][boss_y] = self.boss_room

    def fill_rooms(self):
        # Fill the remaining rooms
        room_types = {
            'empty': {'class': EmptyRoom, 'count': 0, 'lower_limit': 0.4, 'upper_limit': 0.6},
            'enemy': {'class': EnemyRoom, 'count': 0, 'lower_limit': 0.2, 'upper_limit': 0.4},
            'wall': {'class': WallRoom, 'count': 0, 'lower_limit': 0.1, 'upper_limit': 0.3},
            'shrine': {'class': ShrineRoom, 'count': 0, 'lower_limit': 0.05, 'upper_limit': 0.15},
        }
        total_rooms = self.width * self.width - 3  # Subtract 3 for the entrance, exit, and boss rooms
        for x in range(self.width):
            for y in range(self.width):
                if (x, y) in [self.entrance_room.coords, self.exit_room.coords, self.boss_room.coords]:
                    # print("UNIQUE ROOM | ", self.rooms[x][y].__class__.__name__)
                    continue  # Skip the entrance, exit, and boss rooms
                # Calculate weights based on current counts and limits
                weights = []
                for room_type, data in room_types.items():
                    if data['count'] / total_rooms < data['lower_limit']:
                        weights.append(1)
                    elif data['count'] / total_rooms > data['upper_limit']:
                        weights.append(0)
                    else:
                        weights.append((data['upper_limit'] - data['count'] / total_rooms) / (data['upper_limit'] - data['lower_limit']))
                weights = [weight / sum(weights) for weight in weights]  # Normalize weights
                room_type = np.random.choice(list(room_types.keys()), p=weights)
                room = room_types[room_type]['class'](self, x, y)
                self.rooms[x][y] = room
                room_types[room_type]['count'] += 1  # Increment count
                # print(self.rooms[x][y].__class__.__name__, room.coords)

    def connect_rooms(self):
        rooms = self.rooms
        for row in rooms:
            for room in row:
                if room.room_type == 'wall':
                    continue
                possible_connections = []
                for direction, data in DIRECTIONS.items():
                    dx, dy = data['relative']
                    nx, ny = room.x + dx, room.y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.width:
                        adjacent_room = self.get_room(nx, ny)
                        if adjacent_room is not None and adjacent_room.room_type != 'wall' and room.get_connection(direction) is None:
                            possible_connections.append((adjacent_room, direction))
                if not possible_connections:
                    continue
                for connection, direction in possible_connections:
                    if room.connect(connection, direction):
                        room.connection_count -= 1
                        connection.connection_count -= 1


    def get_room(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.width:
            return self.rooms[x][y]
        else:
            return None

    def get_adjacent(self, x, y):
        adjacent_rooms = []
        for direction, data in DIRECTIONS.items():
            dx, dy = data['relative']
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.width:
                adjacent_rooms.append(self.rooms[nx][ny])
        return adjacent_rooms
    def get_in_range(self, x, y, range):
        in_range_rooms = []
        visited = [[False for _ in range(self.width)] for _ in range(self.width)]
        queue = deque([(x, y, 0)])  # queue of (x, y, distance)
        while queue:
            cx, cy, dist = queue.popleft()
            if dist > range:
                break
            if not visited[cx][cy]:
                visited[cx][cy] = True
                in_range_rooms.append(self.rooms[cx][cy])
            for direction, data in DIRECTIONS.items():
                dx, dy = data['relative']
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.width and 0 <= ny < self.width:
                    queue.append((nx, ny, dist + 1))
        return in_range_rooms


    def get_discovered(self):
        return [room for sublist in self.rooms for room in sublist if room.is_discovered]

    def get_occupied(self):
        return next((room for room in self.get_discovered() if room.is_occupied), None)

    def get_in_range(self, x, y, range):
        in_range_rooms = []
        visited = [[False for _ in range(self.width)] for _ in range(self.width)]
        queue = deque([(x, y, 0)])  # queue of (x, y, distance)
        while queue:
            cx, cy, dist = queue.popleft()
            if dist > range:
                break
            if not visited[cx][cy]:
                visited[cx][cy] = True
                in_range_rooms.append(self.rooms[cx][cy])
            for direction in DIRECTIONS.keys():
                dx, dy = DIRECTIONS[direction][0]
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.width and 0 <= ny < self.width:
                    queue.append((nx, ny, dist + 1))
        return in_range_rooms


    def discover_range(self, x, y, range):
        rooms_in_range = self.get_in_range(x, y, range)
        for room in rooms_in_range:
            room.is_discovered = True
    
    def print_floor(self):
        print('-'*50)
        for row in self.rooms:
            for room in row:
                string = list(room.__str__())
                if room.is_occupied:
                    string = Fore.MAGENTA + '<X>' + Style.RESET_ALL
                print(''.join(string), end='')
            print()
        print('-'*50)

# --- Rooms ---
class Room:
    def __init__(self, floor, x, y):
        self.floor = floor
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.is_discovered = False
        self.is_occupied = False
        self.max_connection_count = random.randint(2,4) if self.room_type != 'wall' else 0
        self.connection_count = self.max_connection_count
        self.connections = {direction: None for direction in DIRECTIONS.keys()}

    def enter(self):
        if self.room_type == 'wall':
            raise KeyError('You cannot enter this room.')
        self.is_occupied = True
        self.on_enter()
        return self
    
    def leave(self, direction):
        try:
            if self.connections[direction] is None:
                raise KeyError('You cannot leave this room in that direction.')
            self.is_occupied = False
            return self.connections[direction]
        except KeyError as e:
            raise KeyError('You cannot leave this room in that direction.') from e

    def connect(self, room, direction):
        if room in self.connections.values():
            return False
        self.connections[direction] = room
        opposite_direction = DIRECTIONS[direction]['opposite']
        room.connections[opposite_direction] = self
        return True

    def get_connection(self, direction=None):
        if direction is None:
            return self.connections
        else:
            return self.connections.get(direction)

class ShrineRoom(Room):
    def __init__(self, floor, x, y):
        self.room_type = "shrine"
        self.collected = False
        super().__init__(floor, x, y)

    def on_enter(self):
        self.collected = True
        print(Fore.YELLOW + 'You found a shrine! +1 Bombs.' + Style.RESET_ALL)
    
    def __str__(self):
        return Fore.YELLOW + '/~\\' + Style.RESET_ALL

class WallRoom(Room):
    def __init__(self, floor, x, y):
        self.room_type = "wall"
        super().__init__(floor, x, y)

    def on_enter(self):
        print(Fore.RED + "You ran into a wall!" + Style.RESET_ALL)

    def __str__(self):
        return Fore.RED + '|||' + Style.RESET_ALL
    
class EnemyRoom(Room):
    def __init__(self, floor, x, y, scale=0):
        self.room_type = "enemy"
        self.scale = 1+scale
        self.enemies = round(random.randint(2, 4)*(self.scale))
        self.max_health = round(sum(random.randint(15, 25) for _ in range(self.enemies)) * self.scale, 2)
        self.health = self.max_health
        self.damage = self.get_damage()
        super().__init__(floor, x, y)

    def set_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0
            raise ValueError("This room has already been cleared!")

    def get_damage(self):
        self.damage = sum(random.randint(1, 5) for _ in range(self.enemies))*self.scale

    def turn(self, controller):
        try:
            player_damage = controller.get_damage()
            enemy_health = self.set_health(-player_damage)
            print(f"You dealt {player_damage} damage to the enemies. They have {enemy_health} health left.")
            enemy_damage = self.get_damage()
            player_health = controller.set_health(-enemy_damage)
            print(f"The enemies dealt {enemy_damage} damage to you. You have {player_health} health left.")
        except ValueError as e:
            raise ValueError(e) from e
            
    
    def on_enter(self):
        print(Fore.CYAN + f"You found an enemy room! Enemy Count: {self.enemies} | Enemy Health: {self.health}" + Style.RESET_ALL)
        return self
        
    def __str__(self):
        return Fore.CYAN + ':e:' + Style.RESET_ALL

class EmptyRoom(Room):
    def __init__(self, floor, x, y):
        self.room_type = "empty"
        super().__init__(floor, x, y)

    def on_enter(self):
        print(Fore.WHITE + "You found an empty room." + Style.RESET_ALL)
        
    def __str__(self):
        return Fore.WHITE + '[ ]' + Style.RESET_ALL
    
class BossRoom(Room):
    def __init__(self, floor, x, y, scale=0):
        self.room_type = "boss"
        self.scale = 1+scale
        self.boss = True
        self.max_health = 100*(np.ceil(scale/2))
        self.health = self.max_health
        self.damage = self.get_damage()
        super().__init__(floor, x, y)

    def set_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0
            raise ValueError("The Boss is dead!")

    def get_damage(self):
        self.damage = random.randint(10, 20)*self.scale

    def turn(self, controller):
        try:
            player_damage = controller.get_damage()
            enemy_health = self.set_health(-player_damage)
            print(f"You dealt {player_damage} damage to the enemies. They have {enemy_health} health left.")
            enemy_damage = self.get_damage()
            player_health = controller.set_health(-enemy_damage)
            print(f"The boss deals {enemy_damage} damage to you. You have {player_health} health left.")
        except ValueError as e:
            raise ValueError(e) from e
            
    def on_enter(self):
        print(Fore.RED + f"You found the boss room! Boss Health: {self.health}" + Style.RESET_ALL)
        return self
        
    def __str__(self):
        return Fore.RED + '<B>' + Style.RESET_ALL
    
class EntranceRoom(Room):
    def __init__(self, floor, x, y):
        self.room_type = "entrance"
        self.connection = None
        super().__init__(floor, x, y)

    def connect_floor(self , prev_floor):
        self.connection = prev_floor

    def on_enter(self):
        return Fore.GREEN + "You found the entrance!" + Style.RESET_ALL
    
    def __str__(self):
        return Fore.GREEN + '˄˄˄' + Style.RESET_ALL

class ExitRoom(Room):
    def __init__(self, floor, x, y):
        self.room_type = "exit"
        self.connection = None
        super().__init__(floor, x, y)

    def connect_floor(self , next_floor):
        self.connection = next_floor

    def on_enter(self):
        return Fore.GREEN + "You found the exit!" + Style.RESET_ALL

    def __str__(self):
        return Fore.GREEN + '˅˅˅' + Style.RESET_ALL

class Controller:
    def __init__(self, size, seed):
        self.my_map = Map(size, seed)
        self.current_floor = self.my_map.floors[0]
        self.current_room = self.current_floor.entrance_room.enter()
        self.experience = 1
        self.level = np.ceil(self.experience/100)
        self.scale = np.ceil(self.level*.2) 
        self.max_health = 100-(self.scale*10)
        self.health = self.max_health
        self.magic_dmg_mod = .1
        self.phys_dmg_mod = .1
        self.dmg_mod = max(self.magic_dmg_mod, self.phys_dmg_mod)
        self.dmg = 0
        self.bombs = 3
        self.bombing = False
    
    def set_health(self, amount):
        self.health += amount-amount*self.scale*.1
        if self.health < 0:
            self.health = 0
            raise ValueError(f"You took {amount} damage and died!")
        elif self.health > self.max_health:
            self.health = self.max_health
        return self.health
    
    def set_mod(self, modifier, increment = True):
        self[f'{modifier}_dmg_mod'] += .1 if increment else -.1
        self.dmg_mod = max(self.magic_dmg_mod, self.phys_dmg_mod)
        return self.dmg_mod
    
    def set_experience(self, points):
        self.experience += points
        self.level = np.ceil(self.experience/100)
        self.scale = np.ceil(self.level*.2)
        self.max_health = 100-(self.scale*10)
        self.health = self.max_health
        self.dmg = (10*(self.dmg_mod+1))*(self.scale+1)
        return self.experience

    def get_damage(self):
        self.dmg = (random.randint(10,20)*(self.dmg_mod+1))*(self.scale)
        return self.dmg

    def move(self, direction):
        try:
            new_room = self.current_room.leave(direction)
            if new_room.room_type == 'exit':
                self.current_floor = self.current_floor.next_floor or self.my_map.new_floor()
                self.current_room = self.current_floor.entrance_room.enter()
            elif new_room.room_type == 'entrance':
                if self.current_floor.prev_floor:
                    print('You found the entrance to the previous floor!')
                    self.current_floor = self.current_floor.prev_floor
                    self.current_room = self.current_floor.exit_room.enter()
                else:
                    self.current_room = new_room.enter()
                
            else:
                self.current_room = new_room.enter()
        except Exception as e:
            raise Exception(e) from e


    def toggle_bomb(self):
        if self.bombs <= 0:
            raise ValueError("You have no bombs left!")
        self.bombing = not self.bombing

    def attack(self):
        if self.current_room.room_type not in ['boss', 'enemy']:
            raise KeyError("There is nothing to attack in this room.")
        try:
            self.current_room.turn(self)
        except Exception as e:
            raise Exception(e) from e




def game_menu():
    size = int(input("Enter a size for the map: ")or 10) 
    seed = input("Enter a seed to generate the map: ") or None
    controller = Controller(size, seed)
    bomb_mode = False

    while True:
        controller.current_floor.print_floor()
        command = readchar.readkey()
        if command == ' ':
            bomb_mode = not bomb_mode
            continue
        direction = next((key for key, data in DIRECTIONS.items() if command in data['hotkeys']), None)
        if bomb_mode:
            try:
                controller.use_bomb(direction)
                print("You used a bomb and destroyed a wall.")
            except ValueError as e:
                print(e)
            bomb_mode = False
        elif direction is not None:
            try:
                controller.move(direction)
            except Exception as e:
                print(e)
        elif command == 'q':
            try: 
                controller.attack()
            except Exception as e:
                print(e)
        else:
            print("Invalid command. Please use the arrow keys or (W,A,S,D) to move.")

game_menu()