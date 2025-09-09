"""
File: Caveman Pacman Control 
Author: David Sarkies
Initial: 9 September 2025
Update: 9 September 2025
Version: 0.0
"""

import pygame

def get_keypress():

	events = pygame.event.get()
	key = ""

	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				key = "N"
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				key = "S"
			elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
				key = "W"
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				key = "E"
			elif event.key == pygame.K_q:
				key = "Q"

	return key


"""
9 September 2025 - Created file
"""