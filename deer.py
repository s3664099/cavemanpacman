"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 16 September 2025
Version: 0.0

- If sees bear/player moves in opposite direction
"""

import random

class Deer:

	def __init__(self,row,col):
		self.position = (row,col)
		self.fleeing = False
		self.score = 10

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def check_position(self,row,col):
		return (row,col) == self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def move_deer(self,map_data,width):
		non_blockers = ["."," ","w"]
		new_row,new_col = self.position
		row,col = self.position
		movement = random.randint(0,12)

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
			if (new_position in non_blockers):
				map_data[row][col] = " "
				map_data[new_row][new_col]="d"
				self.position = (new_row,new_col)

		return map_data

"""
16 September 2025 - Created file
"""