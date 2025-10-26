"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 26 October 2025
Version: 0.12
"""

import random

class GameMap:

    PLAYER_CHAR = "P"
    DEER_CHAR = "d"
    BEAR_CHAR = "B"
    ENTRANCE_CHAR = "#"
    EXIT_CHAR = "3"

    def __init__(self, file_path):

        #Load Map Data
        self.map_data = self._load_map(file_path)
        if not self.map_data:
            raise ValueError("Failed to load map from {}".format(file_path))

        #Store Map Dimensions
        self.height = len(self.map_data)
        self.width = len(self.map_data[0])

        #Initialise entity positions
        self.player = None
        self.deers = []
        self.bears = []
        self.entrance = None
        self.exit = None
        self.score = 0

        self.__find_characters()
        self.__validate_map()
    

    # --- Map Loading ---
    def _load_map(self, file_path: str) -> list[list[str]]|None:

        map_data = []

        try:
            with open(file_path, 'r') as file:
                lines = [line.rstrip('\n') for line in file if line.strip()]
                
                if not lines:
                     map_data = None
                
                # Check if all lines have the same length
                width = len(lines[0])

                for i, line in enumerate(lines):
                    if len(line) != width:
                        print("Warning: Line {} length mismatch. Padding with spaces.".format(i+1))
                        line = line.ljust(width)
                    map_data.append(list(line))

        except FileNotFoundError:
            print("Error: File '{}' not found.".format(file_path))
            map_data = None

        except Exception as e:
            print("Error loading map: {}".format(e))
            map_data = None

        return map_data
    
    # --- Character Scanning ---
    def __find_characters(self):

        char_mapping = {
            self.PLAYER_CHAR: 'player',
            self.DEER_CHAR: 'deers',
            self.BEAR_CHAR: 'bears',
            self.ENTRANCE_CHAR: 'entrance',
            self.EXIT_CHAR: 'exit'
        }

        counts = {
            'player':0,
            'entrance':0,
            'exit':0
        }

        for row in range(self.height):
            for col in range(self.width):
                cell = self.map_data[row][col]
                if cell in char_mapping:
                    attr = char_mapping[cell]
                    if attr in ['player','entrance','exit']:
                        counts[attr] += 1
                        if counts[attr] > 1:
                            print("Warning: Multiple {}s found, using last at ({},{})".format(attr,row,col))
                    if attr == 'player':
                        self.player = (row,col)
                    elif attr == 'deers':
                        self.deers.append((row,col))
                    elif attr == 'bears':
                        self.bears.append((row,col))
                    elif attr == 'entrance':
                        self.entrance = (row,col)
                    elif attr == 'exit':
                        self.exit = (row,col)

    # --- Map Validation ---
    def __validate_map(self):
        if self.player is None:
            raise ValueError("No player found in map!")

        if self.entrance is None:
            raise ValueError("No entrance found in map!")

        if self.exit is None:
            raise ValueError("No exit found in map!")


    # --- Accessors ---
    def get_cell(self, row: int, col: int) -> str | None:
        character_position = None
        if 0 <= row < self.height and 0 <= col < self.width:
            character_position = self.map_data[row][col]
        return character_position

    def get_map(self) -> list[list[str]]:
        return [row.copy() for row in self.map_data]

    def get_tile(self,row: int, column: int) -> tuple[int,int]:
        return self.map_data[row][column]

    def set_tile(self, row: int, column: int, tile: str):
        self.map_data[row][column] = tile

    def set_map(self,map_data: list[list[str]]):
        
        if not map_data or not all(len(row) == len(map_data[0]) for row in map_data):
            raise ValueError("Invalid map data")
        self.map_data = [row.copy() for row in map_data]
        self.height = len(self.map_data)
        self.width = len(self.map_data[0])

    def get_dimensions(self) -> tuple[int,int]:
        return self.width, self.height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_player(self) -> tuple[int,int]:
        if self.player is None:
            raise ValueError("No player found in map!")
        return self.player

    def get_deers(self) -> list[tuple[int,int]]:
        return self.deers

    def get_bears(self) -> list[tuple[int,int]]:
        return self.bears

    def get_entrance(self) -> tuple[int,int]:
        if self.entrance is None:
            raise ValueError("No entrance found in map!")
        return self.entrance

    def get_exit(self) -> tuple[int,int]:
        if self.exit is None:
            raise ValueError("No exit found in map!")
        return self.exit

    # --- Utility ---
    def print_map(self): 
        for row in self.map_data:
            print("".join(row))

"""
4 September 2025 - Created File
5 September 2025 - Starting tidying up file
8 September 2025 - Added getter for retrieving map
10 September 2025 - Movement now works
11 September 2025 - Added code to prevent movement through certain blocks
13 September 2025 - Added scoring, updated map and added restrictions for player movement
                  - Added end game states
14 September 2025 - Added deer movement. Removed deer from list when grab it
15 September 2025 - Added bear movement
16 September 2025 - Moved move deer function to deer class
18 September 2025 - Removed player functions and variable
23 September 2025 - Added Cave Entrance Tile
16 October 2025 - Added get height
18 October 2025 - Added maze exit.
19 October 2025 - Fixed error and tightened Code.
20 October 2025 - Further refactoring of code. Updated init, and load data
22 October 2025 - Updated code
26 October 2025 - Changed code to handle map object being passed into player
"""