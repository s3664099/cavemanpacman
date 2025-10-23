"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 23 October 2025
Version: 0.2

- Add hints and then recommend changes
"""

class Player:

	TILE_EMPTY = " "
	TILE_DOT = "."
	TILE_DEER = "d"
	TILE_WALL = "#"
	TILE_EXIT = "3"
	TILE_BEAR = "B"
	TILE_WATER = "w"
	TILE_PLAYER = "P"

	SPECIAL_TILES = [TILE_EXIT]
	SCORE_VALUES = {".": 1, "d": 10, "w": 5}

	MOVE_KEYS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

	STATE_RUNNING = "running"
	STATE_DEAD = "dead"
	STATE_ESCAPED = "escaped"

	def __init__(self,row,col):
		self.position = (row,col)
		self.score = 0
		self.state = self.STATE_RUNNING
		self.underlying_tile = self.TILE_EMPTY

	def move_player(self,key,map_data,width,height):

		row,col = self.position
		new_row,new_col = self.get_new_position(row,col,key)

		if self.state == self.STATE_RUNNING:
			map_data = self.process_move(row,col,new_row,new_col,height,width,map_data)
		
		return map_data

	def get_new_position(self,row,col,key):
		new_row,new_col = row,col
		
		delta = self.MOVE_KEYS.get(key,(0,0))
		new_row = row+delta[0]
		new_col = col+delta[1]

		return new_row,new_col

	def process_move(self,row,col,new_row,new_col,height,width,map_data):

		if self.is_within_bounds(new_row,new_col,height,width):
			new_position = map_data[new_row][new_col]
			map_data = self.process_tile_interaction(row,col,new_row,new_col,new_position,map_data)
		else:
			self.state = self.STATE_ESCAPED

		return map_data

	def is_within_bounds(self,row,col,height,width):
		within = (0 <= row<height) and (0<= col<width)
		return within

	def process_tile_interaction(self,row,col,new_row,new_col,new_tile,map_data):

		non_blockers = [
			self.TILE_DOT,
			self.TILE_EMPTY,
			self.TILE_DEER,
			self.TILE_WATER,
			self.TILE_EXIT
		]

		if new_tile in non_blockers:
			self.update_score(new_tile)
			map_data = self.update_map_tiles(row,col,new_row,new_col,map_data)
		elif new_tile == self.TILE_BEAR:
			self.state = self.STATE_DEAD

		return map_data

	def update_map_tiles(self,old_row,old_col,new_row,new_col,map_data):

		if self.underlying_tile in self.SPECIAL_TILES:
			map_data[old_row][old_col] = self.underlying_tile
		else:
			map_data[old_row][old_col] = self.TILE_EMPTY

		self.underlying_tile = map_data[new_row][new_col]
		map_data[new_row][new_col] = self.TILE_PLAYER
		self.position = (new_row,new_col)

		return map_data

	def update_score(self,new_position):
		if new_position in self.SCORE_VALUES:
			self.score += self.SCORE_VALUES[new_position]

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def get_running(self):
		return self.state == self.STATE_RUNNING

	def set_running(self,running):
		if running:
			self.state = self.STATE_RUNNING
		else:
			self.state = self.STATE_DEAD


"""
18 September 2025 - Created File
18 October 2025 - Added check to preserve maze exit
23 October 2025 - Updated code to made it more maintainable
"""