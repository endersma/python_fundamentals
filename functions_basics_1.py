#1
# def a():
#     return 5
# print(a())

# It will print 5

#2

# def a():
#     return 5
# print(a()+a())

# this will print 10

# #3

# def a():
#     return 5
#     return 10
# print(a())

# if this works like JavaScript, which I believe it does, the first return will negate the second return. Only 5 will be printed

# #4

# def a():
#     return 5
#     print(10)
# print(a())

# I believe that the same thing will happen here. The return will negate the print. Only 5 will be printed.

# #5

# def a():
#     print(5)
# x = a()
# print(x)

# This one presents an arguement and parameter. 5 will be printed

# #6

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# print((1+2) +)(2+3)) print(3=5) 8. This was wrong. The string type is wrong, so it generates an error.

# #7

# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# I think that since str() was used, this will just conatenate 2 and 5, so it will print 25

# #8

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# I want to say that this function will print 7 since it is last. No. It prints 100 and returns 10.

# #9

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# 7, 14, 21

# #10

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# 8

# #11

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# I think that the output will be 500, 300, 500, 500

#12

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# 500, 300, 500, 500

# #13

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# 500, 300, 500, 300

# #14

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# :( hmmmm 1 ,3 2? I don't get this. Oh. Now I do. When a() is called it prints 1, calls b() 3, and prints 2

# #15

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# 1, 3, 5, 10