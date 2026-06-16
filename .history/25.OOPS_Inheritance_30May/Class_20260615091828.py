class A:
    def __init__(self):
        self.var1=100

    def edit_var1(self,var2):
        self.var1= var2  

    def display1(self,var1):
        print("class A :", self.var1)

class B(A):
  
    def display2(self):
        print("class B :", self.var1)

obj=B()
#obj.display1(200)
obj.edit_var1(200)