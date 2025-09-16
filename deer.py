"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 16 September 2025
Version: 0.0
"""

class Deer:

	def __init__(self,row,col):
		self.position = (row,col)
		self.running = False

	def get_position(self):
		return self.position

	def check_position(self,row,col):
		return (row,col) == self.position

	def set_position(self,row,col):
		self.position = (row,col)




"""
16 September 2025 - Created file
"""