"""
File: Caveman Pacman Control 
Author: David Sarkies
Initial: 9 September 2025
Update: 19 October 2025
Version: 0.2
"""

import pygame

KEY_BINDINGS = {
	pygame.K_UP: "N",
	pygame.K_w: "N",
	pygame.K_DOWN: "S",
	pygame.K_s:"S",
	pygame.K_LEFT:"W",
	pygame.K_a:"W",
	pygame.K_RIGHT:"E",
	pygame.K_d:"E",
	pygame.K_q:"Q",
	pygame.K_p:"P"
}

def get_keypress():

	events = pygame.event.get()
	keys = []

	for event in events:
		if event.type == pygame.KEYDOWN:
			keys.append(KEY_BINDINGS.get(event.key,""))

	return keys[-1] if keys else ""


"""
9 September 2025 - Created file
11 October 2025 - Added pause keystroke
19 October 2025 - Added handling for multiple keystrokes
				- Tightened code
"""
