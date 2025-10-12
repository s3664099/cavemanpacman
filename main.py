"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 12 October 2025
Version: 0.11

- Deer flees faster (add it also where bear chases)
- see what Deepseek thinks (good, bad, ugly)
"""

from map import PacmanMap
from deer import Deer
from bear import Bear
from player import Player
from display import View
import control
import time

half_move_counter = 0.5
move_counter = 1
 
def remove_deers(deers,player,bears):
    update_deers = []
    for deer in deers:
        add_deer = True
        if deer.check_current_position(player.get_position()[0],player.get_position()[1]):
            add_deer = False

        for bear in bears:
            if (deer.check_current_position(bear.get_position()[0],bear.get_position()[1])):
                add_deer = False

        if add_deer:
            update_deers.append(deer)

    return update_deers

def pause(action,player):
    pause = False

    if action == "P":
        pause = True
    while(pause):
        action = control.get_keypress()
        if action == "P" or action == "Q":
            pause = False
        quit(action,player)

def quit(action,player):
    if action == "Q":
        player.set_running(False)


def main():
    pacman_map = PacmanMap("map.txt")
    game_screen = View(pacman_map.get_dimensions())
    game_screen.update_screen(pacman_map,0)
    base_time = time.time()

    deers = []
    bears = []

    player = Player(pacman_map.get_player()[0],pacman_map.get_player()[1])

    for deer in pacman_map.get_deers():
        deers.append(Deer(deer[0],deer[1]))

    for bear in pacman_map.get_bears():
        bears.append(Bear(bear[0],bear[1]))


    while(player.get_running()):
        action = control.get_keypress()
        quit(action,player)
        pause(action,player)
        pacman_map.set_map(player.move_player(action,pacman_map.get_map(),pacman_map.get_width()))
        game_screen.update_screen(pacman_map,player.get_score())
        
        current_time = time.time()

        if (current_time-base_time>half_move_counter) and (current_time-base_time<move_counter):
            for bear in bears:
                if (bear.get_chasing()):
                    pacman_map.set_map(bear.move_bear(pacman_map.get_map(),pacman_map.get_width(),pacman_map.get_entrance()))
                    bear.set_chasing(False)

        elif (current_time-base_time>move_counter):
            base_time = current_time

            dear_no = 0
            for deer in deers:
                dear_no +=1
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
"""