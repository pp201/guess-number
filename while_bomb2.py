import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Enter number: ')
	num = int(num)
	if num == r:
		print('BINGO')
		break
	elif num > r:
		print('Smaller')
	elif num < r:
		print('Bigger')
	print('You tried', count, 'times')