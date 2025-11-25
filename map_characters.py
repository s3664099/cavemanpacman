"""
File: Caveman Pacman Characters
Author: David Sarkies
Initial: 4 November 2025
Update: 4 November 2025
Version: 1.0
"""

# --- Map Character Constants ---

# Entities
PLAYER = "P"
DEER = "d"
BEAR = "B"

# Terrain
ENTRANCE = "#"
EXIT = "3"
CAVE_WALL = "2"
FOREST_WALL = "1"

# Environment
WATER = "w"
EMPTY = " "
BLANK = " "
DOT = "."
BLOCKED = "X"

# Directons
NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

NULL = ""

BEAR_NON_BLOCKERS = [DOT,EMPTY,WATER,PLAYER,DEER,ENTRANCE]
BEAR_NON_BLOCKERS_SANS_ENTRANCE = [DOT,EMPTY,WATER,PLAYER,DEER]



"""
4 November 2025 - Created File
"""