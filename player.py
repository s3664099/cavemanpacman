"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 18 October 2025
Version: 0.1
"""

SPECIAL_TILES = ["3"]

class Player:

	def __init__(self,row,col):
		self.position = (row,col)
		self.score = 0
		self.running = True
		self.square = " "

	def move_player(self,key,map_data,width,height):

		row,col = self.position
		new_row,new_col = self.position
		non_blockers = ["."," ","d","w","3"]

		if key == "N":
			new_row -=1
		elif key == "S":
			new_row +=1
		elif key == "E":
			new_col +=1
		elif key == "W":
			new_col -=1

		if 0 <= new_row < height and 0 <= new_col < width:
			new_position = map_data[new_row][new_col]

			if (new_position in non_blockers):

				if (new_position=="."):
					self.score += 1
				elif (new_position=="d"):
					self.score += 10
				elif (new_position=="w"):
					self.score += 5


				if self.square in SPECIAL_TILES:
					map_data[row][col] = self.square
				else:
					map_data[row][col] = " "

				self.square = map_data[new_row][new_col]
				map_data[new_row][new_col] = "P"
				self.position = (new_row,new_col)
			elif (new_position == "B"):
				self.running = False
		else:
			self.running = False

		return map_data

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def get_running(self):
		return self.running

	def set_running(self,running):
		self.running = running


"""
18 September 2025 - Created File
18 October 2025 - Added check to preserve maze exit
"""