"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 5 September 2025
Version: 0.1
"""

class PacmanMap:
    def __init__(self, file_path):

        self.map_data = self.load_map(file_path)
        self.height = len(self.map_data) if self.map_data else 0
        self.width = len(self.map_data[0]) if self.map_data else 0
        self.player = []
        self.deer = []
        self.bear = []

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
                
                if not lines:
                    lines = None
                
                # Check if all lines have the same length
                first_line_length = len(lines[0])
                for i, line in enumerate(lines):
                    if len(line) != first_line_length:
                        print(f"Warning: Line {i+1} has different length than first line")

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            lines = None

        except Exception as e:
            print(f"Error loading map: {e}")
            lines = None

        return lines

    #Get the character at a specific position
    def get_cell(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.map_data[row][col]
        return None
    
    #Merge all into same, and fill this from constructor
    def find_character(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == self.player_position:
                    self.player.append((row,col))
                elif self.map_data[row][col] == self.deer_position:
                    self.deer.append((row,col))
                elif self.map_data[row][col] == self.bear_position:
                    self.bear.append((row,col))
            
    #Print the map
    def print_map(self):
        
        for row in self.map_data:
            print(row)
    
    #Return map dimensions
    def get_dimensions(self):
        return self.width, self.height

    #Getters
    def get_player(self):
        return self.player

    def get_deer(self):
        return self.deer

    def get_bear(self):
        return self.bear
"""
4 September 2025 - Created File
5 September 2025 - Starting tidying up file
"""