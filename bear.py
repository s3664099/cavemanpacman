"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 18 October 2025
Version: 0.11
"""

import random

MAX_SEARCH_DISTANCE = 20
MOVEABLE_SPACE = ""

class Bear:

	def __init__(self,row,col):

		self.position = (row,col)
		self.chasing = False
		self.square = " "
		self.start = True
		self.has_food = False
		self.movement = 0
		self.width = -1
		self.height = -1

	def get_position(self):
		return self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def get_square(self):
		return self.square

	def set_square(self,square):
		self.square = square

	def is_chasing(self):
		return self.chasing

	def stop_chasing(self):
		self.chasing = False

	def start_chasing(self):
		self.chasing = True

	def move_bear(self,pacman_map):
		map_data = pacman_map.get_map()
		self.width = pacman_map.get_width()
		self.height = pacman_map.get_height()
		entrance = pacman_map.get_entrance()

		non_blockers = ["."," ","w","P","d","#"]
		new_row,new_col = self.position
		row,col = self.position
		move = False

		while not move:

			if self.start:

				cave_entrance_row,cave_entrance_col = entrance
				if cave_entrance_col<col and map_data[row][col-1] in non_blockers:
					map_data = self.bear_move(map_data,row,col,row,col-1)
					move = True
				elif cave_entrance_row<row and map_data[row-1][col] in non_blockers:
					map_data = self.bear_move(map_data,row,col,row-1,col)
					move = True
				elif cave_entrance_row>row and map_data[row+1][col] in non_blockers:
					map_data = self.bear_move(map_data,row,col,row+1,col)
					move = True
				elif cave_entrance_col>col and map_data[row][col+1] in non_blockers:
					map_data = self.bear_move(map_data,row,col,row,col+1)
					move = True
				else:
					move = True

				if cave_entrance_row==row and cave_entrance_col==col:
					self.start = False
			else:

				movement = self.find_prey(map_data,row,col)

				if (movement == -1):
					movement = self.determine_movement(map_data,row,col)
					new_row,new_col = row,col
				else:
					self.start_chasing()

				if (movement == 0):
					new_row -=1
				elif (movement == 1):
					new_row +=1
				elif (movement == 2):
					new_col -=1
				elif (movement == 3):
					new_col +=1

				map_data = self.bear_move(map_data,row,col,new_row,new_col)
				move = True
				self.movement = movement
		
		return map_data

	def search_direction(self,map_data,row,col,row_delta,col_delta,direction):
		found_stop = False
		position = 0
		new_movement = -1
		distance = 0

		while not found_stop and position < MAX_SEARCH_DISTANCE:
			position+=1
			check_row = row + (row_delta*position)
			check_col = col + (col_delta*position)
			found_stop,new_movement,distance = self.check_position(map_data,check_row,check_col,position,direction)

		return new_movement,distance

	def find_prey(self,map_data,row,col):

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
					map_data,row,col,row_delta,col_delta,dir_code)
				movement,distance = self.check_move(new_movement,movement,new_distance,distance)
			except Exception as e:
				print(f"Bear direction {dir_code} error at ({row}, {col}): {e}")

		return movement

	def check_position(self,map_data,row,col,position,direction):

		found_stop = False
		movement = -1
		distance = 0

		if map_data[row][col] == "1" or map_data[row][col] == "2" or map_data[row][col] == "3":
			found_stop = True
		elif map_data[row][col] == "P" or map_data[row][col] == "d":
			found_stop = True
			movement = direction
			distance = position
		elif row<0 or row>=self.height or col<0 or col>=self.width:
			found_stop = True
			print("Exceeds bounds")

		return found_stop,movement,distance

	def check_move(self,new_movement,movement,position,distance):

		if new_movement != -1:
			if position<distance:
				movement = new_movement
				distance = position
			elif movement == -1:
				movement = new_movement
				distance = position

		return movement,distance

	def determine_movement(self,map_data,row,col):

		movement_options = ["","","",""]
		non_blockers = ["."," ","w","P","d"]
		valid_move = False
		movement = 0

		if ((map_data[row-1][col]) not in non_blockers) or self.movement ==1:
			movement_options[0] = "X"

		if ((map_data[row+1][col]) not in non_blockers) or self.movement ==0:
			movement_options[1] = "X"

		if ((map_data[row][col-1]) not in non_blockers) or self.movement ==3:
			movement_options[2] = "X"

		if ((map_data[row][col+1]) not in non_blockers) or self.movement ==2:
			movement_options[3] = "X"

		while not valid_move:
			movement = random.randint(0,3)

			if MOVEABLE_SPACE not in movement_options:
				print("Don't Move",self.position)
				movement = -1
				valid_move = True
			elif movement_options[movement] != "X":
				valid_move = True

		return movement

	def bear_move(self,map_data,row,col,new_row,new_col):
		map_data[row][col] = self.square
		self.square = map_data[new_row][new_col]

		if (self.square=="d"):
			self.square = " "

		map_data[new_row][new_col]="B"
		self.position = (new_row,new_col)
		return map_data

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
"""