"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 27 November 2025
Version: 1.9
"""

import random
from map import GameMap
import map_characters as char

DIRS = char.DIRS

class Deer:

	def __init__(self,position: tuple[int,int],game_map: GameMap)-> None:
		self.position = position
		self.game_map = game_map
		self.fleeing = False
		self.score = 10
		self.non_blockers = [char.DOT,char.EMPTY,char.WATER]
		self.square = char.EMPTY
		self.height = game_map.get_height()
		self.width = game_map.get_width()

		self.GRAZING_MOVE_CHANCE = 12
		self.WILL_MOVE_LIMIT = 3

	def get_score(self) -> int:
		return self.score

	def get_position(self) -> tuple[int,int]:
		return self.position

	def collides_with(self,encounter: object)->bool:
		return encounter.get_position()==self.position

	def set_position(self,position: tuple[int,int])->bool:
		self.position = position

	def is_fleeing(self)->bool:
		return self.fleeing

	def set_fleeing(self)->None:
		self.fleeing = True

	def stop_fleeing(self)->None:
		self.fleeing = False

	def move_deer(self)->None:
		
		row,col = self.position
		directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

		movement_options,predator_found = self.find_predator()
		movement = random.randint(0,self.GRAZING_MOVE_CHANCE)  # 1 in 4 chance to move when grazing
		
		if (predator_found):
			
			self.set_fleeing()
			for x in range(4):
				if self.game_map.get_tile(directions[x]) not in self.non_blockers:
					movement_options[x] = char.BLOCKED

			can_move = False

			for x in movement_options:
				if x == char.NULL:
					can_move = True
			if can_move:
				found_move = False
				while not found_move:
					movement = random.randint(0,3)
					if movement_options[movement] == char.NULL:
						self.game_map.set_tile(self.position,self.square)
						self.calculate_move(movement)
						found_move = True

		else:
			self.fleeing = False
			if(movement<self.WILL_MOVE_LIMIT):
				self.calculate_move(movement)

	def calculate_move(self,movement: int)->None:

		new_row, new_col = self.position
		new_row, new_col = new_row+DIRS[movement][0],new_col+DIRS[movement][1]

		if new_col>=0 and new_col<self.width and new_row>=0 and new_row<self.height:
			new_position = self.game_map.get_tile((new_row,new_col))
			if (new_position in self.non_blockers):
				if not self.fleeing:
					self.game_map.set_tile(self.position,char.BLANK)
				else:
					self.game_map.set_tile(self.position,self.square)

				self.square = new_position
				self.position = (new_row,new_col)
				self.game_map.set_tile(self.position,char.DEER)
				

	def look_for_predator(self,direction,predator_found)-> tuple[str,bool]:

		found_stop = False
		found_predator = False
		position = 0
		row_pos,col_pos = self.position
		movement = char.NULL

		while not found_stop and position<20:
			position +=1
			row_pos,col_pos = row_pos+DIRS[direction][0],col_pos+DIRS[direction][1]
			found_stop,found_predator = self.check_position(row_pos,col_pos)

		if found_predator:
			predator_found = True
			movement = char.BLOCKED

		return movement,predator_found

	def find_predator(self)-> tuple[int,bool]:

		movement = [char.NULL,char.NULL,char.NULL,char.NULL]
		predator_found = False

		for x in range(4):
			try:
				movement[x],predator_found = self.look_for_predator(x,predator_found)
			except Exception as e: 
				print("Deer ",x)
				print(self.position)
				print(e)

		return movement,predator_found

	def check_position(self,row_pos:int,col_pos:int)->tuple[bool,bool]:
		found_stop = False
		found_predator = False

		if self.game_map.get_tile((row_pos,col_pos)) == char.PLAYER or self.game_map.get_tile((row_pos,col_pos)) == char.BEAR:
			found_stop = True
			found_predator = True
		elif self.game_map.get_tile((row_pos,col_pos)) == char.CAVE_WALL or self.game_map.get_tile((row_pos,col_pos)) == char.FOREST_WALL or self.game_map.get_tile((row_pos,col_pos)) == char.EXIT:
			found_stop = True
		elif row_pos<0 or row_pos>=self.height or col_pos<0 or col_pos>=self.width:
			found_stop = True

		return found_stop,found_predator

"""
16 September 2025 - Created file
4 October 2025 - Added check for predators
7 October 2025 - Updated predetorFound
8 October 2025 - Deer now flees
10 October 2025 - Added code so deer doesn't pick up stuff when fleeing
11 October 2025 - Fixed bug where deer disappears when fleeing
13 October 2025 - Added getter/setter for fleeing
14 October 2025 - Changed check position to collides with bear/player
				- updated the fleeing checks and sets
15 October 2025 - Changed so only map object passed through to move function
16 October 2025 - Fixed issues and set boundaries
17 October 2025 - Added max search distance
3 November 2025 - Started updating class
4 November 2025 - Updated to use file holding constants
26 November 2025 - Updated code to make it tighter
27 November 2025 - Tightened Code to create loops
"""