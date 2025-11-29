"""
File: Caveman Pacman Display 
Author: David Sarkies
Initial: 6 September 2025
Update: 29 November 2025
Version: 2.0
"""

import pygame
import map_characters as char
import os

class View:

	CELL_SIZE = 30
	SCORE_BAR_HEIGHT = 30
	FONTSIZE = 24
	SCORE_BAR_COLOUR = (50, 50, 50)
	SCORE_TEXT_COLOUR = (255, 255, 255)
	BACKGROUND_COLOUR = (0,0,0)

	ICON_DIR = os.path.join(os.path.dirname(__file__), "icons")
	CAVEWOMAN = "cavewoman.png"
	BEAR = "bear.png"
	DEER = "deer.png"
	FOREST = "forest.png"
	RASPBERRY = "raspberry.png"
	WALL = "wall.png"
	PUDDLE = "puddle.png"

	def __init__ (self,dimensions):

		pygame.init()

		self.width = dimensions[0]
		self.height = dimensions[1]
		self.screen = pygame.display.set_mode((self.width*self.CELL_SIZE, (self.height+1)*self.CELL_SIZE))
		pygame.display.set_caption("Caveman Pacman")
		self.player = self.load_icon(self.CAVEWOMAN, self.CELL_SIZE)
		self.bear = self.load_icon(self.BEAR, self.CELL_SIZE)
		self.deer = self.load_icon(self.DEER, self.CELL_SIZE)	
		self.forest = self.load_icon(self.FOREST, self.CELL_SIZE)
		self.raspberry = self.load_icon(self.RASPBERRY, self.CELL_SIZE)
		self.wall = self.load_icon(self.WALL, self.CELL_SIZE)
		self.puddle = self.load_icon(self.PUDDLE, self.CELL_SIZE)

		# Draw score, lives, and level text
		self.font = pygame.font.Font(None, self.FONTSIZE)

		self.tile_lookup = {
			char.FOREST_WALL: self.forest,
			char.BEAR: self.bear,
			char.DEER: self.deer,
			char.CAVE_WALL: self.wall,
			char.PLAYER: self.player,
			char.DOT: self.raspberry,
			char.WATER: self.puddle
		}

	def load_icon(self,name, size):
		path = os.path.join(self.ICON_DIR, name)
		return pygame.transform.scale(pygame.image.load(path), (size, size))

	def update_screen(self,pacman_map,score):

		self.screen.fill(self.BACKGROUND_COLOUR)
		game_map = pacman_map.get_map()

		# Draw score bar at the top
		score_bar_rect = pygame.Rect(0, 0, self.width*self.CELL_SIZE, self.SCORE_BAR_HEIGHT)
		pygame.draw.rect(self.screen, self.SCORE_BAR_COLOUR , score_bar_rect)  # Dark gray background

		# Score text
		score_text = self.font.render(f"Score: {score}", True, self.SCORE_TEXT_COLOUR)
		self.screen.blit(score_text, (10, 5))

		for col in range(self.width):
			for row in range(self.height):

				# Adjust y-position by score_bar_height to make room for the score bar
				y_pos = row * self.CELL_SIZE + self.SCORE_BAR_HEIGHT
				x_pos = col * self.CELL_SIZE

				tile = game_map[row][col]
				image = self.tile_lookup.get(tile)
				if image:
					self.screen.blit(image, (x_pos,y_pos))

		pygame.display.update()

"""
6 September 2025 - Created file
7 September 2025 - Started building display
8 September 2025 - Basic Map displays
				 - Completed mathematical display of map
10 September 2025 - added clear screen function
12 September 2025 - Added score bar
13 September 2025 - Added puddle
18 September 2025 - Updated with player score
20 September 2025 - Fixed score display
28 November 2025 - Removed magic numbers
29 November 2025 - Increased version number
"""
