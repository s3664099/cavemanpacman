"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 4 November 2025
Version: 1.5
"""

import random
import map_characters as char
from map import GameMap

MAX_SEARCH_DISTANCE = 20
MOVEABLE_SPACE = ""

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

	def move_bear(self) -> None:

		entrance = self.game_map.get_entrance()
		non_blockers = [char.DOT,char.EMPTY,char.WATER,char.PLAYER,char.DEER,char.ENTRANCE]
		row,col = self.position
		directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
		move = False

		while not move:

			if self.start:

				cave_entrance_row,cave_entrance_col = entrance
				if cave_entrance_col<col and self.game_map.get_tile(directions[2]) in non_blockers:
					self.bear_move(directions[2])
					move = True
				elif cave_entrance_row<row and self.game_map.get_tile(directions[0]) in non_blockers:
					self.bear_move(directions[0])
					move = True
				elif cave_entrance_row>row and self.game_map.get_tile(directions[1]) in non_blockers:
					self.bear_move(directions[1])
					move = True
				elif cave_entrance_col>col and self.game_map.get_tile(directions[3]) in non_blockers:
					self.bear_move(directions[3])
					move = True
				else:
					move = True

				if cave_entrance_row==row and cave_entrance_col==col:
					self.start = False
			else:

				movement = self.find_prey()

				if (movement == -1):
					movement = self.determine_movement()
				else:
					self.start_chasing()

				map_data = self.bear_move(directions[movement])
				move = True
				self.movement = movement
	
	def search_direction(self,row_delta: int,col_delta: int,direction:int) -> tuple[int,int]:
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

	def find_prey(self) -> int:

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
				new_movement,new_distance = self.search_direction(
					row_delta,col_delta,dir_code)
				movement,distance = self.check_move(new_movement,movement,new_distance,distance)
			except Exception as e:
				print("Bear direction {} error at {}: {}".format(dir_code,self.position,e))

		return movement

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

	def determine_movement(self) -> int:

		movement_options = ["","","",""]
		non_blockers = [char.DOT,char.EMPTY,char.WATER,char.PLAYER,char.DEER]
		valid_move = False
		movement = 0
		row,col = self.position
		directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

		if (self.game_map.get_tile(directions[0]) not in non_blockers) or self.movement ==1:
			movement_options[0] = char.BLOCKED

		if (self.game_map.get_tile(directions[1]) not in non_blockers) or self.movement ==0:
			movement_options[1] = char.BLOCKED

		if (self.game_map.get_tile(directions[2]) not in non_blockers) or self.movement ==3:
			movement_options[2] = char.BLOCKED

		if (self.game_map.get_tile(directions[3]) not in non_blockers) or self.movement ==2:
			movement_options[3] = char.BLOCKED

		while not valid_move:
			movement = random.randint(0,3)

			if MOVEABLE_SPACE not in movement_options:
				print("Don't Move",self.position)
				movement = -1
				valid_move = True
			elif movement_options[movement] != char.BLOCKED:
				valid_move = True

		return movement

	def bear_move(self,new_positon: tuple[int,int]) -> None:
		
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
"""