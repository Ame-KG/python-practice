import random

# Scoreboard Variables
cpu_score = 0
player_score = 0

# Core Game Loop
while cpu_score != 3 and player_score != 3:

	# Player Move Storer
	random_num = random.randint(1,3)
	cpu_move = ''


	# Cpu Move Allocator
	if random_num == 1 :
		cpu_move = 'rock'
	elif random_num == 2:
		cpu_move = 'paper' 
	elif random_num == 3:
		cpu_move = 'scissor' 

	# Player Move Collector
	player_move = input('Enter your move(rock, paper or scissor):')


	# WIN DETECTOR:

	# Tied Moves
	if player_move.lower() == cpu_move:
		print(F'Cpu move was {cpu_move} and your move was {player_move}, tie, NO POINTS!')
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')
# Game

	# Player Rock Moves
	elif player_move.lower() == 'rock' and cpu_move == 'paper':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		cpu_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')


	elif player_move.lower() == 'rock' and cpu_move == 'scissor':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		player_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')


	# Player Paper Moves
	elif player_move.lower() == 'paper' and cpu_move == 'scissor':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		cpu_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')


	elif player_move.lower() == 'paper' and cpu_move == 'rock':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		player_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')

	# Player Scissor Moves
	elif player_move.lower() == 'scissor' and cpu_move == 'rock':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		cpu_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')


	elif player_move.lower() == 'scissor' and cpu_move == 'paper':
		print(F'Cpu move was {cpu_move} and your move was {player_move}')
		player_score += 1
		print(f'cpu score: {cpu_score} \nYour score: {player_score}')


if player_score == 3:
	print('You Win!')
else:
	print('You Lose!!!')

print(f'Cpu Score: {cpu_score} -- Player Score: {player_score}')