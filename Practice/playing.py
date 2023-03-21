# A prototype for a game i intend to create in the future
import random 

# In future there will also be stamina and potions along with damage and hp
# Character Parent Class
class Character():
	def __init__(self, name, hp, dmg):
 		self.name = name
 		self.hp = hp
 		self.dmg = dmg


class protagonist(Character):
	hp = 100
	dmg = 5

	
class enemy(Character):
	pass


# Protagonist/ Player
# Ame = protagonist('Ame', 100, 10)
# Ame.moveset(input('Enter Your 1st Move'), input('Enter Your 2nd Move'), input('Enter Your 3rd Move'))

lv1_boss = enemy('Eigo', 250, 5)
lv2_boss = enemy('Sarah', 100, 15)
lv3_boss = enemy('Auruah', 250, 15)

# Heal is a potion
# in future there will be multiple heal potions with varying heal capabilities and varying weights
# the amount of potions a player can have depend on the weight they can carry
# There will be other potions that do damage or reverse your oponents move
# there will be a load out class in future in which a player selects:...
# their sword (different swords have different, weight and damage)
# their potions
# their sheild ( different sheilds have different perks and hps, sheilds can break)
# armour (different armours have different weights, perks and hp bonuses)
# The perks can be for example
player_HEAL = 4
boss_heal = 4

#_______________________________________________________________________________________________________
# The actual game

level_1 = True

if lv1_boss.hp <= 0:
	level_1 = False
	print(f'{lv1_boss.name} has been defeated!!!')



print('LEVEL 1 START!')
player = protagonist(input('Enter your name: '), 100,5)
player_atk_count = 0
player_blk_count = 0

# Successful attack count perk
if player_atk_count >= 5:
	player.dmg = 10

elif player_atk_count >= 10:
	player.dmg = 20

# Successful block count perk
if player_blk_count >= 5:
	player_HEAL = 10


# Level one game loop and mechanics
while level_1:
	# First 3 moves are preselected in future
	# For now ask for players move and randomly select moves for player 1
	player_move = input('Enter your move (attack, block, heal): ')
	boss_move = ''

	# enemy move generator
	num = random.randint(1,3)

	if num == 1:
		boss_move = 'attack'

	elif num == 2:
		boss_move = 'block'

	elif num == 3:
		boss_move = 'heal'

	# GAME LOGIC/MECHANICS:
	#same moves played
	if boss_move == 'block' and player_move == 'block':
		print(f'{lv1_boss.name} move was block, {player.name} and your move was block')

	# in future if they both attack at the same time either they cancel each other out or...
	# the difference between their two damages are shared
	elif boss_move == 'attack'and player_move == 'attack':
		print(f'{lv1_boss.name} move was attack, {player.name} and your move was attack')
		lv1_boss.hp -= player.dmg
		player.hp -= lv1_boss.dmg
		print(f'{lv1_boss.name}\'s hp: {lv1_boss.hp}')
		print(f'{player.name}\'s hp: {player.hp}')

	elif boss_move == 'heal' and player_move == 'heal':
		print(f'{lv1_boss.name} move was heal, {player.name} and your move was heal')
		lv1_boss.hp += boss_heal
		player.hp += player_HEAL
		print(f'{lv1_boss.name}\'s hp: {lv1_boss.hp}')
		print(f'{player.name}\'s hp: {player.hp}')


	# Player attack moves
	elif boss_move == 'heal' and player_move == 'attack':
		print(f'{lv1_boss.name} move was {boss_move}, {player.name} and your move was {player_move}')
		lv1_boss.hp += player_HEAL
		lv1_boss.hp -= player.dmg
		print(f'{lv1_boss.name}\'s hp: {lv1_boss.hp}')
		print(f'{player.name}\'s hp: {player.hp}')


