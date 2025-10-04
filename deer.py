"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 4 October 2025
Version: 0.1

- If sees bear/player moves in opposite direction
"""

import random

class Deer:

	def __init__(self,row,col):
		self.position = (row,col)
		self.fleeing = False
		self.score = 10

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def check_position(self,row,col):
		return (row,col) == self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def move_deer(self,map_data,width):
		non_blockers = ["."," ","w"]
		new_row,new_col = self.position
		row,col = self.position
		movement = random.randint(0,12)

		if (movement == 0):
			new_row -=1
		elif (movement == 1):
			new_row +=1
		elif (movement == 2):
			new_col -=1
		elif (movement == 3):
			new_col +=1

		if (new_col<width):
			new_position = map_data[new_row][new_col]
			if (new_position in non_blockers):
				map_data[row][col] = " "
				map_data[new_row][new_col]="d"
				self.position = (new_row,new_col)

		return map_data

	def find_predator(self,map_data,row,col):

		movement = -1
		distance = 0

		try:
			found_stop = False
			position = 0
			map_pos = 0
			new_movement = -1

			while not found_stop:
				map_pos -=1
				position +=1
				found_stop,new_movement,distance = self.check_position(map_data,row+map_pos,col,position,0)
			movement,distance = self.check_move(new_movement,movement,position,distance)
		except:
			print("North")
			print(row+map_pos,col)

		try:
			found_stop = False
			position = 0
			map_pos = 0
			new_movement = -1

			while not found_stop:
				map_pos +=1
				position +=1
				found_stop,new_movement,distance = self.check_position(map_data,row+map_pos,col,position,1)
			movement,distance = self.check_move(new_movement,movement,position,distance)
		except:
			print("South")
			print(row+map_pos,col)

		try:
			found_stop = False
			position = 0
			map_pos = 0
			new_movement = -1

			while not found_stop:
				map_pos -=1
				position +=1
				found_stop,new_movement,distance = self.check_position(map_data,row,col+map_pos,position,2)
			movement,distance = self.check_move(new_movement,movement,position,distance)
		except:
			print("East")
			print(row,col+map_pos)

		try:
			found_stop = False
			position = 0
			map_pos = 0
			new_movement = -1

			while not found_stop:
				map_pos +=1
				position +=1
				found_stop,new_movement,distance = self.check_position(map_data,row,col+map_pos,position,3)
			movement,distance = self.check_move(new_movement,movement,position,distance)
		except:
			print("West")
			print(row,col+map_pos)

		return movement

	def check_position(self,map_data,row,col,position,direction):
		found_stop = False
		movement = -1
		distance = 0
		if map_data[row][col] == "P" or map_data[row][col] == "d":
			found_stop = True
			movement = -direction
			distance = position
			print("Move ",direction)
		elif map_data[row][col] == "1" or map_data[row][col] == "2" or map_data[row][col] == "/":
			found_stop = True
		return found_stop,movement,distance

	def check_move(self,new_movement,movement,position,distance):

		if new_movement != -1:
			if position<distance:
				movement = new_movement
				distance = position
			elif movement == -1:
				movement = new_movement
				distance = position

		return movement,distance


"""
16 September 2025 - Created file
4 October 2025 - Added check for predators
"""