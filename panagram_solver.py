#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
import os
import pdb
from random import choice, shuffle
# Global variables

# Class declarations

# Function declarations

def show_word(valid_words, words_shown):
	searching = True
	while(searching):
		att = choice(valid_words)
		if att not in words_shown:
			searching = False
	return att

def split(word): 
    return [char for char in word]

def main():
    words_path = './corncob_lowercase.txt'
    with open(words_path) as f:
    	words = f.read().splitlines()

    center = input("Center letter: ")
    letters = input("Outside letters: ")

    letters = split(letters)
    letters.append(center)
    #center = 'l'
    #letters = list('lnupoar')

    valid_words = []
    word_counter = 0
    for word in words:
    	word_counter += 1
    	if not word_counter % 10000:
    		print("..")
    	if word[0].isupper():
    		continue

    	word_list = list(word.lower())
    	if len(word_list) < 4:
    		continue

    	if center in word_list:
    		flag = 1
    		for val in word_list:
    			if val not in letters:
    				flag = 0
    				continue
    		if flag:
    			valid_words.append(word)


    # finding panagram
    panagram = ""
    for word in valid_words:
    	flag = 1
    	for letter in letters:
    		if letter not in word:
    			flag = 0
    	if flag:
    		panagram = word
    		break

    playing = True
    print("word list created, hit enter for a hint, or type \'panagram\', \'word\' or \'quit\'")
    print("")
    words_shown = []
    shuffle(valid_words)
    while(playing):
    	new = input()
    	if new == 'quit' or new == 'q':
    		playing = False
    		print('All done!')
    	elif new == 'word' or new == 'w':
    		# word = show_word(valid_words, words_shown)
    		word = valid_words.pop()
    		print(word)
    		words_shown.append(word)
    	elif new == 'panagram' or new == 'p':
    		if panagram:
    			print(panagram)
    		else:
    			print('no panagram found! :(')
    	elif new == 'all':
    		while(valid_words):
    			word = valid_words.pop()
    			print(word)
    			words_shown.append(word)
    	else:
    		# hint = show_word(valid_words, words_shown)
    		hint = valid_words.pop()
    		hint_start = hint[:3]
    		while(len(hint_start) < len(hint)):
    			hint_start = hint_start + "*"
    		print(hint_start)
    		words_shown.append(hint)
    	if not valid_words:
    		playing = False
    		print('Those are all of the words we got!!')



# Main body
if __name__ == '__main__':
    main()
