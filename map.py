"""
File: Caveman Pacman Map
Author: David Sarkies
Initial: 4 September 2025
Update: 4 September 2025
Version: 0.0
"""

class PacmanMap:
    def __init__(self, file_path):
        self.map_data = self.load_map(file_path)
        self.height = len(self.map_data) if self.map_data else 0
        self.width = len(self.map_data[0]) if self.map_data else 0
        self.player = []
        self.deer = []
        self.bear = []
    
    def load_map(self, file_path):
        """Load map from text file"""
        try:
            with open(file_path, 'r') as file:
                lines = [line.rstrip('\n') for line in file.readlines()]
                # Filter out empty lines and ensure all lines have same length
                lines = [line for line in lines if line]
                
                if not lines:
                    return None
                
                # Check if all lines have the same length
                first_line_length = len(lines[0])
                for i, line in enumerate(lines):
                    if len(line) != first_line_length:
                        print(f"Warning: Line {i+1} has different length than first line")
                
                return lines
                
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error loading map: {e}")
            return None
    
    def get_cell(self, row, col):
        """Get the character at a specific position"""
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.map_data[row][col]
        return None
    
    def find_character(self, char):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == char:
                    self.player.append((row,col))
        return self.player

    def find_deer(self, char):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == char:
                    self.deer.append((row,col))
        return self.deer

    def find_bear(self, char):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == char:
                    self.bear.append((row,col))
        return self.bear
    
    def print_map(self):
        """Print the map"""
        for row in self.map_data:
            print(row)
    
    def get_dimensions(self):
        """Return map dimensions"""
        return self.width, self.height
"""
4 September 2025 - Created File