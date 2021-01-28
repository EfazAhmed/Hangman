import random


# image that is used when user has 6 strikes
def default():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_1():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_2():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |        |      ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_3():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |       /|      ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_4():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |       /|\     ")
    print("|  |               ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_5():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |       /|\     ")
    print("|  |       /       ")
    print("|  |               ")
    print("|  |               ")


# image that is used when user has 6 strikes
def strike_6():
    print(" _________________ ")
    print("|   ______________|")
    print("|  |        |      ")
    print("|  |        |      ")
    print("|  |        O      ")
    print("|  |       /|\     ")
    print("|  |       / \     ")
    print("|  |               ")
    print("|  |               ")


# this function checks if the user's guess is one letter
def check_guess(letter):
    if not letter:
        print("You didn't make a guess! Please guess again!")
    elif letter.isalpha() and len(letter) == 1:
        return True
    elif len(letter) > 1:
        print("You've guesses more than one letter! Please guess again!")
    else:
        print("Don't enter numbers. Please guess again!")


# this function picks a random word from the word list
def pickWord():
    return random.choice(word_list)


# this function updates the current answer that the user has given
# this function also takes into account duplicate answers
def update(letter):
    global strikes
    global current_answer
    global selected_word
    right = 0
    if not check_guess(letter):
        return
    for i in range(0, len(selected_word)):
        if letter in selected_word[i] and selected_word[i] != "_ ":
            current_answer[i] = letter + " "
            right = right + 1
    if right == 0:
        if letter not in guesses_list:
            strikes = strikes + 1
            print("You've guesses a wrong letter!")
        else:
            print("You've already guess that!")
    if right > 0 and letter in guesses_list:
        print("You've already guess that!")
    if right > 0 and guess not in guesses_list:
        print("You've guess a correct letter!")
    if check_guess(letter) and letter not in guesses_list:
        guesses_list.append(letter)


# this function updates the current image based on the amount of strikes the user has
def image():
    if strikes == 0:
        default()
    elif strikes == 1:
        strike_1()
    elif strikes == 2:
        strike_2()
    elif strikes == 3:
        strike_3()
    elif strikes == 4:
        strike_4()
    elif strikes == 5:
        strike_5()
    elif strikes == 6:
        strike_6()


# this function resets all values that were initialized in the beginning of the program when playing again
def reset():
    global selected_word
    global current_answer
    global guesses_list
    global strikes
    global play
    global word
    word = pickWord().upper()
    selected_word = []
    current_answer = []
    guesses_list = []
    strikes = 0
    play = True
    for i in range(0, len(word) - 1):
        current_answer.append("_ ")
        selected_word.append(word[i] + " ")
    print("word: " + "".join(current_answer))
    default()


# -----------------------------------------------------------------
word_list = []
with open('Word_List.txt', 'r') as file:
    for line in file:
        word_list.append(line)

selected_word = []
current_answer = []
guesses_list = []
strikes = 0
play = True

print("Enter anything when ready to start!")
x = input()
word = pickWord().upper()
selected_word = []
current_answer = []
for i in range(0, len(word) - 1):
    current_answer.append("_ ")
    selected_word.append(word[i] + " ")

print("Word: " + "".join(current_answer))
default()

while play:
    # print(selected_word)
    # print(current_answer)
    guess = input("Your guess is: ").upper()
    if check_guess(guess):
        update(guess)
        print("Word: " + "".join(current_answer))
        image()
    else:
        print("Word: " + "".join(current_answer))
        image()
        continue

    answer = ""
    if current_answer == selected_word or strikes == 6:
        play = False
        if current_answer == selected_word:
            print("You got it!")
        else:
            print("You lost the game! The word was " + word)
        answer = input("Do you want to play again?(Y/N): ")
        if answer.upper() == "Y":
            play = True
            reset()
        elif answer.upper() == "N":
            print("Thanks for playing!")
            break
        else:
            while answer != "N" or answer != "Y":
                answer = input("Sorry I couldn't understand you. Was that a Y or a N? ")
                if answer.upper() == "Y":
                    play = True
                    reset()
                    break
                elif answer.upper() == "N":
                    print("Thanks for playing!")
                    break
