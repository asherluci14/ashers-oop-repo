import random


def choose_hidden_word():
    # Readying the file
    infile = open('pokemon-2-1.txt', 'r')
    text = infile.read()
    infile.close()

    # Splitting the string into a list of pokemon
    pokemon_list = text.split(',')

    # Removing whitespace
    for i in range(0, len(pokemon_list)):
        pokemon_list[i] = pokemon_list[i].strip().lower()

    # Choosing one random pokemon from the list
    pokemon = random.choice(pokemon_list)
    return pokemon


def display_word(hidden_word, guessed_letters):
    word = ''

    for letter in hidden_word:
        if letter in guessed_letters:
            word += letter
        else:
            word += '_'

        word += ' '

    print(word)

def play_game():
    game_complete = False
    guessed_letters = []
    guess_count = 0

    pokemon = choose_hidden_word()

    while not game_complete:
        print("----------------------------------")
        print()
        display_word(pokemon, guessed_letters)
        print(f"Guesses so far: {guess_count}")
        print(f"Letters guessed so far: ", end='')
        for letter in guessed_letters:
            print(letter, end=' ')

        print('\n')

        guess = input("Enter a letter: ")
        guess = guess.strip().lower()

        if len(guess) == 1 and guess.isalpha():
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                guess_count += 1
            else:
                print("You have already guessed this letter. Please try again.")
        else:
            print("You must enter only one alphabetical character. Please try again.")

        correct_letters = 0

        for letter in pokemon:
            if letter in guessed_letters:
                correct_letters += 1

        if correct_letters == len(pokemon):
            game_complete = True


    print()
    print(f"Congratulations! You guessed {pokemon.upper()} in {guess_count} guesses!")


play_game()


