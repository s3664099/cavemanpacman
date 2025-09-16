"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 13 September 2025
Version: 0.5

Create Bear & Deer object and have movement occur in there.
    Stores the position
    Has the flee/chase boolean
    Bear holds what is on the square
"""

from map import PacmanMap
from display import View
import control
import time

# Example usage
if __name__ == "__main__":
    
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())
    game_screen.update_screen(pacman_map)
    base_time = time.time()

    thing=0
    while(pacman_map.get_running()):
        action = control.get_keypress()
        if action == "Q":
            pacman_map.set_running(False)
        pacman_map.move_player(action)
        game_screen.update_screen(pacman_map)
        
        current_time = time.time()
        if (current_time-base_time>1):
            base_time = current_time
            pacman_map.move_deer()
            pacman_map.move_bear()
        

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
13 September 2025 - Passed map object to display as opposed to just map
"""