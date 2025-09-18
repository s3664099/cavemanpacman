"""
File: Caveman Pacman Display 
Author: David Sarkies
Initial: 6 September 2025
Update: 18 September 2025
Version: 0.5
"""

import pygame

class View:
	def __init__ (self,dimensions):

		pygame.init()

		self.cell_size = 30
		self.score_bar_height = 30  # Height of the score bar
		self.width = dimensions[0]
		self.height = dimensions[1]
		self.screen = pygame.display.set_mode((self.width*self.cell_size, (self.height+1)*self.cell_size))
		pygame.display.set_caption("Caveman Pacman")
		self.player = pygame.transform.scale(pygame.image.load("icons/cavewoman.png"),(self.cell_size,self.cell_size))
		self.bear = pygame.transform.scale(pygame.image.load("icons/bear.png"),(self.cell_size,self.cell_size))
		self.deer = pygame.transform.scale(pygame.image.load("icons/deer.png"),(self.cell_size,self.cell_size))		
		self.forest = pygame.transform.scale(pygame.image.load("icons/forest.png"),(self.cell_size,self.cell_size))
		self.raspberry = pygame.transform.scale(pygame.image.load("icons/raspberry.png"),(self.cell_size,self.cell_size))
		self.wall = pygame.transform.scale(pygame.image.load("icons/wall.png"),(self.cell_size,self.cell_size))
		self.puddle = pygame.transform.scale(pygame.image.load("icons/puddle.png"),(self.cell_size,self.cell_size))

	def update_screen(self,pacman_map,score):

		self.screen.fill((0,0,0))
		game_map = pacman_map.get_map()

		# Draw score bar at the top
		score_bar_rect = pygame.Rect(0, 0, self.width, self.score_bar_height)
		pygame.draw.rect(self.screen, (50, 50, 50), score_bar_rect)  # Dark gray background

		# Draw score, lives, and level text
		font = pygame.font.Font(None, 24)

		# Score text
		score_text = font.render(f"Score: {score}", True, (255, 255, 255))
		self.screen.blit(score_text, (10, 5))

		for col in range(self.width):
			for row in range(self.height):

				# Adjust y-position by score_bar_height to make room for the score bar
				y_pos = row * self.cell_size + self.score_bar_height
				x_pos = col * self.cell_size

				if game_map[row][col] == "1":
					self.screen.blit(self.forest,(x_pos,y_pos))
				elif game_map[row][col] == "B":
					self.screen.blit(self.bear,(x_pos,y_pos))
				elif game_map[row][col] == "d":
					self.screen.blit(self.deer,(x_pos,y_pos))
				elif game_map[row][col] == "2":
					self.screen.blit(self.wall,(x_pos,y_pos))
				elif game_map[row][col] == "P":
					self.screen.blit(self.player,(x_pos,y_pos))
				elif game_map[row][col] == ".":
					self.screen.blit(self.raspberry,(x_pos,y_pos))
				elif game_map[row][col] == "w":
					self.screen.blit(self.puddle,(x_pos,y_pos))

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
"""
