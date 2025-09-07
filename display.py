"""
File: Caveman Pacman Display 
Author: David Sarkies
Initial: 6 September 2025
Update: 7 September 2025
Version: 0.1
"""

import pygame

class View:
	def __init__ (self,dimensions):
		self.cell_size = 20
		self.screen = pygame.display.set_mode((dimensions[0]*self.cell_size, dimensions[1]*self.cell_size))
		pygame.display.set_caption("Caveman Pacman")
		self.player = pygame.transform.scale(pygame.image.load("icons/cavewoman.png"),(self.cell_size,self.cell_size))
		self.bear = pygame.transform.scale(pygame.image.load("icons/bear.png"),(self.cell_size,self.cell_size))
		self.deer = pygame.transform.scale(pygame.image.load("icons/deer.png"),(self.cell_size,self.cell_size))		
		self.forest = pygame.transform.scale(pygame.image.load("icons/forest.png"),(self.cell_size,self.cell_size))
		self.raspberry = pygame.transform.scale(pygame.image.load("icons/raspberry.png"),(self.cell_size,self.cell_size))
		self.cliffs = pygame.transform.scale(pygame.image.load("icons/cliffs.png"),(self.cell_size,self.cell_size))

	#Display

"""
6 September 2025 - Created file
7 September 2025 - Started building display
"""
