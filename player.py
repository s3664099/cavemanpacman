"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 18 September 2025
Version: 0.0
"""

class Player:

	def __init__(self,row,col):
		self.position = (row,col)
		self.score = 0
		self.running = True

	def move_player(self,key,map_data,width):

		row,col = self.position
		new_row,new_col = self.position
		non_blockers = ["."," ","d","w","/"]

		if key == "N":
			new_row -=1
		elif key == "S":
			new_row +=1
		elif key == "E":
			new_col +=1
		elif key == "W":
			new_col -=1

		if (new_col<width):
			new_position = map_data[new_row][new_col]

			if (new_position in non_blockers):

				if (map_data[new_row][new_col]=="."):
					self.score += 1
				elif (map_data[new_row][new_col]=="d"):
					self.score += 10
				elif (map_data[new_row][new_col]=="w"):
					self.score += 5

				map_data[row][col] = " "
				map_data[new_row][new_col] = "P"
				self.position = (new_row,new_col)
			elif (new_position == "B"):
				self.running = False
		elif (new_row,new_col == 9,25):
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
"""