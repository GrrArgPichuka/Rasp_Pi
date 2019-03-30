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

	while correct == True:
		number = get_num(lower_limit, upper_limit)
	
		print "The range is", lower_limit, "to", upper_limit
		guess = int(input("Enter your guess: "))

		print "Your guess was", guess, "and the number was", number

		if guess == number:
			print "You guessed correctly!"
			upper_limit = upper_limit + 5
		else:
			print "Whoops! You were wrong!"
			correct = False


main()
