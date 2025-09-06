"""
File: Caveman Pacman Display 
Author: David Sarkies
Initial: 6 September 2025
Update: 6 September 2025
Version: 0.0
"""

import pygame

class View:
	def __init__ (self,map):
		width,height = map.get_dimensions()
		self.screen = pygame.display.set_mode((width, height))

"""
6 September 2025 - Created file
"""
