# def volume(r):
#     print((4/3)*3.14*r**3)

# volume(10) 
# volume(20)
# volume(30) 
# #####################################

# def cal(a,b):
#     if b==0:
#        print("error,b should be greather value")
#        return
    
#     print("sum",a+b)
#     print("sub",a-b)
#     print("mul",a*b)
#     print("div",a/b)

# c=0
# cal(10,c)

#############################################
# def cal(a,b):
#     if b==0:
#         return "zero not aceppted"
#     return a/b

# str=cal(10,2)
# print(str)

# ##################################
#//recursion//
# def fact(n):
#     if n==1:
#         return 1
#     print(n)
#     return n*fact(n-1)

# res=fact(5)
# print(res)
# ################################
# def num(n):
   
#    if n<=0:
#       return 
#    num(n-1)
#    print(n)

# num(10)
###############################
##mult##

# def numb(a,b):
    
#     if b==0:
#         return 0
#     elif b == 1:
#         return a   
#     else:
#         return a+numb(a,b-1)
    
# mult=numb(5,3) 
# print(mult)
#################################
# //fabicani//
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2) 

# res=fib(4)
# print(res)
######################################
# list=[1,2,3,4,5]
# target=6
# for i in range(0,len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i]+list[j]==target:
#           print(list[i],list[j])  
##########################  
# list=[1,2,3,4,5]
# for i in list:
#     target=6
#     for j in list:
#         if i+j==target and i != j:
#           print(i,j) 
###################################################
#arbidary arguments
# def sum(a,b,**c):
#   return c

# print(sum(2,3,d=5,e=6,f=7,g=8))  
################################################
##scopes########
# globals()['a']=27 
# a=10  #global scope
# # globals()['a']=27 
# def add():
#   globals()['a']=27 
#   a=14 #local scope
#   print(a) //14
#   # globals()['a']=27
# add() 
# print("this is",a) #27

##############################
##lambda functions
# lamb_func=lambda x :x*x
# print(lamb_func(5))
##one way///////////////////////////////////
# def squt(x):
#   return x*x
# list1=[1,5,6,7,8]  
# print(list(map(squt,list1)))
#two way/////////////////////////////////////////
# from functools import reduce
# list1=[1,5,6,7,8]  
# print(list(map(lambda x:x*x,list1)))
# print(list(filter(lambda x:x%2==0,list1)))
# print(reduce(lambda x,y:x-y,list1))
# ###############################################
#Decorators//////////////////
def func_decorator(func):
  
  def wrapper():
    print("check ther a man")
    print("working")
    func()
    print("thankyou")
  return wrapper

@func_decorator
def printer():
  print("printing.............")
printer()  