"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 27 October 2025
Version: 0.20



deer.py
control.py
display.py
main.py

"""

from map import GameMap
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
        player.set_end()

def main():
    game_map = GameMap("map.txt")
    game_screen = View(game_map.get_dimensions())

    last_update_time = time.time()
    is_paused = False
    half_move_done = False

    player = Player(game_map)
    deers = [Deer(*pos) for pos in game_map.get_deers()]
    bears = [Bear(*pos) for pos in game_map.get_bears()]


    while(player.is_running()):

        current_time = time.time()
        elapsed_time = current_time - last_update_time
        action = control.get_keypress()
        
        handle_quit(action,player)
        is_paused = handle_pause(action, is_paused)
        
        if not is_paused:

            player.move_player(action)

            if elapsed_time >= HALF_MOVE_INTERVAL and not half_move_done:
                for bear in bears:
                    if (bear.is_chasing()):
                        game_map.set_map(bear.move_bear(game_map))
                        bear.stop_chasing()

                for deer in deers:
                    if (deer.is_fleeing()):
                        game_map.set_map(deer.move_deer(game_map))
                        deer.stop_fleeing()

                half_move_done = True

            if elapsed_time >= FULL_MOVE_INTERVAL:

                for deer in deers:
                    game_map.set_map(deer.move_deer(game_map))

                for bear in bears:
                    game_map.set_map(bear.move_bear(game_map))

                # Reset timing
                last_update_time = current_time
                half_move_done = False

            deers = remove_deers(deers,player,bears)

        game_screen.update_screen(game_map,player.get_score())
        time.sleep(0.01)
    game_map.print_map()
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
                - Updated timing
                - Changed so only map object passed through to move function
16 October 2025 - Changed so only map object passed through to deer
18 October 2025 - Changed pacman_map to game_map
26 October 2025 - Updated script to handle changes to player object
27 October 2025 - Passed game map to player once
"""