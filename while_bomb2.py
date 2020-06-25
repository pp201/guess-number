import random
start = input('Start at the min number ')
start= int(start)
end = input('End at the max number ')
end = int(end)
r = random.randint(start, end)
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