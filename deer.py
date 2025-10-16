"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 16 October 2025
Version: 0.9
"""

import random

class Deer:

	def __init__(self,row,col):
		self.position = (row,col)
		self.fleeing = False
		self.score = 10
		self.non_blockers = ["."," ","w"]
		self.square = " "
		self.north = 0
		self.south = 1
		self.west = 2
		self.east = 3
		self.height = -1
		self.width = -1

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def collides_with(self,encounter):
		return (encounter.get_position()[0],encounter.get_position()[1]) ==self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def is_fleeing(self):
		return self.fleeing

	def set_fleeing(self):
		self.fleeing = True

	def stop_fleeing(self):
		self.fleeing = False

	def move_deer(self,pacman_map):
		map_data = pacman_map.get_map()
		self.width = pacman_map.get_width()
		self.height = pacman_map.get_height()

		new_row,new_col = self.position
		row,col = self.position

		movement_options,predator_found = self.find_predator(map_data,row,col)
		movement = random.randint(0,12)

		if (predator_found):

			self.set_fleeing()
			if map_data[row-1][col] not in self.non_blockers:
				movement_options[self.north] = "X"
			if map_data[row+1][col] not in self.non_blockers:
				movement_options[self.south] = "X"
			if map_data[row][col-1] not in self.non_blockers:
				movement_options[self.west] = "X"
			if map_data[row][col+1] not in self.non_blockers:
				movement_options[self.east] = "X"

			can_move = False

			for x in movement_options:
				if x == "":
					can_move = True
			if can_move:
				found_move = False
				while not found_move:
					movement = random.randint(0,3)
					if movement_options[movement] == "":
						map_data[row][col] = self.square
						map_data = self.calculate_move(movement,map_data,row,col)
						found_move = True

		else:
			self.fleeing = False
			map_data = self.calculate_move(movement,map_data,row,col)

		return map_data

	def calculate_move(self,movement,map_data,row,col):

		new_row = row
		new_col = col

		if (movement == self.north):
			new_row -=1
		elif (movement == self.south):
			new_row +=1
		elif (movement == self.west):
			new_col -=1
		elif (movement == self.east):
			new_col +=1

		if new_col>=0 and new_col<self.width and new_row>=0 and new_row<self.height:
			new_position = map_data[new_row][new_col]
			if (new_position in self.non_blockers):
				if not self.fleeing:
					map_data[row][col] = " "

				self.square = map_data[new_row][new_col]
				map_data[new_row][new_col]="d"
				self.position = (new_row,new_col)
		return map_data

	def look_for_predator(self,map_data,row,col,direction,predator_found):

		found_stop = False
		position = 0
		row_pos = 0
		col_pos = 0
		movement = ""

		while not found_stop:
			if direction == self.north:
				row_pos -=1
			elif direction == self.south:
				row_pos +=1
			elif direction == self.west:
				col_pos -=1
			else:
				col_pos +=1

			position +=1
			found_stop,found_predator = self.check_position(map_data,row+row_pos,col+col_pos,position,0)
		if found_predator:
			movement = "X"
			predator_found = True

		return movement,predator_found

	def find_predator(self,map_data,row,col):

		movement = ["","","",""]
		predator_found = False

		try:
			movement[self.north],predator_found = self.look_for_predator(map_data,row,col,self.north,predator_found)
		except Exception as e: 
			print("Deer North")
			print(row,col)
			print(e)

		try:
			movement[self.south],predator_found = self.look_for_predator(map_data,row,col,self.south,predator_found)
		except Exception as e:
			print("Deer South")
			print(row,col)
			print(e)

		try:
			movement[self.west],predator_found = self.look_for_predator(map_data,row,col,self.west,predator_found)
		except Exception as e:
			print("Deer West")
			print(row,col)
			print(e)

		try:
			movement[self.east],predator_found = self.look_for_predator(map_data,row,col,self.east,predator_found)
		except Exception as e:
			print("Deer East")
			print(row,col)
			print(e)

		return movement,predator_found

	def check_position(self,map_data,row,col,position,direction):
		found_stop = False
		found_predator = False

		if map_data[row][col] == "P" or map_data[row][col] == "B":
			found_stop = True
			found_predator = True
		elif map_data[row][col] == "1" or map_data[row][col] == "2" or map_data[row][col] == "/":
			found_stop = True
		elif row<0 or row>=self.height or col<0 or col>=self.width:
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

"""