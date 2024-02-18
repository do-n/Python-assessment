# print(' This is my first class')
# print(' This is my first class')
# print(' This is my first class')

def my_function():
    text = 'This is my first class'
    print(text)
    print(text)
    print(text)
my_function()

def number_one():
    number = input('Enter your name')
    print(number)
number_one()

def number_two(text):
    print(text)
    print(text)
    print(text)
number_two('This is my first class')

def number_three(number):
    print(number)
number_three(888)

def name(firstname):
    print(firstname)
name('Don')
name('Caleb')


def student_name(firstname,lastname):
  print(firstname +' '+ lastname)
student_name('Don', 'Caleb')

def salutation(firstname):
    print(firstname +'GoodMorning')
salutation('Don')

def salutation(firstname,lastname):
    print(firstname + lastname + 'GoodMorning')

salutation('Esther', 'Mutwiri')
salutation('John', 'Doe')
salutation('Don', 'Marocho')


def school_age(firstname,age):
    if age<10:
        print(firstname + 'you are young')
    elif age>10:
        print(firstname + 'you are middle aged')
    else:
        print(firstname + 'you are older')
school_age('Esther', 9)
school_age('John', 14)
school_age('Don', 22)


def add_age(age):
     new_age = age + 18
     return new_age

print(add_age(20))


def subtract_age(age):
    new_age = age - 7
    return new_age


print(subtract_age(20))

def performance(english,math):
    total = english + math
    return total
print(performance('21', '22'))

def performance(*marks):
    total = sum(marks)
    return total
print(performance(22,45,656))
print(performance(434,45,6456,3466,233))
print(performance(222,4567,656,2344,4563,2567,))
print(performance(6578))

def country(nchi ='Kenya'):
    return nchi
print(country('Norway'))
print(country('China'))
print(country('Japan'))
print(country())
