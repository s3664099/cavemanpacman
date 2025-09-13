"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 9 September 2025
Version: 0.4
"""

from map import PacmanMap
from display import View
import control

# Example usage
if __name__ == "__main__":
    
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())
    game_screen.update_screen(pacman_map)
    running = True

    thing=0
    while(running):
        action = control.get_keypress()
        if action == "Q":
            running = False
        pacman_map.move_player(action)
        game_screen.update_screen(pacman_map)
        #Move bear & move Deer

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
9 September 2025 - Added controls and quit
"""