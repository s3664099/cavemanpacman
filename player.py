"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 26 October 2025
Version: 0.4

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

	SPECIAL_TILES: list[str] = [TILE_EXIT]
	SCORE_VALUES: dict[str,int] = {".": 1, "d": 10, "w": 5}

	MOVE_KEYS: dict[str,tuple[int,int]] = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

	STATE_RUNNING = "running"
	STATE_DEAD = "dead"
	STATE_ESCAPED = "escaped"
	STATE_END =  "ended"

	PLAYER_NON_BLOCKERS = [
		TILE_DOT,
		TILE_EMPTY,
		TILE_DEER,
		TILE_WATER,
		TILE_EXIT
	]

	def __init__(self,row: int,col: int) -> None:
		self.position = (row,col)
		self.map = None
		self.score = 0
		self.state = self.STATE_RUNNING
		self.underlying_tile = self.TILE_EMPTY

	def move_player(self,key: str,game_map: object) -> None:

		self.map = game_map
		row,col = self.position
		new_row,new_col = self.get_new_position(row,col,key)

		if self.state == self.STATE_RUNNING:
			self.process_move(row,col,new_row,new_col)

		return self.map
	
	def get_new_position(self,row: int,col: int,key: str) -> tuple[int,int]:
		new_row,new_col = row,col
		
		delta = self.MOVE_KEYS.get(key,(0,0))
		new_row = row+delta[0]
		new_col = col+delta[1]

		return new_row,new_col

	def process_move(self,row: int,col: int,new_row: int,new_col: int) -> None:

		if self.is_within_bounds(new_row,new_col):
			new_tile = self.map.get_tile(new_row,new_col)
			self.process_tile_interaction(row,col,new_row,new_col,new_tile)
		else:
			self.state = self.STATE_ESCAPED

	def is_within_bounds(self,row: int,col) -> bool:
		within = (0 <= row<self.map.get_height()) and (0<= col<self.map.get_width())
		return within

	def process_tile_interaction(self,row:int,col:int,new_row:int,new_col:int,new_tile: str):

		if new_tile in self.PLAYER_NON_BLOCKERS:
			self.update_score(new_tile)
			self.update_map_tiles(row,col,new_row,new_col)
		elif new_tile == self.TILE_BEAR:
			self.state = self.STATE_DEAD

	def update_map_tiles(self,old_row: int,old_col:int,new_row:int,new_col:int):

		if self.underlying_tile in self.SPECIAL_TILES:
			self.map.set_tile(old_row,old_col,self.underlying_tile)
		else:
			self.map.set_tile(old_row,old_col,self.TILE_EMPTY)

		self.underlying_tile = self.map.get_tile(new_row,new_col)
		self.map.set_tile(new_row,new_col,self.TILE_PLAYER)
		self.position = (new_row,new_col)

	def update_score(self,new_position: str) -> None:
		if new_position in self.SCORE_VALUES:
			self.score += self.SCORE_VALUES[new_position]

	def get_score(self) -> int:
		return self.score

	def get_position(self) -> tuple[int,int]:
		return self.position

	def get_running(self) -> bool:
		return self.state == self.STATE_RUNNING

	def set_end(self):
		self.state = self.STATE_END

	def set_state_dead(self) -> None:
		self.state = self.STATE_DEAD


"""
18 September 2025 - Created File
18 October 2025 - Added check to preserve maze exit
23 October 2025 - Updated code to made it more maintainable
24 October 2025 - Added hints to functions
26 October 2025 - Removed the game map being passed around to a simple game map that is stored
				  and returned when the player moves
				  Moved the map object instead of the map
"""