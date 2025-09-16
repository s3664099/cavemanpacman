"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 16 September 2025
Version: 0.6

Create Deer object and have movement occur in there.
    Stores the position
    Has the flee/chase boolean
    Bear holds what is on the square

Do flee for deer
    - if see player or bear, runs away (and at double speed)
    - checks if see every move. Stops once no longer see
Do chase for beer
"""

from map import PacmanMap
from deer import Deer
from display import View
import control
import time

# Example usage
if __name__ == "__main__":
    
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())
    game_screen.update_screen(pacman_map)
    base_time = time.time()
    running = True

    deers = []

    for deer in pacman_map.get_deers():
        deers.append(Deer(deer[0],deer[1]))

    while(running):
        action = control.get_keypress()
        if action == "Q":
            running = False
        pacman_map.move_player(action)
        game_screen.update_screen(pacman_map)
        
        current_time = time.time()
        if (current_time-base_time>1):
            base_time = current_time

            for deer in deers:
                pacman_map.set_map(deer.move_deer(pacman_map.get_map(),pacman_map.get_width()))

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
        deer_positions = pacman_map.get_deers()
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
16 September 2025 - Added Deer class
                  - Moved move deer function to Deer Class
"""