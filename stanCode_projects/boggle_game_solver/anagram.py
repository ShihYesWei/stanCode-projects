"""
File: anagram.py
Name: Alan Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 21

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'      # Controls when to stop the loop

# Global variable
dictionary = []  # A python list of vocabulary from FILE = 'dictionary.txt'
alpha_dict = {}  # A python dict for saving the input words of [order : alphabet]
num_list = []    # A python list for saving integers with the length of the input vocabulary
printed = []     # A python list for saving the printed anagrams


def main():
    """
    this function read the dictionary and save it into a python list first
    and waiting for user to input vocabulary
    alpha_dict, num_list and printed
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or ' + str(EXIT) + ' to quit) ')
    global num_list
    global alpha_dict
    global printed
    while True:
        vocabulary = input('Find anagrams for: ')
        if vocabulary == EXIT:
            break
        else:
            sub_s = []  # initialize after a new input
            num_list = []  # initialize after a new input
            alpha_dict = {}  # initialize after a new input
            printed = []  # initialize after a new input
            make_dict(vocabulary)
            make_list(vocabulary)
            print('Searching...')
            find_anagrams(vocabulary, num_list, sub_s)
            print(f'{len(printed)} anagrams: {printed}')


def find_anagrams(s, l, new_l):
    """
    finding anagrams by permuting the integers in python list: num_list
    :param s: (str) the input vocabulary
    :param l: (list) the number list from python list: num_list
    :param new_l: (list) the new list for permutation of list l
    """
    if len(new_l) == len(s):  # base case: the potentially anagram word is finished
        word = translation(new_l)
        if word in dictionary and word not in printed:  # check whether the anagram is a word and have not been printed
            print('Found: ', end='')
            print(word)
            print('Searching...')
            printed.append(word)
    else:  # recursive case
        if not has_prefix(new_l):   # if the combination so far is not prefix of any word, then skip.
            return
        for i in range(len(l)):
            order = l[i]
            if order not in new_l:
                new_l.append(order)
                find_anagrams(s, l, new_l)
                new_l.pop()


def read_dictionary():
    """
    read the dictionary.txt and save the words into the python list: dictionary
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            dictionary.append(line)


def make_dict(s):
    """
    save each units of input vocabulary with its order

    for example:
    when the input word is "stop"
    this dict will save {0: 's', 1: 't', 2: 'o', 3: 'p'}

    :param s: (str) the input vocabulary
    """
    for i in range(len(s)):
        alpha_dict[i] = s[i]


def make_list(s):
    """
    make a list of integer with the length of the input vocabulary
    by combining this list and the make_dict, finding anagrams is just like dealing with permutation.

    for example:
    when the input word is "stop"
    this list will save [0, 1, 2, 3]

    :param s: (str) the input vocabulary
    """
    global num_list
    for i in range(len(s)):
        num_list.append(i)


def translation(number_list):
    """
    transform the number into combination of words according to alpha_dict

    for example:
    when the input word is "stop", the alpha_dict saves: {0: 's', 1: 't', 2: 'o', 3: 'p'}
    when the given number_list is [3, 2, 1, 0]
    this function returns "pots"

    :param number_list: (list) list of integers
    :return word: (str) the translated word
    """
    word = ''
    for number in number_list:
        word += alpha_dict[number]
    return word


def has_prefix(n_lst):
    """
    This function will search whether the dictionary have the word of the prefix so far
    and aim to shorten the searching time.

    :param n_lst: (list) combination of the integer, upon input will be translated
    :return: (boolean) if word(s) with the prefix exist, return True
    """
    s = translation(n_lst)
    for word in dictionary:
        if word.startswith(s):
            return True
    return False


if __name__ == '__main__':
    main()
