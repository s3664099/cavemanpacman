"""
File: Caveman Pacman Control 
Author: David Sarkies
Initial: 9 September 2025
Update: 19 October 2025
Version: 0.2
"""

import pygame

def get_keypress():

	events = pygame.event.get()
	keys = []

	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				keys.append("N")
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				keys.append("S")
			elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
				keys.append("W")
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				keys.append("E")
			elif event.key == pygame.K_q:
				keys.append("Q")
			elif event.key == pygame.K_p:
				keys.append("P")

	return keys[-1] if keys else ""


"""
9 September 2025 - Created file
11 October 2025 - Added pause keystroke
19 October 2025 - Added handling for multiple keystrokes
"""
