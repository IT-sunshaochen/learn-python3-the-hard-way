
from sys import argv 

script, user_name, id = argv
prompt = '# ' 

print(f" 姓名：{user_name}, 编号：{id},  你好，我是程序{script}.")
print("我想要问你几个问题")
print(f"Do you like me {user_name}?")
likes = input(prompt) 

print(f"Where do you live {user_name}?")
lives = input(prompt) 

print("What kind of computer do you have?")
computer = input(prompt) 

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice. 
""")

# first test