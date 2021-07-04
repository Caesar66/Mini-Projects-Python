import random
import os

class Player:
	def __init__(self, p):
		self.p = p

class Game:
	def __init__(self, n):
		self.n = n
		self.grid_size = (2*n-1, 2*(n-1))
		self.grid_ = [0 for x in range(self.grid_size[0]*self.grid_size[1])]
		#controls the "height" of each column
		self.col_control = [self.grid_size[1] for x in range(self.grid_size[0])]
		self.endgame = self.grid_size[0]*self.grid_size[1]

		self.grid_str = ('{}|'*(self.grid_size[0]-1)+'{}\n')*(self.grid_size[1])
		self.grid_label = "|".join([str(i) for i in range(1, self.grid_size[0]+1)])+"\n"

	def __repr__(self):
		return "Game(" + str(self.n) + ")"
	
	def __str__(self):
		return self.grid_str.format(*self.grid_)+"\n"+self.grid_label

	def get_position(self, col):
		return (col-1)+self.col_control[col-1]*self.grid_size[0]

	def insert(self, col, player):
		try:
			if(self.col_control[col-1] == 0):
				raise IndexError
			self.col_control[col-1] -= 1
			self.grid_[self.get_position(col)] = player	
		except IndexError:
			return "Column full. Choose another column.\n"
		else:
			self.endgame -= 1
			return 0

	def check_row(self, col):
		pos = self.get_position(col)
		chk_ = self.grid_[pos-(pos%self.grid_size[0]): pos-(pos%self.grid_size[0])+self.grid_size[0]]

		return self.check_positions(chk_)

	def check_column(self, col):
		chk_ = self.grid_[col-1::self.grid_size[0]]
		
		return self.check_positions(chk_)

	def check_diagonal_tb(self, col):
		pos = self.get_position(col)
		#Checks if the position belong to a "superior" diagonal or inferior
		# |\\ SUP |
		# | \\    |    The function works differently depending on which one it is
		# |  \\   |    If it is a superior: Gets the first value of the diagonal go all the way to the end
		# |   \\  |    If it is an inferior: Gets the first value and the last value.
		# |    \\ |    Both cases, the steps is always the grid_size[0]+1 (One increment to the row size)
		# | INF \\|    To check where the diagonal is you calculate the col + abs(row (col_control) - grid_size[0] (size of the row)). If it is bigger then the grid_size[1], it is superior otherwise, inferior.
		#
		#Basically the first value is gotten by calculating the "distance" in unit that the position is to the beginning of the diagonal.
		# |B| | | The distance from N to B is grid_size[0]+1. To limit the diagonal to the "edge" of the array you use the row (col_control) and the col. 
		# | |N| | 
		# | | |E|   
		# 
		#
		if((col-1)+abs(self.col_control[col-1]+1-self.grid_size[0]) <= self.grid_size[1]):
			__begin = pos-(col-1)*(self.grid_size[0]+1)
			chk_ = self.grid_[__begin::(self.grid_size[0]+1)]
		else:
			__begin = pos%(self.grid_size[0]+1)
			__end = pos+(self.grid_size[0]-col)*(self.grid_size[0]+1)
			chk_ = self.grid_[__begin:__end+1:(self.grid_size[0]+1)]
		return self.check_positions(chk_)

	def check_diagonal_bt(self, col):
		pos = self.get_position(col)
		#This one does the same thing but to the "other" diagonal
		# | SUP //|
		# |    // |    The function works differently depending on which one it is
		# |   //  |    If it is a superior: Gets the first value of the diagonal go all the way to the end
		# |  //   |    If it is an inferior: Gets the first value and the last value.
		# | //    |    Both cases, the steps is always the grid_size[0]-1 (One decrement to the row size)
		# |// INF |    
		#
		#Basically the first value is gotten by calculating the "distance" in unit that the position is to the beginning of the diagonal.
		# | | |B|
		# | |N| |
		# |E| | |   
		#
		if((col-1)+self.col_control[col-1] < self.grid_size[1]):
			__begin = pos-self.col_control[col-1]*(self.grid_size[0]-1)
			__end = pos+(col-1)*(self.grid_size[0]-1)
			chk_ = self.grid_[__begin:__end+1:self.grid_size[0]-1]
		else:
			__begin = pos-(self.grid_size[0]-col)*(self.grid_size[0]-1)
			chk_ = self.grid_[__begin::self.grid_size[0]-1]
		return self.check_positions(chk_)

	def check_positions(self, chk_):
		c_ = 1
		for v in range(1, len(chk_)):
			if(chk_[v] == 0):
				continue
			elif(chk_[v] == chk_[v-1]):
				c_ += 1
				if(c_ == self.n):
					return True
			else:
				c_ = 1
		return False

	def check_endgame(self):
		return True if self.endgame == 0 else False

def check_input(n, r1, r2):
	try:
		if(n.lower() == "exit"):
			return -1
		else:
			n = eval(n)
			if(type(n) is not int):
				raise Exception
			elif(n < r1 or n > r2):
				return "Please choose an integer between {} and {} (included).\n".format(r1,r2)
			else:
				return n
	except:
		return "Invalid Text.\n"

def get_connect_size(r1, r2):
	while(True):
		n = check_input(input("What size of Connect would you like to play? Choose a number between 4 and 10 (included).\nWrite EXIT to quit the game.\n"), r1, r2)
		if(type(n) == str):
			os.system("cls||clear")
			print(n)
			continue
		return n

def main_game(game_):
	player = 1
	while(True):
		print(game_)
		col = check_input(input("Player {}'s turn.\nPick a column from 1 to {}.\n".format(player, game_.grid_size[0])), 1, game_.grid_size[0])
		if(type(col) is str):
			os.system("cls||clear")
			print(col)
			continue
		elif(col == -1):
			print("Thanks for playing!")
			return -1
		r_ = game_.insert(col, player)
		if(type(r_) is not int):
			os.system("cls||clear")
			print(r_)
			continue
		else:
			if(game_.check_column(col) or game_.check_row(col) or game_.check_diagonal_bt(col) or game_.check_diagonal_tb(col)):
				print("\nPlayer {} won!".format(player))
				print(game_)
				return 0
			else:
				if(game_.check_endgame()):
					print("\nThe game has ended in a draw!")
					return 0
				player = 1 if player == 2 else 2
				os.system("cls||clear")
				print(game_.endgame)
				continue

r1 = 4
r2 = 10
gameLoop = True
os.system("cls||clear")
print("Welcome to Connect N!\n")
while(gameLoop):
	n = get_connect_size(r1, r2)
	if(n == -1):
		break
	os.system("cls||clear")
	game_ = Game(n)
	while(True):
		r_ = main_game(game_)
		if(r_ == -1):
			gameLoop = False
			break
		else:
			r_ = check_input(input("Type 1 to play again or anything else if you want to quit.\n"), 1, 1)
			if(type(r_) is str):
				print("Thanks for playing!")
				gameLoop = False
				break
			else:
				os.system("cls||clear")
				game_ = Game(n)
