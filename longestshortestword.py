# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:38:13 2024

@author: Anupam Nair
"""

file_n=open("D:\\python practice\\world.txt","w")


#ask the user for input

for i in range(5):    
    n=input("enter line:")    
    file_n.write(n)
    file_n.write('\n')
    
file_n.close()
    
    
file_r=open("D:\\python practice\\world.txt","r")

lines=file_r.readlines()

#print(lines)

short=0
long=0
word=[]

for line in lines:
    line=line.strip() #removing newline chars
    text=line.split() #splitting at every space
    word.extend(text)
print(word)   

long=max(word,key=len)
short=min(word,key=len)

print("the longest word is :",long,"and its length is:",len(long))
print("the shortest word is :",short,"and its length is:",len(short))
    
    
    
        
        
    
    
    
    