def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b 

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b  # b不能等于0，这里面没有加判断


print("Let's do some math with just functions!") 
add1,add2 = map(int,input("请输入两个不为0的值：").split()) # map是python的内置函数，会对指定序列做映射。可以用来做类型转换。
sub1,sub2 = map(int,input("请输入两个不为0的值：").split())
mul1,mul2 = map(int,input("请输入两个不为0的值：").split())
div1,div2 = map(int,input("请输入两个不为0的值：").split())
age = add(add1, add2)
height = subtract(sub1, sub2)
weight = multiply(mul1, mul2)
iq = divide(div1, div2) 

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # age + (height-(iq/2*weight)) 

print("That becomes: ", what, "Can you do it by hand?") 