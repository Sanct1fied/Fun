userinput = input('is your number less than or greater than 0?:')

if userinput in ['greater']:
	number = int(input('what number do you want turned into a power'))
	if number > 0:
		while number < 1000:
			print("that number is too small")
			number = int(input('what number do you want turned into a power'))
		else:
			temp = [char for char in str(number)]
			standardform = ['','','','']
			for i in range(4):
				standardform[i] = temp[i]
			rounder = int(standardform[2])
			if int(standardform[3]) >= 5:
				rounder += 1
			else:
				pass
	else:
		print('error')
	
	
		power = len(temp)-1
		finalnum = standardform[0] + '.' + standardform[1] + str(rounder) + 'x10' + '^' + str(power)
		print(finalnum)
else: 
	number = input('what number do you want turned into a power')
	decimal = float(number)
	if decimal < 0:
		temp = [char for char in str(decimal)]
		standardform = ['','','','']
		for i in range(len(temp)):
			if int(temp[i]) == 0:
				counter += 1
				pass
			else:
				standardform[i-counter] = int(temp[i])
		rounder = int(standardform[2])
		if int(standardform[3]) >= 5:
			rounder += 1
		else:
			pass
			
		power = counter-1
		finalnum = standardform[0] + '.' + standardform[1] + str(rounder) + 'x10' + '^-' + str(power)
		print(finalnum)
