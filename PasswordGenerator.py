import random
import string
from random import randint


#currently a work in progress, but functional to some degree

text_file = open('usa.txt', 'r')
file_content = text_file.read()
content_list = file_content.split('\n')



#user inputs length of password they would like
length = int(input('\nPassword length: '))

#variables
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

#randomizing the characters
#temp = random.sample(all, length)

#create the password
#password = "".join(temp)

#print the password
#print(password)

random3 = randint(1, 3)
random2 = randint(1, 2)
number_of_numbers = random2
number_of_words = random3
randomnumbers = random.choices(num, k=number_of_numbers)
randompuncutation = random.choices(symbols, k=number_of_numbers)
temp2 = ''.join(randompuncutation) + ''.join(randomnumbers)
temp3 = ''.join(random.sample(temp2, len(temp2)))

content_list_sorted = sorted(content_list, key=len)

oneletterword = []
twoletterword = []
threeletterword = []
fourletterword = []
fiveletterword = []
sixletterword = []
sevenletterword = []
eightletterword = []
nineletterword = []
tenletterword = []
elevenlettewrord = []
twelveletterword = []
thirteenletterword = []

for i in content_list_sorted:
    if len(i) == 1:
        oneletterword.append(i)
    elif len(i) == 2:
        twoletterword.append(i)
    elif len(i) == 3:
        threeletterword.append(i)
    elif len(i) == 4:
        fourletterword.append(i)
    elif len(i) == 5:
        fiveletterword.append(i)
    elif len(i) == 6:
        sixletterword.append(i)
    elif len(i) == 7:
        sevenletterword.append(i)
    elif len(i) == 8:
        eightletterword.append(i)
    elif len(i) == 9:
        nineletterword.append(i)
    elif len(i) == 10:
        tenletterword.append(i)
    elif len(i) == 11:
        elevenlettewrord.append(i)
    elif len(i) == 12:
        twelveletterword.append(i)
    elif len(i) == 13:
        thirteenletterword.append(i)
    else:
        pass


number_of_characters = length - len(temp3)

if number_of_characters == 1:
    password = random.choice(oneletterword) + temp3
elif number_of_characters == 2:
    password = random.choice(twoletterword) + temp3
elif number_of_characters == 3:
    password = random.choice(threeletterword) + temp3
elif number_of_characters == 4:
    password = random.choice(fourletterword) + temp3
elif number_of_characters == 5:
    password = random.choice(fiveletterword) + temp3
elif number_of_characters == 6:
    password = random.choice(sixletterword) + temp3
elif number_of_characters == 7:
    password = random.choice(sevenletterword) + temp3
elif number_of_characters == 8:
    password = random.choice(eightletterword) + temp3
elif number_of_characters == 9:
    passcombo = randint(1, 3)
    if passcombo == 1:
        password = random.choice(nineletterword) + temp3
    elif passcombo == 2:
        password = random.choice(fourletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 3:
        password = random.choice(fiveletterword) + random.choice(fourletterword) + temp3
elif number_of_characters == 10:
    passcombo = randint(1, 4)
    if passcombo == 1:
        password = random.choice(tenletterword) + temp3
    elif passcombo == 2:
        password = random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 3:
        password = random.choice(sixletterword) + random.choice(fourletterword) + temp3
    elif passcombo == 4:
        password = random.choice(fourletterword) + random.choice(sixletterword) + temp3
elif number_of_characters == 11:
    passcombo = randint(1,8)
    if passcombo == 1:
        password = random.choice(elevenlettewrord) + temp3
    elif passcombo == 2:
        password = random.choice(sixletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 3:
        password = random.choice(fiveletterword) + random.choice(sixletterword) + temp3
    elif passcombo == 4:
        password = random.choice(sevenletterword) + random.choice(fourletterword) + temp3
    elif passcombo == 5:
        password = random.choice(fourletterword) + random.choice(fiveletterword) \
                   + random.choice(twoletterword) + temp3
    elif passcombo == 6:
        password = random.choice(fiveletterword) + random.choice(fourletterword) \
                   + random.choice(twoletterword) + temp3
    elif passcombo == 7:
        password = random.choice(sixletterword) + random.choice(threeletterword) \
                   + random.choice(threeletterword) + temp3
    elif passcombo == 8:
        password = random.choice(sixletterword) + random.choice(threeletterword) \
                   + random.choice(threeletterword) + temp3
elif number_of_characters == 12:
    passcombo = randint(1, 10)
    if passcombo == 1:
        password = random.choice(twelveletterword) + temp3
    elif passcombo == 2:
        password = random.choice(sixletterword) + random.choice(sixletterword) + temp3
    elif passcombo == 3:
        password = random.choice(sevenletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 4:
        password = random.choice(fiveletterword) + random.choice(sevenletterword) + temp3
    elif passcombo == 5:
        password = random.choice(eightletterword) + random.choice(fourletterword) + temp3
    elif passcombo == 6:
        password = random.choice(fourletterword) + random.choice(eightletterword) + temp3
    elif passcombo == 7:
        password = random.choice(threeletterword) + random.choice(threeletterword) \
                   + random.choice(sixletterword) + temp3
    elif passcombo == 8:
        password = random.choice(threeletterword) + random.choice(sixletterword) \
                                 + random.choice(threeletterword) + temp3
    elif passcombo == 9:
        password = random.choice(sixletterword) + random.choice(threeletterword) \
                   + random.choice(threeletterword) + temp3
    elif passcombo == 10:
        password = random.choice(fourletterword) + random.choice(fourletterword) \
                   + random.choice(fourletterword) + temp3
elif number_of_characters == 13:
    passcombo = randint(1, 12)
    if passcombo == 1:
        password = random.choice(thirteenletterword) + temp3
    elif passcombo == 2:
        password = random.choice(sevenletterword) + random.choice(sixletterword) + temp3
    elif passcombo == 3:
        password = random.choice(sixletterword) + random.choice(sevenletterword) + temp3
    else:
        password = random.choice(eightletterword) + random.choice(fiveletterword) + temp3
elif number_of_characters == 14:
    passcombo = randint(1, 15)
    if passcombo == 1:
        password = random.choice(fourletterword) + random.choice(tenletterword) + temp3
    elif passcombo == 2:
        password = random.choice(fiveletterword) + random.choice(nineletterword) + temp3
    elif passcombo == 3:
        password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
    elif passcombo == 4:
        password = random.choice(sevenletterword) + random.choice(sevenletterword) + temp3
    elif passcombo == 5:
        password = random.choice(eightletterword) + random.choice(sixletterword) + temp3
    elif passcombo == 6:
        password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
    else:
        password = random.choice(tenletterword) + random.choice(fourletterword) + temp3
else:
    password = 'sorry we currently do not support that many characters at the moment'

print(password)






