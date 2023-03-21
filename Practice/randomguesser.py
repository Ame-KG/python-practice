# Modules
import random

# Number Generator
num = random.randint(0, 10)

# Guess Receiver
guess = int(input('Enter Guess between 0 and 10(including 0): '))

# Game Loop
while guess != num:
	if guess < num:
		print('Your guess was incorrect and less than the answer... ')
		guess = int(input('Guess Again: '))
	elif guess > num:
		print('Your guess was incorrect and greater than the answer... ')
		guess = int(input('Guess Again: '))
print('Correct Guess!')		


		