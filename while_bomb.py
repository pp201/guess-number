import random

n = random.randint(1,10)
i = 10

while i>0:	
	i = i - 1
	guess = input('Enter a number ')
	g = int(guess)
	if n == g:
		print('Bomb')
		break
	elif g > n:
		print('Smaller')
		print('Bigger')
		if i > 0:
			print('One more guess')
		else:
			print('No more chance')		
	elif g < n:
		print('Bigger')
		if i > 0:
			print('One more guess')
		else:
			print('No more chance')