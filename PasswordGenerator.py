import random
import string

'''
this code is for creating a password by using a list of words instead of just pulling random characters
so that the password is easier to remember, currently not sure how to have the program pull from the list of words,
then create a combination of the words from the list to match the number of characters requested in the length. 
Will work on that in the future. The usa.txt file is included in the github if you want to try and work on it yourself.

text_file = open('usa.txt', 'r')
file_content = text_file.read()
content_list = file_content.split('\n')
'''


#user inputs length of password they would like
length = int(input('\nPassword length: '))

#variables
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

#randomizing the characters
temp = random.sample(all, length)

#create the password
password = "".join(temp)

#print the password
print(password)