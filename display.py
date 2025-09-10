"""
File: Caveman Pacman Display 
Author: David Sarkies
Initial: 6 September 2025
Update: 10 September 2025
Version: 0.3
"""

import pygame

class View:
	def __init__ (self,dimensions):

		pygame.init()

		self.cell_size = 30
		self.width = dimensions[0]
		self.height = dimensions[1]
		self.screen = pygame.display.set_mode((self.width*self.cell_size, self.height*self.cell_size))
		pygame.display.set_caption("Caveman Pacman")
		self.player = pygame.transform.scale(pygame.image.load("icons/cavewoman.png"),(self.cell_size,self.cell_size))
		self.bear = pygame.transform.scale(pygame.image.load("icons/bear.png"),(self.cell_size,self.cell_size))
		self.deer = pygame.transform.scale(pygame.image.load("icons/deer.png"),(self.cell_size,self.cell_size))		
		self.forest = pygame.transform.scale(pygame.image.load("icons/forest.png"),(self.cell_size,self.cell_size))
		self.raspberry = pygame.transform.scale(pygame.image.load("icons/raspberry.png"),(self.cell_size,self.cell_size))
		self.wall = pygame.transform.scale(pygame.image.load("icons/wall.png"),(self.cell_size,self.cell_size))

	def update_screen(self,pacman_map):

		self.screen.fill((0,0,0))

		for col in range(self.width):
			for row in range(self.height):
				if pacman_map[row][col] == "1":
					self.screen.blit(self.forest,(col*self.cell_size,row*self.cell_size))
				elif pacman_map[row][col] == "B":
					self.screen.blit(self.bear,(col*self.cell_size,row*self.cell_size))
				elif pacman_map[row][col] == "d":
					self.screen.blit(self.deer,(col*self.cell_size,row*self.cell_size))
				elif pacman_map[row][col] == "2":
					self.screen.blit(self.wall,(col*self.cell_size,row*self.cell_size))
				elif pacman_map[row][col] == "P":
					self.screen.blit(self.player,(col*self.cell_size,row*self.cell_size))
				elif pacman_map[row][col] == ".":
					self.screen.blit(self.raspberry,(col*self.cell_size,row*self.cell_size))

		pygame.display.update()

"""
6 September 2025 - Created file
7 September 2025 - Started building display
8 September 2025 - Basic Map displays
				 - Completed mathematical display of map
10 September 2025 - added clear screen function
"""
