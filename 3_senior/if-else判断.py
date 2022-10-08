'''
Author: sunshaochen 805960031@qq.com
Date: 2022-09-22 16:44:27
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-09-22 16:44:42
FilePath: \learn-python3-the-hard-way\3_senior\if-else判断.py
Description: 
'''
people = 30
cars = 40
trucks = 15 


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.") 

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.") 

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")