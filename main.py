"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 8 September 2025
Version: 0.3
"""

from map import PacmanMap
from display import View

# Example usage
if __name__ == "__main__":
    
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())
    game_screen.update_screen(pacman_map.get_map())

    thing=0
    while(True):
        thing+=1
         #Move Cavewoman first - create controller and use arrow keys
         #                     - Takes position, changes it based of movement,
         #                     - If Blocked does nothing
         #                     - If not blocked, moves to new position, previous position is blank
         #                     - Updates map - if berry adds 1 to score
         #                                   - if deer adds 10
         #                                   - if bear - dies

    if pacman_map.map_data:
        print(f"Map loaded: {pacman_map.width}x{pacman_map.height}")
        print("\nMap:")
        pacman_map.print_map()
        
        # Example: Find Pac-Man's starting position (usually 'P')
        pacman_positions = pacman_map.get_player()
        if pacman_positions:
            print(f"\nPac-Man starts at: {pacman_positions[0]}")

        # Example: Find deer starting position (usually 'P')
        deer_positions = pacman_map.get_deer()
        if deer_positions:
            print(f"\nDeer start at: {deer_positions}")

        # Example: Find bear starting position (usually 'P')
        bear_positions = pacman_map.get_bear()
        if bear_positions:
            print(f"\nBears start at: {bear_positions}")
        
"""
4 September 2025 - Created File
7 September 2025 - Added creation of View object
8 September 2025 - Added call to display screen
"""