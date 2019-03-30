# This is the Guessing Game!
import random

def get_num(a, b):
	random_num = random.randint(a, b)
	return random_num

def main():
	print("Welcome to the Guessing Game!")

	lower_limit = 1
	upper_limit = 5
	correct = True
	num_hints = 0     # this variable will keep track of the number of hints

	# we have to get an initial random number before we enter the while loop
	number = get_num(lower_limit, upper_limit)

	while correct == True:
	
		print "The range is", lower_limit, "to", upper_limit
		guess = int(input("Enter your guess: "))

		# if they request their first hint 
		if guess == 0 and num_hints == 0:
			if number >= upper_limit / 2: # checks to see if the number is in the upper half or if it is the median
				print "The number is greater than or equal to", (upper_limit / 2)
			else: # it is in the lower half
				print "The number is less than", (upper_limit / 2)
			num_hints = num_hints + 1 # we have to increment the number of hints we have given them
		
		# if they request their second hint
		elif guess == 0 and num_hints == 1:
			if number % 2 == 0: # if the remainder of the number / 2 is 0, our number is even
				print "The number is even"
			else:
				print "The number is odd"
			num_hints = num_hints + 1

		# if they request their third hint
		elif guess == 0 and num_hints == 2:
			if number % 3 == 0: # if the remainder of the number / 3 is 0, our number is divisible by 3
				print "The number is divisible by 3"
			else:
				print "The number is not divisible by 3"
			num_hints = num_hints + 1

		# if they request for a hint but they are out of hints
		elif guess == 0:
			print "You are out of hints! You have to guess!"

		elif guess == number:
			print "Your guess was", guess, "and the number was", number
			print "You guessed correctly!"
			upper_limit = upper_limit + 5
			number = get_num(lower_limit, upper_limit) # we have to get a new random number
			num_hints = 0 # we have to reset the number of hints we have given them

		else:
			print "your guess was", guess, "and the number was", number
			print "Whoops! You were wrong!"
			correct = False


main()
