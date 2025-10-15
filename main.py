"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 15 October 2025
Version: 0.15

- Find out why errors appear when bear moves
- Find out why the blocker for the exit doesn't work
- see what Deepseek thinks (good, bad, ugly)
"""

from map import PacmanMap
from deer import Deer
from bear import Bear
from player import Player
from display import View
import control
import time

HALF_MOVE_INTERVAL = 0.5
FULL_MOVE_INTERVAL = 1
 
"""Remove deer that collided with player or bears using list comprehension"""
def remove_deers(deers,player,bears):
    return [
        deer for deer in deers 
        if not (deer.collides_with(player) or 
                any(deer.collides_with(bear) for bear in bears))
    ]

"""Non-blocking pause handling that returns new pause state"""
def handle_pause(action, is_paused):
    
    if action == "P":
        is_paused = not is_paused  # Toggle pause state
    return is_paused

def handle_quit(action,player):
    if action == "Q":
        player.set_running(False)

def main():
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())

    base_time = time.time()
    is_paused = False

    player = Player(*pacman_map.get_player())
    deers = [Deer(*pos) for pos in pacman_map.get_deers()]
    bears = [Bear(*pos) for pos in pacman_map.get_bears()]


    while(player.get_running()):

        action = control.get_keypress()
        handle_quit(action,player)
        is_paused = handle_pause(action, is_paused)
        
        game_screen.update_screen(pacman_map,player.get_score())
        
        if not is_paused:
            pacman_map.set_map(player.move_player(action,pacman_map.get_map(),pacman_map.get_width()))
            current_time = time.time()

            if (current_time-base_time>HALF_MOVE_INTERVAL) and (current_time-base_time<FULL_MOVE_INTERVAL):
                for bear in bears:
                    if (bear.is_chasing()):
                        pacman_map.set_map(bear.move_bear(pacman_map.get_map(),pacman_map.get_width(),pacman_map.get_entrance()))
                        bear.stop_chasing()

                for deer in deers:
                    if (deer.is_fleeing()):
                        pacman_map.set_map(deer.move_deer(pacman_map.get_map(),pacman_map.get_width()))
                        deer.stop_fleeing()

            elif (current_time-base_time>FULL_MOVE_INTERVAL):
                base_time = current_time

                for deer in deers:
                    pacman_map.set_map(deer.move_deer(pacman_map.get_map(),pacman_map.get_width()))

                for bear in bears:
                    pacman_map.set_map(bear.move_bear(pacman_map.get_map(),pacman_map.get_width(),pacman_map.get_entrance()))

            deers = remove_deers(deers,player,bears)

    return player.get_score()

# Example usage
if __name__ == "__main__":
    main()


"""
4 September 2025 - Created File
7 September 2025 - Added creation of View object
8 September 2025 - Added call to display screen
9 September 2025 - Added controls and quit
13 September 2025 - Passed map object to display as opposed to just map
16 September 2025 - Added Deer class
                  - Moved move deer function to Deer Class
17 September 2025 - Added Bear Class
                  - Moved move bear function to Bear Class
18 September 2025 - Added player class and moved player move function to player class
19 September 2025 - Added section to remove deers from deer list
11 October 2025 - Added a pause game function
12 October 2025 - Move code into main function
13 October 2025 - Made deer move faster if fleeing
14 October 2025 - Created constants and tightened remove deer function
                - Added non blocking pause
15 October 2025 - Updated Bear chasing routine
"""