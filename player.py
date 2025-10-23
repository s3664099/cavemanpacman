"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 23 October 2025
Version: 0.2
"""

class Player:

	SPECIAL_TILES = ["3"]
	TILE_EMPTY = " "
	TILE_DOT = "."
	TILE_DEER = "d"
	TILE_WALL = "#"
	TILE_EXIT = "3"
	TILE_BEAR = "B"
	TILE_WATER = "w"
	TILE_PLAYER = "P"
	SCORE_VALUES = {".": 1, "d": 10, "w": 5}
	NON_BLOCKERS = [TILE_DOT,TILE_EMPTY,TILE_DEER,TILE_WATER,TILE_EXIT]

	def __init__(self,row,col):
		self.position = (row,col)
		self.score = 0
		self.running = True
		self.underlying_tile = " "

	def move_player(self,key,map_data,width,height):

		row,col = self.position
		new_row,new_col = self.get_new_position(row,col,key)
		map_data = self.can_move_to(row,col,new_row,new_col,height,width,map_data)
		
		return map_data

	def get_new_position(self,row,col,key):
		new_row,new_col = row,col
		
		if key == "N":
			new_row -=1
		elif key == "S":
			new_row +=1
		elif key == "E":
			new_col +=1
		elif key == "W":
			new_col -=1

		return new_row,new_col

	def can_move_to(self,row,col,new_row,new_col,height,width,map_data):

		if 0 <= new_row < height and 0 <= new_col < width:
			new_position = map_data[new_row][new_col]

			if new_position in self.NON_BLOCKERS:

				self.update_score(new_position)

				if self.underlying_tile in self.SPECIAL_TILES:
					map_data[row][col] = self.underlying_tile
				else:
					map_data[row][col] = self.TILE_EMPTY

				self.underlying_tile = map_data[new_row][new_col]
				map_data[new_row][new_col] = self.TILE_PLAYER
				self.position = (new_row,new_col)
			elif (new_position == self.TILE_BEAR):
				self.running = False
		else:
			self.running = False

		return map_data

	def update_score(self,new_position):

		if new_position in self.SCORE_VALUES:
			self.score += self.SCORE_VALUES[new_position]

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
23 October 2025 - Updated code to made it more maintainable
"""