from random import randint

def print_board(board):
	prt_board = [str(i) for i in board]
	for i in range(0, len(prt_board)):
		if ord(prt_board[i]) >= 49 and ord(prt_board[i]) <= 57:
			prt_board[i] = ' '
	print('|'.join(prt_board[0:3]) + '\n' + '|'.join(prt_board[3:6]) + '\n' + '|'.join(prt_board[6:]) + '\n') 

def have_win(player, board):
	if (board[0] == player and board[1] == player and board[2] == player) \
	or (board[3] == player and board[4] == player and board[5] == player) \
    	or (board[6] == player and board[7] == player and board[8] == player) \
	or (board[0] == player and board[3] == player and board[6] == player) \
	or (board[1] == player and board[4] == player and board[7] == player) \
	or (board[2] == player and board[5] == player and board[8] == player) \
	or (board[0] == player and board[4] == player and board[8] == player) \
	or (board[2] == player and board[4] == player and board[6] == player):
        	return True
	else:
		return False
    
def empty_index(board):
	index = []
	i = 0
	while i <= 8:
		if board[i] != 'X' and board[i] != 'O':
			index.append(i)
		i += 1
	return index
  

def minimax(newBoard, player):
	availSpots = empty_index(newBoard)
	if have_win('O', newBoard):
		return [0,10] 
	if have_win('X', newBoard):
		return [0,-10]
	if len(availSpots) == 0:
		return [0,0] 
	moves = []
	for i in range(0, len(availSpots)):
		move = []
		move.append(newBoard[availSpots[i]]) 
		newBoard[availSpots[i]] = player
		if player == 'O':
			result = minimax(newBoard, 'X')
			move.append(result[1])
		else:
			result = minimax(newBoard, 'O')	
			move.append(result[1])
		newBoard[availSpots[i]] = move[0] 
		moves.append(move)
	if player == 'O':
		bestScore = -10000
		for move in moves:
			if move[1] > bestScore:
				bestScore = move[1]
				bestMove = move
	else:
		bestScore = 10000
		for move in moves:
			if move[1] < bestScore:
				bestScore = move[1]
				bestMove = move
	return bestMove

def AI_get_first_move():
	x = randint(1,2)
	if x == 1:
		return True	
	else:
		return False

def put_player_move(board):
	play = True
	while play:
		try:
			x = int(input("Entrez votre coup\n"))
		except: 
			print("Je n'ai pas compris\n")
			continue
		x -= 1
		if (x <= 8 and x >= 0) and (board[x] != 'X' and board[x] != 'O'):
			board[x] = 'X'
			play = False
		else:
			print("Vous devez choisir une case libre en tapant un chiffre de 1 à 9\n")

def put_AI_move(board):
	move = minimax(board, 'O')
	x = move[0]
	board[x - 1] = 'O'

def tie(board):
	if empty_index(board) == []:
		return True

input("\nBienvenue dans le TicTacToe\n\n|X| |X|\n| |O| |\n|X| |X|\n\nPressez Entrée pour tirer au sort le premier joueur\n")
print("...\n")
board = [1,2,3,4,5,6,7,8,9]
play = True
if AI_get_first_move():
	board[4] = 'O'
	input("L'ORDINATEUR COMMENCE\nEntrée pour commencer...\n")
else:
	input("VOUS COMMENCEZ\nEntrée pour commencer...\n")
print("Pour jouer, entrer un chiffre correspondant à une case\n|1|2|3|\n|4|5|6|\n|7|8|9|\n")
print_board(board)
while play:
	put_player_move(board)
	print_board(board)
	if have_win('X', board):
		print("Vous avez gagné, vous ête officiellement très fort\n")
		break
	if tie(board):
		print("Match nul\n")
		break
	put_AI_move(board)
	print_board(board)
	if have_win('O', board):
		print("C'est perdu\nQuel échec...")
		break
	if tie(board):
		print("Match nul\n")
		break
