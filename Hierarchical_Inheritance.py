class Parent:
    def func1(self):
        print("function is in Parent class")
class Child1(Parent):
    def func2(self):
        print("function is in Child1 class")
class Child2(Parent):
    def func3(self):
        print("function is in Child2 class")
obj1=Child1()
obj2=Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
