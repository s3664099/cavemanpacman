"""
File: Caveman Pacman Player
Author: David Sarkies
Initial: 18 September 2025
Update: 31 October 2025
Version: 1.5
"""

from map import GameMap
import map_characters as char

class Player:

	SPECIAL_TILES: list[str] = [char.EXIT]
	SCORE_VALUES: dict[str,int] = {".": 1, "d": 10, "w": 5}

	MOVE_KEYS: dict[str,tuple[int,int]] = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

	STATE_RUNNING = "running"
	STATE_DEAD = "dead"
	STATE_ESCAPED = "escaped"
	STATE_END =  "ended"

	PLAYER_NON_BLOCKERS = [
		char.DOT,
		char.EMPTY,
		char.DEER,
		char.WATER,
		char.EXIT
	]

	def __init__(self,game_map: GameMap) -> None:
		self.position = game_map.get_player()
		self.map = game_map
		self.score = 0
		self.state = self.STATE_RUNNING
		self.underlying_tile = self.map.get_tile(self.position)

	def move_player(self,key: str) -> None:

		new_position = self.get_new_position(key)

		if self.state == self.STATE_RUNNING:
			self.process_move(new_position)
	
	def get_new_position(self,key: str) -> tuple[int,int]:
		
		delta = self.MOVE_KEYS.get(key,(0,0))
		new_row,new_col = self.position
		return (new_row+delta[0],new_col+delta[1])

	def process_move(self,new_position: tuple[int,int]) -> None:

		if self.is_within_bounds(new_position):
			new_tile = self.map.get_tile(new_position)
			self.process_tile_interaction(new_position,new_tile)
		else:
			self.state = self.STATE_ESCAPED

	def is_within_bounds(self,new_position: tuple[int,int]) -> bool:
		row,col = new_position
		within = (0 <= row<self.map.get_height()) and (0<= col<self.map.get_width())
		return within

	def process_tile_interaction(self,new_position: tuple[int,int],new_tile: str) -> None:

		if new_tile in self.PLAYER_NON_BLOCKERS:
			self.update_score(new_tile)
			self.update_map_tiles(new_position)
		elif new_tile == char.BEAR:
			self.state = self.STATE_DEAD

	def update_map_tiles(self,new_position: tuple[int,int]) -> None:

		if self.underlying_tile in self.SPECIAL_TILES:
			self.map.set_tile(self.position,self.underlying_tile)
		else:
			self.map.set_tile(self.position,char.EMPTY)

		self.underlying_tile = self.map.get_tile(new_position)
		self.map.set_tile(new_position,char.PLAYER)
		self.position = new_position

	def update_score(self,new_position: str) -> None:
		if new_position in self.SCORE_VALUES:
			self.score += self.SCORE_VALUES[new_position]

	def get_score(self) -> int:
		return self.score

	def get_position(self) -> tuple[int,int]:
		return self.position

	def is_running(self) -> bool:
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
27 October 2025 - Removed GameMap from being passed in
31 October 2025 - Finalised passing tuples
"""