"""
File: boggle.py
Name: Alan Chen
----------------------------------------
Boggle is a popular board game in America.
In a 4x4 letters array, players will try to find out words longer than 4 letters.
This program find out all the words in the 4x4 letters array.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dictionary = []  # A python list of vocabulary from FILE = 'dictionary.txt'
printed = []


def main():
    """
    This function reads the dictionary first,
    then ask users to input
    if the input is in legal format,
    it will start the searching
    """
    read_dictionary()
    boggle_box = input_boggle()
    if len(boggle_box) == 4 and boggle_box[3]:
        find(boggle_box)
        print(f'There are {len(printed)} words in total.')


def find(boggle_box):
    """
    The 16 starting point of the words.
    The boggle_box will be like this:
        [['f', 'y', 'c', 'l'], #0,0   0,1   0,2   0,3
         ['i', 'o', 'm', 'g'], #1,0   1,1   1,2   1,3
         ['o', 'r', 'i', 'l'], #2,0   2,1   2,2   2,3
         ['h', 'j', 'h', 'u']] #3,0   3,1   3,2   3,3
    """
    for y in range(4):
        for x in range(4):
            word = []
            path = []
            word.append(boggle_box[x][y])  # every start point
            path.append((x, y))
            find_helper(x, y, word, path, boggle_box)


def find_helper(x, y, word, path, boggle_box):
    """
    helper function of finding anagrams
    :param x:(int) the x position in the boggle_box
    :param y:(int) the y position in the boggle_box
    :param word: (list) a list of letters
    :param path: (list) containing tuples of the used position
    :param boggle_box: (list) a 2D list of the letters
    """
    if len(word) == 4:
        if combine(word) not in printed:
            if has_prefix(word):
                if combine(word) in dictionary:
                    print(f'Found: "{combine(word)}"')
                    printed.append(combine(word))
                    elongation(x, y, word, path, boggle_box)
                else:
                    word_longer_than_4(x, y, word, path, boggle_box)
    else:
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if 4 > j >= 0 and 4 > i >= 0:
                    if (i, j) not in path:
                        word.append(boggle_box[i][j])
                        path.append((i, j))
                        find_helper(i, j, word, path, boggle_box)
                        word.pop()
                        path.pop()


def word_longer_than_4(x, y, word, path, boggle_box):
    """
    This function is for those word longer than 4 words and are in the corresponding prefix.
    For example:
    "nurs" is not a word, but "nurse" is.
    """
    if has_prefix(word):
        if combine(word) in dictionary and combine(word) not in printed:
            print(f'Found: "{combine(word)}"')
            printed.append(combine(word))
        else:
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if 4 > j >= 0 and 4 > i >= 0:
                        if (i, j) not in path:
                            word.append(boggle_box[i][j])
                            path.append((i, j))
                            word_longer_than_4(i, j, word, path, boggle_box)
                            word.pop()
                            path.pop()


def elongation(x, y, word, path, boggle_box):
    """
    This function is for those have 4-letter words and to elongate more letters on it.
    For example:
    "room" is already a word, and "roomy" is also a word
    """
    if combine(word) in dictionary and combine(word) not in printed:
        print(f'Found: "{combine(word)}"')
        printed.append(combine(word))
    else:
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if 4 > j >= 0 and 4 > i >= 0:
                    if (i, j) not in path:
                        word.append(boggle_box[i][j])
                        path.append((i, j))
                        if has_prefix(combine(word)):
                            elongation(i, j, word, path, boggle_box)
                        word.pop()
                        path.pop()


def input_boggle():
    """
    This function ask user to input 4 rows of 4 letters spacing with ' '
    if the format doesn't fulfill the requirement of input, the program stops directly
    :return: boggle_box (list): the 4x4 letters array
    """
    boggle_box = []
    for i in range(4):
        if i == 0:
            box1 = input('1 row of letters: ')
            box1 = box1.lower()
            boggle_box.append(deal_with_input(box1))
            if not boggle_box[0]:
                break
        elif i == 1:
            box2 = input('2 row of letters: ')
            box2 = box2.lower()
            boggle_box.append(deal_with_input(box2))
            if not boggle_box[1]:
                break
        elif i == 2:
            box3 = input('3 row of letters: ')
            box3 = box3.lower()
            boggle_box.append(deal_with_input(box3))
            if not boggle_box[2]:
                break
        elif i == 3:
            box4 = input('4 row of letters: ')
            box4 = box4.lower()
            boggle_box.append(deal_with_input(box4))
            if not boggle_box[3]:
                break
    return boggle_box


def deal_with_input(box):
    """
    This function will check the format of input rows.
    If user input non-alphabet or not single letters or no space between letters,
    it will print 'Illegal input'.
    If the input format is correct, the input string will be transform into list

    for example:
    an input of "a b c d" will be save into a list ['a', 'b', 'c', 'd']
    :return: list_of_box (list) when legal format: a list contain 4 alphabets, when illegal format: empty list
    """
    list_of_box = []
    if len(box) != 7:
        print('Illegal input')
    else:
        if box[1] is not ' ' or box[3] is not ' ' or box[5] is not ' ':
            print('Illegal input')
        elif box[0].isalpha() and box[2].isalpha() and box[4].isalpha() and box[6].isalpha():
            list_of_box.append(box[0])
            list_of_box.append(box[2])
            list_of_box.append(box[4])
            list_of_box.append(box[6])
        else:
            print('Illegal input')
    return list_of_box


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            dictionary.append(line)


def combine(sub_s):
    """
    This function combine the list of sub-string into a word
    and I don't know why I cannot enter here or it will make error
    """
    word = ''
    for i in range(len(sub_s)):
        word += sub_s[i]
    return word


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    w = combine(sub_s)
    for word in dictionary:
        if word.startswith(w):
            return True
    return False


if __name__ == '__main__':
    main()
