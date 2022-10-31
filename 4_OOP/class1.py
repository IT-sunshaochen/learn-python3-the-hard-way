'''
Author: sunshaochen 805960031@qq.com
Date: 2022-10-18 15:21:23
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-10-30 14:43:29
FilePath: \learn-python3-the-hard-way\4_OOP\class1.py
Description: 
'''
# class Song(object):

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])

# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

# 类像特殊的模块
class Test(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def info(self):
        print(f"My nmae is {self.name}, Salary is {self.salary} ")
        

day_salary =  Test("Tom", 1000)

day_salary.info()

        
        