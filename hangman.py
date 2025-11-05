import random

words = ["Python", "Hangman", "Pandas", "Office"]

# randomly chooses from the list above
chosen_word = random.choice(words).lower()
display_words = ['_' for _ in chosen_word]

attempts = 8    # number of allowed attempts

print("Welcome to Hangman game")

while attempts > 0 and '_' in display_words:
    print("\n" + ' '.join(display_words))
    guess = input("Guess the letter: ").lower().strip()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                # Basically reveals the correct letter
                display_words[index] = guess

    else:
        attempts -= 1
        print(f"You chose a wrong word, you have {attempts} attempts left.")

if '_' not in display_words:
    print("You have guessed the word.")
    print(' '.join(display_words))
    print("Congo you won.")
else:
    print("You are out of attempts, the word was: " + chosen_word)
    print("You failed!!")
