number_of_lives = int(input("Number of Lives: "))
hidden_word = input("Input the word: ").upper()
board = []
for i in range(len(hidden_word)):
    board.append("_")
print(board)
print("Guess the " + str(len(hidden_word)) + " letters.")
points = 0
fails = 0

while (fails < number_of_lives or points < len(hidden_word)):
    guess = input('Guess a letter:').upper()
    if guess in hidden_word:
        for i in range(len(hidden_word)):
            if hidden_word[i] == guess:
                points += 1
                board[i] = guess
            else:
                continue
        print(board)
    else:
        fails += 1
        print("Wrong Guess")
    
    if fails > number_of_lives:
        print("Game Over: No more lives for the man :(")
        break
    elif points == len(hidden_word):
        print("Hangman Lives")
        break