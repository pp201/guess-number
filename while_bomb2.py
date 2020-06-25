import random
r = random.randint(1, 100)
while True:
	num = input('Enter number: ')
	num = int(num)
	if num == r:
		print('BINGO')
		break
	elif num > r:
		print('Smaller')
	elif num < r:
		print('Bigger')