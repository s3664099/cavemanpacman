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
		#player = pygame.transform.scale(pygame.image.load("icons/worker.png"),(cell_size,cell_size))

"""
6 September 2025 - Created file
7 September 2025 - Started building display
"""
