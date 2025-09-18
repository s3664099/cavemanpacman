"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 18 September 2025
Version: 0.6

Remove the deer when encountering it
"""

import random

class PacmanMap:
    def __init__(self, file_path):

        self.map_data = self.load_map(file_path)
        self.height = len(self.map_data) if self.map_data else 0
        self.width = len(self.map_data[0]) if self.map_data else 0
        self.player = []
        self.deers = []
        self.bears = []
        self.score = 0
        self.bear_square = [" "," "]

        self.player_position = "P"
        self.deer_position = "d"
        self.bear_position = "B"

        self.find_character()
    

    #Load map from text file
    def load_map(self, file_path):

        lines = ""

        try:
            with open(file_path, 'r') as file:

                #Read Lines, filter our any empty lines
                lines = [line.rstrip('\n') for line in file.readlines()]
                lines = [line for line in lines if line]
                mutable_lines = []
                
                if not lines:
                    mutable_lines = None
                
                # Check if all lines have the same length
                first_line_length = len(lines[0])

                for i, line in enumerate(lines):
                    if len(line) != first_line_length:
                        print(f"Warning: Line {i+1} has different length than first line")
                        line = line.ljust(first_line_length)

                    mutable_lines.append(list(line))

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            mutable_lines = None

        except Exception as e:
            print(f"Error loading map: {e}")
            mutable_lines = None

        return mutable_lines

    #Get the character at a specific position
    def get_cell(self, row, col):
        character_position = None
        if 0 <= row < self.height and 0 <= col < self.width:
            character_position = self.map_data[row][col]
        return character_position
    
    #Merge all into same, and fill this from constructor
    def find_character(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == self.player_position:
                    self.player = (row,col)
                elif self.map_data[row][col] == self.deer_position:
                    self.deers.append((row,col))
                elif self.map_data[row][col] == self.bear_position:
                    self.bears.append((row,col))

    #Print the map
    def print_map(self):
        
        for row in self.map_data:
            print(row)

    def get_map(self):
        return self.map_data

    def set_map(self,map_data):
        self.map_data = map_data
    
    #Return map dimensions
    def get_dimensions(self):
        return self.width, self.height

    def get_width(self):
        return self.width

    #Getters
    def get_player(self):
        return self.player

    def get_deers(self):
        return self.deers

    def get_bears(self):
        return self.bears

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
"""