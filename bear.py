"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 28 September 2025
Version: 0.2

Bear Movement
	- if sees 
	- if lands on deer will move back to the cave.
"""

import random

class Bear:

	def __init__(self,row,col):

		self.position = (row,col)
		self.chasing = False
		self.square = " "
		self.start = True
		self.has_food = False
		self.movement = 0

	def get_position(self):
		return self.position

	def check_position(self,row,col):
		return (row,col) == self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def get_square(self):
		return self.square

	def set_square(self,square):
		self.square = square

	def move_bear(self,map_data,width,entrance):

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

				movement = self.determine_movement(map_data,row,col)
				new_row,new_col = row,col

				if (movement == 0):
					new_row -=1
				elif (movement == 1):
					new_row +=1
				elif (movement == 2):
					new_col -=1
				elif (movement == 3):
					new_col +=1

				if (new_col<width):
					new_position = map_data[new_row][new_col]
					if(new_position in non_blockers):
						map_data = self.bear_move(map_data,row,col,new_row,new_col)
						move = True
						self.movement = movement
		return map_data

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
			if movement_options[movement] != "X":
				valid_move = True

		return movement

	def bear_move(self,map_data,row,col,new_row,new_col):
		map_data[row][col] = self.square
		self.square = map_data[new_row][new_col]
		map_data[new_row][new_col]="B"
		self.position = (new_row,new_col)
		return map_data


"""
17 September 2025 - Created file
23 September 2025 - Added movement of bear out of cave
28 September 2025 - Added movement of bear so only moves forward.
"""