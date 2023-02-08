#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1) What is the output of the following code and why? 

# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# a) 6 
# b) 33 
# c) 3 + 3 
# d) Error 

# d, because python doesn't add strings and integers together


# In[20]:


var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)


# In[ ]:


# 2) What is the output of the following code? 

# str = "pynative"

# print (str[1:3])

# a) py
# b) yn
# c) pyn
# d) yna

#b, because the string become a list, and the letters correlate to the numbers, and arrays always starts 
# at zero.


# In[21]:


str = "pynative"

print (str[1:3])


# In[ ]:


# 3) What is the output of the following code? 

# var= "James Bond"
# print(var[2::-1])

# a) Jam
# b) dno
# c) maJ
# d) dnoB semaJ

# the answer is c


# In[23]:


var= "James Bond"
print(var[2::-1])


# In[ ]:


# 4) What is the output of the following code? 

# var = "James" * 2  * 3
# print(var)

# a) JamesJamesJamesJamesJamesJames
# b) JamesJamesJamesJamesJames
# c) Error: invalid syntax

# the answer is a


# In[25]:


var = "James" * 2  * 3
print(var)


# In[16]:


# 5) Get rid of the non fruit item: 

# sweets = ['apple', 'bananas', 'cantelopes', 'donut']

my_list = ['apple', 'bananas', 'cantelopes', 'donut']

#my_list = ['apple', 'bananas', 'cantelopes', 'donut']

#my_list.remove('donut')

#print(my_list)


# In[27]:


my_list = ['apple', 'bananas', 'cantelopes', 'donut']

my_list.remove('donut')

print(my_list)


# In[19]:


# 6) Find "santa" in the variable "house" 


 #room1=['gabe','greg']
 #room2=['michelle','santa','stacey']
 #room3=['adam','sam', 'melissa']
 #house=[room2, room1, room3]


# In[33]:




room1=['gabe','greg']
room2=['michelle','santa','stacey']
room3=['adam','sam', 'melissa']

house=[room2, room1, room3]

house[0][1]



# In[ ]:


# 7) A dictionary is the best way to store a sequence of events like a recipe.

# True or false? 
 
#false


# In[5]:


# 8) Remove all dupes 
# names = ['mary', 'bob', 'jessica', 'pierre', 'bob', 'jennifer', 'chris', 
#          'christina', 'tina', 'mary', 'tina', 'bob', 'michelle','jennifer']
#my_list = ['mary', 'bob', 'jessica', 'pierre', 'bob', 'jennifer', 'chris', 
#          'christina', 'tina', 'mary', 'tina', 'bob', 'michelle','jennifer']


# In[54]:


l = ['mary', 'bob', 'jessica', 'pierre', 'bob', 'jennifer', 'chris', 
         'christina', 'tina', 'mary', 'tina', 'bob', 'michelle','jennifer']
print("Original List: ", l)
res = [*set(l)]
print( res)


# In[ ]:


# 9) What's the difference between = and == ? 
# = is a simple assignment operator (declarative), while == checks if two things are equal (inquiry)


# In[78]:


# 10) 

# Use the concepts you learned in class to construct a poem. Please make sure you write your own poem. There are no guidelines to writing this poem but if you want, feel free to following traditional poem formats like ballads, sonnets, haikus or more.  

# See below for example. I expect yours to have a bit more elegant. 

# Credit Poem: "Still I Rise" by Maya Angelou 

# Reference: https://www.popwebdesign.net/popart_blog/en/2018/01/code-poetry-poems-written-in-programming-languages/ 

print('this sentence will form a vase, and this is how')
print('      Sentence will form a vase and this is')
print('           Will form a vase and this')
print('                Form a vase and')
print('                     A vase')
print('                      vase')
print('                     A vase')
print('                 Form a vase and')
print('            Will form a vase and this')
print('      Sentence is still forming a vase,how')
print ('This sentence has formed a vase, and that is how')
print('\n')

print('This sentence will form a wormhole, and you will see')
print('      Sentence will form a wormhole and you see')
print('           Will form a wormhole')
print('                  Form wormhole')
print('                     Wormhole')
print('                      Form')
print('                     Wormhole')
print('                 Formed Wormhole')
print('      Sentence has formed a wormhole you saw')
print ('This Sentence has formed a wormhole and you saw')
print('\n')

print('this sentence will form afunnel and Ill show you')
print('      Sentence will form funnel, Ill show')
print('               Will form a funnel')
print('                  Form funnel')
print('                     Funnel')
print('                  Funnel Formed')
print('                Funnel was Formed')
print('                 Form a vase and')
print('      Sentence has formed funnel, you saw')
print ('This sentence has formed a funnel, you know it')
print('\n')




print('These shapes and words are interesting because')
print ('I can now create all sorts of different forms through them')
print ('I can now create specific  shapes , words. I have the power to make sort, form, and sent^i^ence')

poem_list = ['I', 'now', 'create', 'specific', 'shapes', 'words', 'I', 'have', 'the', 'power', 'to', 'make', 'sort', 'form', 'and', 'sent^i^ence']
poem_list =dict([(1,'I'), (2,'now'), (3,'create'), (4,'specific'), (5,'words'), (6,'have'), (7,'power'), (8,'make'),(9,'and'),(10,'sent^i^ence')])
favorites = {'power':['I', 'create','specific', 'words', 'and', 'sent^i^ence']}
favorites['power']

    


# In[43]:


a = "I Rise"
b = "by maya angelou"

print (f'Still {a}')
print('\n')
print(b.upper())
print('\n')
print('With your bitter, twisted lies,')
print('You may trod me in the very dirt')
print("But still, like dust, I'll rise.")
print('\n')
print('Does my sassiness upset you?')
print('Why are you beset with gloom?')
print("’Cause I walk like I've got oil wells")
print('Pumping in my living room.')
print('\n')
print('Just like moons and like suns,')
print('With the certainty of tides,')
print('Just like hopes springing high,')
print("Still I'll rise.")
print('\n')
print('Did you want to see me broken?')
print('Bowed head and lowered eyes?')
print('Shoulders falling down like teardrops,')
print('Weakened by my soulful cries?')
print('\n')
print('Does my haughtiness offend you?')
print("Don't you take it awful hard")
print("’Cause I laugh like I've got gold mines")
print('Diggin’ in my own backyard.')
print('\n')
print('You may shoot me with your words,')
print('You may cut me with your eyes,')
print('You may kill me with your hatefulness,')
print('But still, like air, I’ll rise.')
print('\n')
print('Does my sexiness upset you?')
print('Does it come as a surprise')
print("That I dance like I've got diamonds")
print('At the meeting of my thighs?')
print('\n')
print('Out of the huts of history’s shame')
print (f'{a}')
print('Up from a past that’s rooted in pain')
print (f'{a}')
print("I'm a black ocean, leaping and wide,")
print('Welling and swelling I bear in the tide.')
print('\n')
print('Leaving behind nights of terror and fear')
print (f'{a}')
print('Into a daybreak that’s wondrously clear')
print (f'{a}')
print('Bringing the gifts that my ancestors gave,')
print('I am the dream and the hope of the slave.')
print (f'{a}')
print (f'{a}')
print (f'{a}.')

