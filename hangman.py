word = "rosemary"

man = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


board = ["_" for i in range(len(word))]

points = 0
attempts = 0

while True:

    if points == len(word):
        print(man[attempts])
        print("".join(board))
        print("\nYou win!")
        break

    if attempts == 6:
        print(man[attempts])
        print("\nYou lost!")
        print(f"The word was '{word}' ")
        break

    print(man[attempts])
    print("\n" + " ".join(board))
    guess = input("Enter a letter: ")

    if guess in board:
        print("\n[!] You already guessed that")
        continue

    if guess not in word:
        print("\nWrong!")
        attempts += 1
    else:
        for idx, char in enumerate(word):
            if char == guess:
                board[idx] = char
                points += 1
