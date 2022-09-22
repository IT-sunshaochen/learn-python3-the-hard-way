'''
Author: sunshaochen 805960031@qq.com
Date: 2022-09-20 15:33:42
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-09-20 17:01:21
FilePath: \learn-python3-the-hard-way\3_senior\exercise26.py
Description: 
'''
from encodings import utf_8
from sys import argv

script, filename = argv 

txt = open(filename,encoding= "utf_8")

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again,encoding="utf_8")

print(txt_again.read())


prompt = '#'
print("How old are you?", end=' ')
age = input(prompt)
print("How tall are you?", end=' ')
height = input(prompt)
print("How much do you weigh?", end=' ')
weight = input(prompt)

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) #.format 格式化输出 与{}配合使用。 %s % xxx
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #format(*x,*xx) 分别是元组和字典传参。




people = 20
cates = 30
dogs = 15
cats = 50

if people < cats:
    print ("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

