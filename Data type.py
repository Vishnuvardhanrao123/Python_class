# Data types are:
# 1.number:
#         a:int
#         b:float
a=23
print("int",type(a))
a=23.56
print("float",type(a))
# 2.complex:
#    a+1j
b=20
print("complex",type(5+b))
# 3.string:
#   "abcd"
c="""vishnu"""
print(type(c),c)
# 4.bool:
#   True/False
a=10
b=20
print(type(a>=b))
# 5.rang:
#   (inistall,final)
for i in range(0,10):
    print(i)

# 6.list:
#    []
list1=[1,2,3,"vishnu",45.66,["yes","no",34]]
print(list1[5][1])
# 7.tuble:
# ()
# /*it is same as list but it is placed in ()/*
# 8.dict:
# {}
# it is object having key and value
dict1={'name':'vishnu',"age":23,
    'coures':{
    'fullstack1':'html',
    'fullstack2':'css',
    'fullstack3':'bootstrap',
    'fullstack4':'javascript'
    }
}
print(dict1['coures'][ 'fullstack1'])
# 9.set:
# {}
# it does not contain key and value but only contain finte elements
set1={1,2,3,4,5-6,-10,-11}
print(set1)

