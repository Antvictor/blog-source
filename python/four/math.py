print(5/2) # 2.5
print(2+3) # 5
print(2-3) # -1
print(2*3) # 6
print(5//2) # 2
print(5%2) # 1
print(5**2) # 1


print("--------------")

print(5>2) # True
print(5<2) # False
print(5>=2) # True
print(5<=2) # False
print(5==2) # False
print(5!=2)# True


a = 5
b = 3
if (a > b):
    print(a)
else:
    print(b)


a = 5
b = 8
c = 12
if (a > b and b > c):
    print(b) # 没有输出

if (a+b>c or a >b):
    print(a) # 5