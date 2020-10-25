# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:22:27 2020

@author: Frederik Haugaard Bruun
"""

#%% 1. Pythagorean theorem:
from math import sqrt

def pythagoras(a, b, c):
    if c == "?":
        a = float(a)
        b = float(b)
        return sqrt((a**2) + (b**2))
    elif b == "?":
        a = float(a)
        c = float(c)
        return sqrt((c**2) - (a**2))
    elif a == "?":
        b = float(b)
        c = float(c)
        return sqrt((c**2) - (b**2))
    
print("Please input 2 out of 3 values for the sides of the triangle.")
print("If the side is unknown please input a  \"?\" ")
a = input("Input value for side a: ")
b = input("Input value for side b: ")
c = input("Input value for side c: ")

         
print("The length of the unknown side is: " + str(pythagoras(a,b,c)))


#%% 2. Median value
from math import ceil

def median(L):
    L.sort()
    for item in L:
        if len(L) % 2 != 0:
            median_index = ceil(len(L) / 2)
            median = L[median_index]
        elif len(L) % 2 == 0:
            median_index1 = int(len(L) / 2)
            median_index2 = median_index1 + 1
            median = (L[median_index1] + L[median_index2]) / 2
    
    return median

my_list = [213, 34, 1 , 7, 9, 21, 43, 22]
print("The median of the list is: ", str(median(my_list)))

#%% 3. Unique list items
def unique(L):
    sub_list = []
    for item in L:
        if L.count(item) == 1:
            sub_list.append(item)
    
    return sub_list

my_list = [1, 1, 1, 1, 3, 3, 3, 2, 6, 7, 8, 2, 76]
print(unique(my_list))


#%% 4. Character count
def characters(textfile):
    text = open(textfile, 'r', encoding='utf-8')
    d = {}
    for line in text:
        for character in line:
            l = []
            l.append(character)
            for item in l :
                if item in d.keys():
                    d[item] += 1
                else:
                    d[item] = 1
    sorted_d = {}
    for key in sorted(d):
        sorted_d[key] = d[key]
    
    return sorted_d

print(characters('raven.txt'))

#%% 5. Word frequency
import matplotlib.pyplot as plt
import os

def count(term):
    frequencies = []
    chapters = []
    files = os.listdir("genesis/")
    count = 0
    file_list = []
    
    
    # Sorts the file list so they appear chronologically 
    for f in files:
        if len(f) == 13:
            file_list.append(f)
    
    for f in files:
        if len(f) == 14:
            file_list.append(f)
    
    
    for f in file_list:
        file = open('genesis/'+f, 'r', encoding='utf-8')
        chapters.append(file_list.index(f) + 1)
        text = file.read()
        words = text.split(" ")
        for w in words:
            if w == term:
                count = count + 1
        frequencies.append(count)
        count = 0
        
    plt.plot(chapters, frequencies)
    plt.xlabel("Chapters")
    plt.ylabel("Frequencies")
    plt.show()
        
    
count('God')
