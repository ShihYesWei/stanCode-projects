"""
File: hangman.py
Author: Alan Chen
-----------------------------
This program plays hangman game.
User will be first told how many characters in the word represented by dashes (-).
If the answer is correct, the dashes will reveal.
The game ends when the wrong guesses achieved N_TURNS or figure out the answer.
The progression of execution will be demonstrated: Head, body, left hand, right hand, right feet, left feet, and death.
"""

import random


N_TURNS = 7
# This constant controls the number of guess the player has


def main():
    """
    This function plays a hangman game.
    Characters in the word will be covered by dashes (-) at the beginning
    Once the correct answer inputted, the Characters will be revealed.
    The game ends when the wrong guesses achieved N_TURNS or figure out the answer.
    The progression of execution will be demonstrated.
    """
    ans = random_word()
    # answer of the random word.
    re_ans = ''
    # the reply to the guess.
    times = N_TURNS
    # how many times left until the game ends.
    hang_man_print(times)
    print('The word looks like: ', end='')
    for i in range(len(ans)):
        re_ans += '-'
    print(re_ans)
    while re_ans.find('-') != -1:
        # This while loop continues until there is no "-" in the re_ans.
        print('You have ' + str(times) + ' guesses left.')
        guess = input('Your guess: ')
        while fit_format(guess) == 0:
            # check the format of input
            print('illegal format.')
            guess = input('Your guess: ')
        guess = guess.upper()
        # case-insensitive
        pos = ans.find(guess)
        # find the guess in the ans.
        s = ''
        # s for string
        if pos == -1:
            # means there is no matches alphabet in the ans.
            times -= 1
            print('There is no ' + guess + '\'s in the word.')
            hang_man_print(times)
            if times >= 1:
                print('The word looks like: ' + str(re_ans))
            if times == 0:
                # wrong guesses for 7 times, lose.
                print('You are completely hung : (')
                print('The word was: ' + ans)
                break
        else:
            # there is matched alphabet in the ans.
            for i in range(len(ans)):
                if ans[i] == guess:
                    s += guess
                else:
                    s += re_ans[i]
            re_ans = s
            print('You are correct!')
            if re_ans.find('-') != -1:
                # there are still '-' exist in re_ans means not yet solved.
                print('The word looks like: ' + str(re_ans))
            else:
                # The word is completely figured out.
                print('You win!!')
                print('The word was: ' + ans)
                print('Oh! See, you know the word! You are acquitted now.')
                times = 8
                # this is for printing hanger only because the man is acquitted.
                hang_man_print(times)
                acquit()


def fit_format(guess):
    """
    This function tells whether the guess input fit the format (one alphabet only)
    :param guess: str, one alphabet.
    :return: 0 or 1: 0, reject, the guess didn't fit the format; 1, pass, the guess fit the format
    """
    if len(guess) > 1:
        return 0
    else:
        if guess.isalpha():
            return 1
        else:
            return 0


def hang_man_print(times):
    """
    This function prints the progression of the man being hung and also interact with user.
    :param times: int, how many chances left for wrong guesses.
    """
    if times == N_TURNS:
        print('You are sentenced death for forgetting an important word!')
        print('Recall or DEAD!')
    if times == 6:
        print('Give you a hint, this is an English word!')
    if times == 5:
        print('One more hint, there must be at least one vowel in this word.')
    if times == 3:
        print('Come on! You knew the word, didn\'t you?')
    if times == 1:
        print('Look! Death is approaching, here comes the last chance!')
    print('  ______   ')
    print('  |    |')
    if times >= 7:
        print('  |    ○')  # 7
    elif times < 7:
        if times > 0:
            print('  |    ( )')  # 6-1
    if times == 0:
        print('  |    (xx)')  # 0
    if times == 5:
        print('  |    |')  # 5
    if times == 4:
        print('  |    |＼')  # 4
    if times < 4:
        print('  |   /|＼')  # 3-0
    if times == 2:
        print('  |  　/')  # 2
    if times < 2:
        print('  | 　 /\\')  # 1-0
    print('  |')
    print('--┴--------')


def acquit():
    """
    This function prints the "un"hangman hooray for being acquitted.
    """
    print('                 www   ')
    print('               \(^o^)/ ')
    print('                  |')
    print('                　/\\')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
