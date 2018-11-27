# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:32:08 2018

@author: Javier Soon
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Given a word list create a hash table, find the anagrams
for a given word in the word list, and find the largest anagram from the 
word list.
"""

import ChainingHashTable 
import time
count = 0
count1 = 0



# =============================================================================
# reads the text file, and at the same time creates the hashtable called
# english_words
# =============================================================================
def file_reader(word_file, initial_capacity):
    english_words = ChainingHashTable.ChainingHashTable(int(initial_capacity))   #calls the class ChainingHashTable from the module ChainingHashTable 
                                                                                # it also takes in a int variable to determine the size of the table
    with open(word_file) as file:
        for line in file:
            english_words.insert(str.lower(line.strip('\n'))) # strips the white default space 
        return english_words
    
    

# =============================================================================
# another print but will be used to find the maxes
# =============================================================================                   
def print_anagrams(user_search_word, english_words, prefix=""):
    global count
    
    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word
#        print((str1))    # prints the word that it just did an anagram for (repeats are included)
       
        if english_words.search(str1):  # looks for str in the tree
            count += 1
            print(prefix + user_search_word)
            print_anagrams(str1, english_words, prefix) 
            
    else:
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
            
            if cur not in before:  # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)   
    return count


def print_anagrams2(user_search_word, english_words, count1, prefix=""):

    if len(user_search_word) <= 1:
        str1 = prefix + user_search_word

#        print(str1)
#        print(len(str1))    # prints the word that it just did an anagram for (repeats are included)
  
        if english_words.search(str1):  # looks for str in the tree
            count1 += 1
            return count1 + print_anagrams2(str1, english_words, count1, prefix) 

    else:
        
        for i in range(len(user_search_word)):
            cur = user_search_word[i: i + 1]
            before = user_search_word[0: i]  # letters before cur
            after = user_search_word[i + 1:]  # letters after cur
        
            if cur not in before:  # Check if permutations of cur have not been generated.
                return count1 + print_anagrams2(before + after, english_words, count1, prefix + cur)  


    return count1

# =============================================================================
#   finds the max number of anagrams and the word 
# =============================================================================
def max_ana(english_words, words_file):
    max = -1    # will hold the max number of anagrams
    max_word = " "  # will hold the word of the max 

    
    with open (words_file, "r") as list:
        for i in list:
            count = 0

            line = (str.lower(i.strip('\n'))) # strips the white default space 
#            print(line)

            count_a = print_anagrams2(line, english_words, count)
                        
            if max < count_a:
                max = count_a
                max_word = line         
                
    print('This is the largest anagram word is: ' , max_word)
    print(' with ' , max ,' anagrams')
    
def user(english_words):
    user_search = input('What word do you want to use: ')
    search = english_words.search(user_search)
    if search == None:
        print('Word is not in HashTable')
        print('GoodBye!')
        main.exit()
    print('The word exists in the Hash Table.')
    return user_search
                    
                    

                    
def main():
    word_file = ('words.txt')
    size = input('What Hash size do you want: ')
    
# =============================================================================
#     creates the hash table
# =============================================================================
    starttime = time.time()

    english_words = file_reader(word_file, size)
#    print(english_words)     # prints the hash table
    endtime = time.time()
    runtime = endtime - starttime
    print(runtime)
    print(runtime * 1000)
    
# =============================================================================
#   asks the user for the word that they want to do the anagrams for and checks
#    if it is it the hash table first
# =============================================================================
    user_in = user(english_words)
    
# =============================================================================
#     anagram for the user's word and count
# =============================================================================
    starttime1 = time.time()
    
    count_ana = print_anagrams(user_in, english_words)
    print('There are: ' , count_ana , ' anagrams for the word.')
    
    endtime1 = time.time()
    runtime1 = endtime1 - starttime1
    print(runtime1 * 1000)    
# =============================================================================
#     prints the largest anagram 
# =============================================================================
#    print('Hello, there. Ahh General Kenobi!')
#    max_ana(english_words, word_file)
    
# =============================================================================
#    calculates and prints the load factor for the hash table 
# =============================================================================
    starttime2= time.time()
    
    load = english_words.load_factor()
    print('The load factor is: ' , load)
    # Robert- This could be a one liner since you dont use load again 
    # print('The load factor is: ' , english_words.load_factor())
    
    endtime2 = time.time()
    runtime2 = endtime2 - starttime2
    print(runtime2 * 1000)
main()
#Robert Corral - Code Review
'''
As before i belive the def discription goes after the def decleration line
check style guide that Manoj sent us other than that good stuff
'''
