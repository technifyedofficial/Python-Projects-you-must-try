import random
print("Best of luck!!")
words = ['technifyed', 'alexa', 'apple', 'google', 'microsoft', 'physics',
'chemistry', 'mathematics', 'siri', 'windows', 'android']
hangmanWord = random.choice(words)
print("Guess the characters")
guesses = ''
chances = 12
while chances > 0:
	failed = 0
	for character in hangmanWord:
		if character in guesses:
			print(character)
		else:
			print("_")
			failed += 1
	if failed == 0:
		print("You WON")
		print("The word was", hangmanWord)
		break
	print()
	guessedLetter = input("guess a character:")
	guesses += guessedLetter
	if guessedLetter not in hangmanWord:
		chances -= 1
		print("Wrong")
		print("You have", + chances, 'more guesses')
		if chances == 0:
			print("You LOST")