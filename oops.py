
class Humanbeing:
    totalcount=0
    def __init__(self,name1,age1,address):
        self.name=name1
        self.age=age1
        self.address1=address
        Humanbeing.totalcount += 1
        print(self.name,"Human being is created")
    @classmethod
    def totalcountreset(cls):
        cls.totalcount=0
        print(cls.totalcount)
    def speak(self):
        print("i am speaking")

    def walk(self):
        print("i am walking")

human1=Humanbeing("rahul","10","knr")
human2=Humanbeing("rah","10","knr")  

# # print(human1.age)
# human1.id=45
# print(Humanbeing.totalcount)   
# Humanbeing.totalcountreset()
# print(human1.id)
# ###################################################
class student(Humanbeing):
    def __init__(self,name1,age1,address):
        super().__init__(name1,age1,address)
        print("this is student")

student1=student("vishnu",20,"ece")
student1.speak()
print(vars(student1))