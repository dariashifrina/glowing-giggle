from flask import Flask, render_template, redirect
import random

#Creation of dictionary
cool_file = open("data/occupations.csv", "r") #Open up our csv file so we can get to working on it
cool_list = cool_file.readlines() #Read the file in a way that each line is a list item
cool_file.close()
#print coolList
cool_dic = {} #Close up the file
i = 1 #this is going to be the index of our list!!
cool_list = cool_list[:len(cool_list)-1]

while (i<len(cool_list)):
     thisLine = cool_list[i] #Let's grab the current line
     last_comma = thisLine.rfind(",") #Let's also find the right comma - the one that seperates the number and value
     prelast_comma = thisLine[:last_comma].rfind(",")
     occupation =  thisLine[:prelast_comma].strip('"')
     percentage = thisLine[prelast_comma + 1: last_comma].strip('\n').strip("\r")
     link = thisLine[last_comma + 1:].strip('\n').strip("\r")
     cool_dic.setdefault(occupation, []).append(percentage)
     cool_dic.setdefault(occupation, []).append(link)
     #cool_dic[thisLine[:prelast_comma].strip('"')] = thisLine[comma + 1:].strip('\n').strip("\r") #Add the stuff before the comma (occupation) to the dictionary as a key, then add the stuff after the comma as a value!
     i += 1 #Wouldn't want an infinite loop now would we

#Returns a random occupation
def random_occupation():
    c = 0 #counter for while loop
    random_float = random.uniform(0.0, 99.8) #float within range
    #print random_float
    cumulative_probability = 0.0
    while (c < len(cool_dic)):
        cumulative_probability += float(cool_dic.values()[c][0])
        if (cumulative_probability>random_float):
            return cool_dic.keys()[c]
        c += 1

#Returns the helpful link to the corresponding occupation	
def occupation_link(occupation):
    return cool_dic[occupation][1]

def get_dic():
    return cool_dic