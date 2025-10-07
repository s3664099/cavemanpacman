"""
File: Caveman Pacman Deer
Author: David Sarkies
Initial: 16 September 2025
Update: 7 October 2025
Version: 0.2

- If sees bear/player moves in opposite direction
	- Not Working see find predator
	- Distance irrelevant as deer will not move if can't move
	- move main game into a function
"""

import random

class Deer:

	def __init__(self,row,col):
		self.position = (row,col)
		self.fleeing = False
		self.score = 10
		self.non_blockers = ["."," ","w"]

	def get_score(self):
		return self.score

	def get_position(self):
		return self.position

	def check_current_position(self,row,col):
		return (row,col) == self.position

	def set_position(self,row,col):
		self.position = (row,col)

	def move_deer(self,map_data,width):
		new_row,new_col = self.position
		row,col = self.position

		movement_options,predator_found = self.find_predator(map_data,row,col)
		movement = random.randint(0,12)
		print(movement_options)
		print(predator_found)
		if (predator_found):

			if map_data[row-1][col] not in self.non_blockers:
				movement_options[0] = "X"
			elif map_data[row+1][col] not in self.non_blockers:
				movement_options[1] = "X"
			elif map_data[row][col-1] not in self.non_blockers:
				movement_options[2] = "X"
			elif map_data[row][col+1] not in self.non_blockers:
				movement_options[3] = "X"

			can_move = False

			for x in movement_options:
				if x == "":
					can_move = True

			if can_move:
				found_move = False
				while not can_move:
					movement_options = random.randint(0,3)
					if movement_options[movement] == "":
						map_data = self.calculate_move(movement,map_data,width,row,col)

		else:
			map_data = self.calculate_move(movement,map_data,width,row,col)

		return map_data

	def calculate_move(self,movement,map_data,width,row,col):

		new_row = 0
		new_col = 0

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
			if (new_position in self.non_blockers):
				map_data[row][col] = " "
				map_data[new_row][new_col]="d"
				self.position = (new_row,new_col)
		print("Deer move",movement)
		return map_data

	def find_predator(self,map_data,row,col):

		#Comes out as [0.0.0.0] and should be "" or X for blocked position

		movement = ["","","",""]
		predator_found = False

		try:
			found_stop = False
			position = 0
			map_pos = 0

			while not found_stop:
				map_pos -=1
				position +=1
				found_stop,new_movement,distance,found_predator = self.check_position(map_data,row+map_pos,col,position,0)
			if found_predator:
				movement[0] = distance
				predator_found = True
		except Exception as e: 
			print("North")
			print(row+map_pos,col)
			print(e)

		try:
			found_stop = False
			position = 0
			map_pos = 0

			while not found_stop:
				map_pos +=1
				position +=1
				found_stop,new_movement,distance,found_predator = self.check_position(map_data,row+map_pos,col,position,1)
			if found_predator:
				movement[1] = distance
				predator_found = True
		except Exception as e:
			print("South")
			print(row+map_pos,col)
			print(e)

		try:
			found_stop = False
			position = 0
			map_pos = 0

			while not found_stop:
				map_pos -=1
				position +=1
				found_stop,new_movement,distafound_predatornce,found_predator = self.check_position(map_data,row,col+map_pos,position,2)
			if found_predator:
				movement[2] = distance
				predator_found = True
		except Exception as e:
			print("East")
			print(row,col+map_pos)
			print(e)

		try:
			found_stop = False
			position = 0
			map_pos = 0

			while not found_stop:
				map_pos +=1
				position +=1
				found_stop,new_movement,distance,found_predator = self.check_position(map_data,row,col+map_pos,position,3)
			if found_predator:
				movement[3] = distance
				predator_found = True
		except Exception as e:
			print("West")
			print(row,col+map_pos)
			print(e)
		print("Movement ")

		return movement,predator_found

	def check_position(self,map_data,row,col,position,direction):
		found_stop = False
		found_predator = True
		movement = -1
		distance = 0
		if map_data[row][col] == "P" or map_data[row][col] == "d":
			found_stop = True
			found_predator = True
			movement = -direction
			distance = position
			print("Move ",direction)
		elif map_data[row][col] == "1" or map_data[row][col] == "2" or map_data[row][col] == "/":
			found_stop = True
		return found_stop,movement,distance,found_predator

"""
16 September 2025 - Created file
4 October 2025 - Added check for predators
7 October 2025 - Updated predetorFound
"""