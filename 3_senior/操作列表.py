'''
Author: sunshaochen 805960031@qq.com
Date: 2022-10-18 14:42:47
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-10-18 15:10:49
FilePath: \learn-python3-the-hard-way\3_senior\操作列表.py
Description: 
'''
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song","Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!             join函数 以指定字符连接字符串
print('#'.join(stuff[3:5]))  # super stellar!
