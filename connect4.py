import os

class ConnectFour:
	def __init__(self):
		self.board = [[0 for _ in range(7)] for _ in range(6)]
		self.symbol1 = '\N{WHITE CIRCLE}'
		self.symbol2 = '\N{BLACK CIRCLE}'
		self.move_count = {i: 0 for i in range(7)}

	def __str__(self):
		board_str = ''
		get_symbol = lambda x: f'{self.symbol1}' if x == 1 else f'{self.symbol2}' if x == -1 else ' '
		#get_symbol = lambda x: f'{1}' if x == 1 else f'{-1}' if x == -1 else ' '
		dash = '\N{Horizontal Bar}'
		board_str += '| '+' | '.join(list(map(str, range(7))))+' |'+'\n'
		board_str += '-'*29+'\n'
		for row in self.board:
			board_str += '| '+' | '.join(list(map(get_symbol, row)))+' |'+'\n'
			board_str += '-'*29+'\n'
		return board_str

	def move(self, column, mark):
		if self.move_count[column] < 6:
			for cell in list(range(6))[::-1]:
				if self.board[cell][column] == 0:
					self.board[cell][column] = mark
					self.move_count[column] += 1
					break
	def value(self):
		def calculate_value(player):
			total_value = 0
			for choice in self.available_moves():
				directions = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1), 'ur': (-1, 1), 'ul': (-1, -1), 'dr': (1, 1), 'dl': (1, -1)}
				lines = {'u': 0, 'd': 0, 'r': 0, 'l': 0, 'ur': 0, 'ul': 0, 'dr': 0, 'dl': 0}
				i = 5 - self.move_count[choice]
				j = choice
				for dir in directions:
					m, n = directions[dir]
					for t in (1, 2, 3):
						if (0<=(i+t*m)<=5) and (0<=(j+t*n)<=6):
							if (self.board[i+t*m][j+t*n] == player):
								lines[dir] += 1
							else:
								break
				choice_value = sum(map(lambda x: x*100 if x == 3 else x*5 if x == 2 else x if x == 1 else 0, filter(lambda x: x>0, lines.values())))
				total_value += choice_value
			return total_value * player
		
		p1 = calculate_value(player = 1)
		p2 = calculate_value(player = -1)
		return p1 + p2
	
	def available_moves(self):
		#returns a list of column numbers with empty cells
		return list(map(lambda x: x[0], filter(lambda x: True if x[1] < 6 else False, self.move_count.items())))
	
	def num_cells(self):
		#number of empty cells in the board, for draw and game over checks
		return 42 - sum(self.move_count.values())

	def check(self, index = False):
		# +1 player 1 | -1 player 2 | 0 draw | 3 game not over
		if self.num_cells() == 0:
			#draw
			if index:
				return [0, None, None]
			return 0
		for i in range(6):
			for j in range(7):
				if abs(self.board[i][j]) == 1:
					RIGHT = (j+3 <= 6)
					LEFT = (j-3 >= 0)
					UP = (i-3 >= 0)
					DOWN = (i+3 <= 5)
					if RIGHT:
						right = 0
						for n in range(4):
							right += self.board[i][j+n]
						if abs(right) == 4:
							if index:
								return [int(right/4),(i, j), (i, j+3)]
							return int(right/4)
						if UP:
							right_up = 0
							for n in range(4):
								right_up += self.board[i-n][j+n]
							if abs(right_up) == 4:
								if index:
									return [int(right_up/4), (i, j), (i-3, j+3)]
								return int(right_up/4)
						if DOWN:
							right_down = 0
							for n in range(4):
								right_down += self.board[i+n][j+n]
							if abs(right_down) == 4:
								if index:
									return [int(right_down/4), (i, j), (i+3, j+3)]
								return int(right_down/4)
					if LEFT:
						left = 0
						for n in range(4):
							left += self.board[i][j-n]
						if abs(left) == 4:
							if index:
									return [int(left/4), (i, j), (i, j-3)]
							return int(left/4)

						if UP:
							left_up = 0
							for n in range(4):
								left_up += self.board[i-n][j-n]
							if abs(left_up) == 4:
								if index:
									return [int(left_up/4), (i, j), (i-3, j-3)]
								return int(left_up/4)

						if DOWN:
							left_down = 0
							for n in range(4):
								left_down += self.board[i+n][j-n]
							if abs(left_down) == 4:
								if index:
									return [int(left_down/4), (i, j), (i+3, j-3)]
								return int(left_down/4)
					if UP:
						up = 0
						for n in range(4):
							up += self.board[i-n][j]
						if abs(up) == 4:
							if index:
									return [int(up/4), (i, j), (i-3, j)]
							return int(up/4)

					if DOWN:
						down = 0
						for n in range(4):
							down += self.board[i+n][j]
						if abs(down) == 4:
							if index:
									return [int(down/4), (i, j), (i+3, j)]
							return int(down/4)
		if index:
			return [3, None, None]
		return 3

if __name__ == '__main__':
	def info():
		os.system('clear||cls')
		print(board)
	turn = 1
	board = ConnectFour()
	player1 = 1
	player2 = -1
	while True:
		info()
		print(board.value())
		if turn:
			choice = int(input(f"Player 1 choice ({board.symbol1}): "))
		else:
			choice = int(input(f"Player 2 choice ({board.symbol2}): "))
		if board.move_count[choice] == 6:
			print('column full')
			continue
		if choice not in range(7):
			print('pick a choice within range')
			continue
		if turn:
			board.move(choice, player1)
		else:
			board.move(choice, player2)
		turn = int(not(turn))
		result = board.check()
		if result == 1:
			info()
			print(f'Player 1 ({board.symbol1}) wins')
			break
		elif result == -1:
			info()
			print(f'Player 2 ({board.symbol2}) wins')
			break
		elif result == 0:
			info()
			print('Draw')
			break