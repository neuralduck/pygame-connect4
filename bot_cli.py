import os
from copy import deepcopy
from connect4 import ConnectFour

# def minimax(board, player, depth = 1):
#     if player == 1:
#         best = [None, -float("inf")]
#     else:
#         best = [None, float("inf")]
#     result, *_ = board.check()
#     if result in (1, 0, -1):
#         return [None, result*1000]
#     if depth == 5:
#         return [None, board.get_value()]
#     for move in board.available_moves():
#         new_board = deepcopy(board)
#         new_board.move(move, player)
#         _, score = minimax(new_board, -player, depth+1)
#         if player == 1:
#             if score > best[1]:
#                 best = [move, score]
#         else:
#             if score < best[1]:
#                 best = [move, score]
#     return best

def minimax(board, player, depth=1, alpha=-float("inf"), beta=float("inf")):
    if player == 1:
        best = [None, -float("inf")]
    else:
        best = [None, float("inf")]
    result, *_ = board.check()
    if result in (1, 0, -1):  # Win, loss, or draw
        return [None, result * 1000]
    if depth == 6:
        return [None, board.get_value()]
    for move in board.available_moves():
        new_board = deepcopy(board)
        new_board.move(move, player)
        _, score = minimax(new_board, -player, depth + 1, alpha, beta)
        if player == 1:
            if score > best[1]:
                best = [move, score]
            alpha = max(alpha, score)
        else:  # Minimizing player
            if score < best[1]:
                best = [move, score]
            beta = min(beta, score)
        if alpha >= beta:
            break
    return best

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
		print(f"eval: {board.get_value()}")
		if turn:
			choice = int(input(f"Your choice ({board.symbol1}): "))
		else:
			#choice = int(input(f"Player 2 choice ({board.symbol2}): "))
			choice = minimax(board, player2)[0]
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
		print('calling check')
		result, *_ = board.check()
		if result == 1:
			info()
			print(f'Player 1 ({board.symbol1}) wins')
			break
		elif result == -1:
			info()
			print(f'Bot({board.symbol2}) wins')
			break
		elif result == 0:
			info()
			print('result reutned zero')
			print('Draw')
			break