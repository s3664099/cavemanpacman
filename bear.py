"""
File: Caveman Pacman Bear
Author: David Sarkies
Initial: 17 September 2025
Update: 17 September 2025
Version: 0.0
"""

import random

class Bear:

	def __init__(self,row,col):

		self.position = (row,col)
		self.chasing = False
		self.square = " "

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

	def move_bear(self,map_data,width):

		non_blockers = ["."," ","w","P","d"]
		new_row,new_col = self.position
		row,col = self.position
		move = False

		while not move:
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
					map_data[row][col] = self.square
					self.square = map_data[new_row][new_col]
					map_data[new_row][new_col]="B"
					self.position = (new_row,new_col)
					move = True
			return map_data


"""
17 September 2025 - Created file
"""