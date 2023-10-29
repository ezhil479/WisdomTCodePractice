# multiple inheritance
class A: # base class
    def class_a_method(self):
        print("I am class A method")
    def hello(self):
        print("hello from A")
class B: # base class
    def class_b_method(self):
        print("I am class B method")
    def hello(self):
        print("hello from B")
class C(A, B):      # derived class
    pass

instanceC = C()
instanceC.hello()   # based on MRO
help(instanceC)