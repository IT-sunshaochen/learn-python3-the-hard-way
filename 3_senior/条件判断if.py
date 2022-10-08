'''
Author: sunshaochen 805960031@qq.com
Date: 2022-09-22 16:36:45
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-09-22 16:39:03
FilePath: \learn-python3-the-hard-way\3_senior\条件判断if.py
Description: 
'''
people = 20
cats = 30
dogs = 15 


if people < cats:          # 本质就是数值比较。
    print("Too many cats! The world is doomed!") 

if people > cats:
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