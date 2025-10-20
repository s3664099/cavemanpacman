"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 20 October 2025
Version: 0.10
"""

import random

class PacmanMap:

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

        #Store Map Dimenstions
        self.height = len(self.map_data)
        self.width = len(self.map_data[0])

        #Initialise entity positions
        self.player = None
        self.deers = []
        self.bears = []
        self.entrance = None
        self.exit = None
        self.score = 0

        self.find_characters()
        self.validate_map()
    

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

    #Get the character at a specific position
    def get_cell(self, row, col):
        character_position = None
        if 0 <= row < self.height and 0 <= col < self.width:
            character_position = self.map_data[row][col]
        return character_position
    
    #Merge all into same, and fill this from constructor
    def find_characters(self):

        player_count = 0
        entrance_count = 0
        exit_count = 0

        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == PLAYER_CHAR:
                    if player_count>0:
                        print(f"Warning: Multple players found, using last at ({row},{col})")
                    self.player = (row,col)
                    player_count +=1
                elif self.map_data[row][col] == DEER_CHAR:
                    self.deers.append((row,col))
                elif self.map_data[row][col] == BEAR_CHAR:
                    self.bears.append((row,col))
                elif self.map_data[row][col] == ENTRANCE_CHAR:
                    if entrance_count>0:
                        print(f"Warning: Multple entrances found, using last at ({row},{col})")
                    self.entrance = (row,col)
                    entrance_count += 1
                elif self.map_data[row][col] == EXIT_CHAR:
                    if exit_count>0:
                        print(f"Warning: Multple exits found, using last at ({row},{col})")
                    self.exit = (row,col)
                    exit_count += 1

    #Print the map
    def print_map(self):
        for row in self.map_data:
            print("".join(row))

    def get_map(self):
        return self.map_data

    def set_map(self,map_data):
        self.map_data = map_data
    
    #Return map dimensions
    def get_dimensions(self):
        return self.width, self.height

    #Getters
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_player(self):
        if self.player is None:
            raise ValueError("No player found in map!")
        return self.player

    def get_deers(self):
        return self.deers

    def get_bears(self):
        return self.bears

    def get_entrance(self):
        if self.entrance is None:
            raise ValueError("No entrance found in map!")
        return self.entrance

    def get_exit(self):
        if self.exit is None:
            raise ValueError("No exit found in map!")
        return self.exit

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
"""