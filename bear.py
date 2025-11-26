"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 26 November 2025
Version: 1.10
"""

import random
import map_characters as char
from map import GameMap

MAX_SEARCH_DISTANCE = 20
DIRS = char.DIRS

class Bear:

	def __init__(self,bear_position: tuple[int,int], game_map: GameMap) -> None:

		self.position = bear_position
		self.game_map = game_map
		self.chasing = False
		self.square = " "
		self.start = True
		self.has_food = False
		self.movement = 0
		self.width = game_map.get_width()
		self.height = game_map.get_height()

	def get_position(self) -> tuple[int,int]:
		return self.position

	def set_position(self,position: tuple[int,int]) -> None:
		self.position = position

	def get_square(self) -> str:
		return self.square

	def set_square(self,square: str) -> None:
		self.square = square

	def is_chasing(self) -> bool:
		return self.chasing

	def stop_chasing(self) -> None:
		self.chasing = False

	def start_chasing(self) -> None:
		self.chasing = True

	def decide_move(self) -> None:

		row,col = self.position
		move = False

		while not move:
			if self.start:
				move = self._move_toward_entrance(row,col)
			else:
				move = self._chase_or_wander(row,col)

	def _move_toward_entrance(self,row: int, col: int) -> bool:

		cave_entrance_row,cave_entrance_col = self.game_map.get_entrance()
		move = False

		if cave_entrance_col<col and self.game_map.get_tile((row+DIRS[2][0],col+DIRS[2][1])) in char.BEAR_NON_BLOCKERS:
			self._update_position((row+DIRS[2][0],col+DIRS[2][1]))
			move = True
		elif cave_entrance_row<row and self.game_map.get_tile((row+DIRS[0][0],col+DIRS[0][1])) in char.BEAR_NON_BLOCKERS:
			self._update_position((row+DIRS[0][0],col+DIRS[0][1]))
			move = True
		elif cave_entrance_row>row and self.game_map.get_tile((row+DIRS[1][0],col+DIRS[1][1])) in char.BEAR_NON_BLOCKERS:
			self._update_position((row+DIRS[1][0],col+DIRS[1][1]))
			move = True
		elif cave_entrance_col>col and self.game_map.get_tile((row+DIRS[3][0],col+DIRS[3][1])) in char.BEAR_NON_BLOCKERS:
			self._update_position((row+DIRS[3][0],col+DIRS[3][1]))
			move = True
		else:
			move = True

		if cave_entrance_row==row and cave_entrance_col==col:
			self.start = False
			move = True

		return move

	def _chase_or_wander(self,row:int,col:int) -> bool:
		movement = self._find_prey()

		if (movement == -1):
			movement = self._determine_movement()
		else:
			self.start_chasing()
		self._update_position((row+DIRS[movement][0],col+DIRS[movement][1]))

		move = True
		self.movement = movement
		return move

	def _find_prey(self) -> int:

		movement = -1
		distance = 0

		#Search all four directions using the helper
		directions = [
			(-1,0,0), # North
			(1,0,1), # South
			(0,-1,2), # West
			(0,1,3) # East
		]

		for row_delta,col_delta,dir_code in directions:
			try:
				new_movement,new_distance = self._search_direction(
					row_delta,col_delta,dir_code)
				movement,distance = self.check_move(new_movement,movement,new_distance,distance)
			except Exception as e:
				print("Bear direction {} error at {}: {}".format(dir_code,self.position,e))

		return movement

	def _determine_movement(self) -> int:

		movement_options = [char.NULL,char.NULL,char.NULL,char.NULL]
		valid_move = False
		movement = 0
		row,col = self.position

		if (self.game_map.get_tile((row+DIRS[0][0],col+DIRS[0][1])) not in char.BEAR_NON_BLOCKERS_SANS_ENTRANCE) or self.movement ==1:
			movement_options[char.NORTH] = char.BLOCKED

		if (self.game_map.get_tile((row+DIRS[1][0],col+DIRS[1][1])) not in char.BEAR_NON_BLOCKERS_SANS_ENTRANCE) or self.movement ==0:
			movement_options[char.SOUTH] = char.BLOCKED

		if (self.game_map.get_tile((row+DIRS[2][0],col+DIRS[2][1])) not in char.BEAR_NON_BLOCKERS_SANS_ENTRANCE) or self.movement ==3:
			movement_options[char.WEST] = char.BLOCKED

		if (self.game_map.get_tile((row+DIRS[3][0],col+DIRS[3][1])) not in char.BEAR_NON_BLOCKERS_SANS_ENTRANCE) or self.movement ==2:
			movement_options[char.EAST] = char.BLOCKED

		while not valid_move:
			movement = random.randint(0,3)

			if char.NULL not in movement_options:
				print("Don't Move",self.position)
				movement = -1
				valid_move = True
			elif movement_options[movement] != char.BLOCKED:
				valid_move = True

		return movement

	def _search_direction(self,row_delta: int,col_delta: int,direction:int) -> tuple[int,int]:
		found_stop = False
		position = 0
		new_movement = -1
		distance = 0
		row,col = self.position

		while not found_stop and position < MAX_SEARCH_DISTANCE:
			position+=1
			check_row = row + (row_delta*position)
			check_col = col + (col_delta*position)
			found_stop,new_movement,distance = self.check_position(check_row,check_col,position,direction)

		return new_movement,distance

	def check_position(self,row:int,col:int,position: int,direction: int) -> tuple[bool,int,int]:

		found_stop = False
		movement = -1
		distance = 0

		if self.game_map.get_tile((row,col)) in [char.FOREST_WALL,char.CAVE_WALL,char.EXIT]:
			found_stop = True
		elif self.game_map.get_tile((row,col)) in [char.PLAYER,char.DEER]:
			found_stop = True
			movement = direction
			distance = position
		elif row<0 or row>=self.height or col<0 or col>=self.width:
			found_stop = True
			print("Exceeds bounds")

		return found_stop,movement,distance

	def check_move(self,new_movement: int,movement:int,position:int,distance:int)-> tuple[int,int]:

		if new_movement != -1:
			if position<distance:
				movement = new_movement
				distance = position
			elif movement == -1:
				movement = new_movement
				distance = position

		return movement,distance

	def _update_position(self,new_positon: tuple[int,int]) -> None:
		self.game_map.set_tile(self.position,self.square)
		self.square = self.game_map.get_tile(new_positon)

		if (self.square==char.DEER):
			self.square = char.EMPTY

		self.game_map.set_tile(new_positon,char.BEAR)
		self.position = new_positon

"""
17 September 2025 - Created file
23 September 2025 - Added movement of bear out of cave
28 September 2025 - Added movement of bear so only moves forward.
2 October 2025 - Added movement to prey
3 October 2025 - Made bear move faster if sees prey
4 October 2025 - Removed second check position
10 October 2025 - Removed some of the prints
13 October 2025 - Added further details for errors
15 October 2025 - Update bear chasing routine to make it clearer
				- Changed so only map object passed through to move function
16 October 2025 - Added boundaries for search
17 October 2025 - Added search limit and fixed error reporting
18 October 2025 - Updated some code, and added section if bear not moving
27 October 2025 - Updated with single instance of game map and added hints
1 November 2025 - Started updating passing tuples for position
2 November 2025 - Finalised moving row,col to tuples
4 November 2025 - Updated to use file holding constants
20 November 2025 - Moved code into a move_toward_entrance function
21 November 2025 - Updated function names
23 November 2025 - Moved non-blockers out
25 November 2025 - Removed null strings and started updated the movements methods
26 November 2025 - Fixed errors
"""