"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
	number_of_primes = int(number_of_primes)

	result_list = []

	if number_of_primes <= 0:
		raise ValueError

	if number_of_primes == 1:
		return [2]
	elif number_of_primes > 1:
		result_list.append(2)

	starting_number = 3
	while len(result_list) < number_of_primes: 
	# if the result list is les than number_of_primes then we still keep going
		isPrime = True
		# It is sufficient to check only up to square root of n - good performance
		for i in range(2, int(starting_number**0.5) + 1):
			if (starting_number % i == 0):
				isPrime = False
				break

		if isPrime == True:
			result_list.append(starting_number)

		starting_number+=1
	
	return result_list