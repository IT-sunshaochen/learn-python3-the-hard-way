# from fileinput import close
# from sys import argv 
# 
# script, filename = argv 
# 
# txt = open(filename) 
# 
# print(f"Here's your file {filename}:")
# print(txt.read()) 
# close()
# print("Type the filename again:")
# file_again = input("> ") 
# 
# txt_again = open(file_again) 
# 
# print(txt_again.read())

print("please input your file name")
file1 = input("> ")
file2 = open(file1,'r',encoding='UTF-8')
print(f"Here's your file {file1}:")
print(file2.read())
file2.close()


