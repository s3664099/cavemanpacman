"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 13 September 2025
Version: 0.5
"""

class PacmanMap:
    def __init__(self, file_path):

        self.map_data = self.load_map(file_path)
        self.height = len(self.map_data) if self.map_data else 0
        self.width = len(self.map_data[0]) if self.map_data else 0
        self.player = []
        self.deer = []
        self.bear = []
        self.score = 0

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
                    self.deer.append((row,col))
                elif self.map_data[row][col] == self.bear_position:
                    self.bear.append((row,col))
    
    def move_player(self,key):

        row,col = self.player
        new_row,new_col = row,col
        non_blockers = ["."," ","d"]

        if key == "N":
            new_row -=1
        elif key == "S":
            new_row +=1
        elif key == "E":
            new_col +=1
        elif key == "W":
            new_col -=1

        if (new_col<self.width):
            new_position = self.map_data[new_row][new_col]

            if (new_position in non_blockers):

                if (self.map_data[new_row][new_col]=="."):
                    self.score += 1
                elif (self.map_data[new_row][new_col]=="d"):
                    self.score += 10
                elif (self.map_data[new_row][new_col]=="w"):
                    self.score += 5

                self.map_data[row][col] = " "
                self.map_data[new_row][new_col] = "P"
                self.player = (new_row,new_col)
        
         #Move Cavewoman first - Checks if valid move (is there a wall)
         #                     - If Blocked does nothing
         #                     - If not blocked, moves to new position, previous position is blank
         #                     - Updates map - if berry adds 1 to score
         #                                   - if deer adds 10
         #                                   - if bear - dies



    #Print the map
    def print_map(self):
        
        for row in self.map_data:
            print(row)

    def get_map(self):
        return self.map_data
    
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

    def get_score(self):
        return self.score
"""
4 September 2025 - Created File
5 September 2025 - Starting tidying up file
8 September 2025 - Added getter for retrieving map
10 September 2025 - Movement now works
11 September 2025 - Added code to prevent movement through certain blocks
13 September 2025 - Added scoring, updated map and added restrictions for player movement
"""