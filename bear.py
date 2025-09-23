"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 23 September 2025
Version: 0.1

Bear Movement
	- if in cave - moves towards exit. If other bear in way, pauses
	- when outside will move forward only (first will not be back into the cave)
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
				movement = random.randint(0,3)
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
		return map_data

	def bear_move(self,map_data,row,col,new_row,new_col):
		map_data[row][col] = self.square
		self.square = map_data[new_row][new_col]
		map_data[new_row][new_col]="B"
		self.position = (new_row,new_col)
		return map_data


"""
17 September 2025 - Created file
23 September 2025 - Added movement of bear out of cave
"""