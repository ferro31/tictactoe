import copy
import os
import random

import generatepossiblemoves

board = [['X', 'X', 'X'],
         ['X', 'X', 'X'],
         ['X', 'X', 'X'],]


def format_board(b):
	a = ''
	for row in b:
		for b in row:
			a += b
	return a


def check_saved():
	if os.path.exists(f"moves/{format_board(board)}.txt"):
		with open(f"moves/{format_board(board)}.txt", 'r') as f:
			return f.readline().split(",")
	else:
		with open(f"moves/{format_board(board)}.txt", 'w+') as f:
			f.write(",".join(list(generatepossiblemoves.generate_possibilies(board))))
			return list(generatepossiblemoves.generate_possibilies(board))


def remove(chosen, possibilties, boardcopy):
	possible_moves = copy.deepcopy(possibilties)
	possible_moves.remove(chosen)
	with open(f"moves/{format_board(boardcopy)}.txt", 'w') as f:
		f.write(",".join(possible_moves))

while True:
	for a in board:
		print(a)
	p = input()
	board[int(p[0])][int(p[1])] = "P"
	boardcopy = copy.deepcopy(board)

	possibilities = check_saved()
	c = random.choice(possibilities)
	board[int(c[0])][int(c[1])] = "C"
	for a in board:
		print(a)
	if int(input()):
		remove(c, possibilities, boardcopy)
	print("*---*")
