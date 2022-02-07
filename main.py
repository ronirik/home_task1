# print('Hello' + 'World!')
# print('Hello world\n' + '5')
# print('Hello world')
# print("I'm 25 years old")
# print('I\'m 25 years\' old')
# print('John'[0])
# print('John'[2])
#print('John'[-2])
#print('John'[2:2])
#print('John'[:6])
#print('John'[6:])
#print('John'[:])
#print('John'[::-1])
#print('John'[::2])
# new_s = s[::-1] konsol
# string[start:stop:step]


#print(len('Hello? John')) #dlina stroki 11
# some_str = "Hello world"
# print(len(some_str))

# name = input('Enter your name ')
# surname = input('Enter suername')
# year_of_birth = int(input('Enter your year'))
# #message = ' Hello ' + name + 'sa ' + suername + 'you are ' + year_of_birth + ' good ' + ((2021 - year_of_birth))

# message_with_format = f'Hello {name},  {surname}, you are {2021-year_of_birth}'
# print(message_with_format)



# age = int(input('Your age '))
# if age >= 18 and age < 50:
#     print('Good')
# else:
#     print('Goodbai')


# some_str = 'Hello, world'
# # print(some_str[0])
# # print(some_str[1])
# # print(some_str[2])
# # print(some_str[3])
# for i in some_str:
#     print(i)

# import math
# print(math.pi)
# print(math.factorial(6))


# qwer = "The quick brown fox jumps over the lazy dog"
# tr = "*"
# for i in qwer:
#    if qwer == 'o':
#       tr = '*'
#       tr = qwer
# print(qwer)



# string = 'The quick brown fox jumps over the lazy dog'  
# new_character = '*' 
# # position = 'o'
# for i in string:
#     temp = list('o') 
#     temp[string] = new_character 
#     string = "".join(temp) 
# print(string)

# print('The quick brown fox jumps over the lazy dog'\
#     .replace('o', '*'))

# num = input('login ')
# import random
# import string
# pas = ''
# for x in range(8): 
#     pas = pas + .join(string.ascii_letters((random.choice(list('1234567890abcdefghigPQRSTUVYXWZ!@#$%^&*()_+')))) 
# print('your pass: ', pas)

# def random_id(length):
#     number = '0123456789'
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     id = ''
#     for i in range(0,length,2):
#         id += random.choice(number)
#         id += random.choice(alpha)
#     return id
# print(id)

# import random, string

# def randomword(length):
#    letters = string.ascii_lowercase
#    return ''.join(random.choice(letters) for i in range(length))
# print(randomword)


# import random
# import string

# def get_random_password():
#     random_source = string.ascii_letters + string.digits + string.punctuation
#     password = random.choice(string.ascii_lowercase)

#     for i in range(6):
#         password += random.choice(random_source)

#     password_list = list(password)
 
#     random.SystemRandom().shuffle(password_list)
#     password = ''.join(password_list)
#     return password

# print("First Random Password is ", get_random_password())
# # output  qX49}]Ru!(
# print("Second Random Password is ", get_random_password())
# # Output  3nI0.V#[T

# list_1 = [('America'),('Japan')]

# for item in list_1
# create tuple of (item[0], item[1].split('.')[1], item[2])
# append to a new list
# list_2 = [(f"{item[0]}{item[1].split('.')[1]}", f"{item[2]}") for item in list_1]

# print(list_2)


d = 'Roman'
print(d[-2:])