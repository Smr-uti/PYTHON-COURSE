print("Jai Ganesh")
In any application (Swiggy, Instagram, E-Commerce), multiple classes communicate with each other. To connect classes, we mainly use two relationships:

##  Topic 1: Aggregation — HAS-A Relationship

### 🔵 Definition
Aggregation is a type of class relationship where one class owns another class as a property. The object of one class is stored inside another class as an attribute.

- `Customer HAS-A Address` → Address is a property of Customer
- `Restaurant HAS-A Menu` → Menu belongs to Restaurant
- `Order HAS-A PaymentDetails` → Payment information is part of the Order
| 🧩 Aggregation — HAS-A | 🔗 Inheritance — IS-A |
|---|---|
| One class owns another class | One class extends another class |
| Customer HAS-A Address | SmartDevice IS-A Device |
| Object of class B stored inside class A | Child class gains parent's members |
| No parent-child relationship | Parent = Base/Super Class |
| Use: when objects are separate entities | Child = Derived/Sub Class |
| `class Customer: self.address = Address(...)` | `class SmartDevice(Device): ...` |
### Aggregation(Has-A relationship)
# example
class Customer:

  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address

  def print_address(self):
    print(self.address.city,self.address.pin,self.address.state)

  def edit_profile(self,new_name,new_city,new_pin,new_state):
    self.name = new_name
    self.address.edit_address(new_city,new_pin,new_state)

class Address:

  def __init__(self,city,pin,state):
      self.city = city
      self.pin = pin
      self.state = state

  def get_city(self):
    return self.city

  def edit_address(self,new_city,new_pin,new_state):
    self.city = new_city
    self.pin = new_pin
    self.state = new_state

add1 = Address('gurgaon',122011,'haryana')
cust = Customer('nitish','male',add1)

cust.print_address()

cust.edit_profile('ankit','mumbai',111111,'maharastra')
cust.print_address()

### Inheritance
## 📌 Topic 2: Inheritance — IS-A Relationship

### 🔵 Definition + DRY Principle

Inheritance is a relationship where a child class inherits the attributes and methods of a parent class — similar to how a child inherits qualities from parents.

**DRY = Don't Repeat Yourself!**



### 🔵 Inheritance Syntax

```python
class ChildClass(ParentClass):    # IS-A Relationship
```

### Example

```python
class AppUser:                     # Parent Class
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f'{self.username} logged in!')


class Learner(AppUser):            # Child — inherits AppUser
    def __init__(self, roll_num):
        self.roll_num = roll_num

    def enroll(self):
        print('Enrolled in course!')


# Child can access parent methods
s = Learner(101)
s.enroll()      # Own method
# s.login()     # Works if parent constructor was called
```

### Key Points

- Parent's **non-private attributes** are directly accessible in the child class.
- Parent's **non-private methods** can be called using the child object.
- **Inheritance is ONE-WAY** → Parent class cannot access child class data or methods.




# constructor example 2

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
#s.brand
#s.brand
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.price)
        print(self.brand) 
        print(self.camera )

class SmartPhone(Phone):
    # def __init__(self, price1, brand1, camera1):
    #     print ("Inside phone constructor")
    #     self.price1 = price1
    #     self.brand1 = brand1
    #     self.camera1 = camera1
    pass

s=SmartPhone(20000, "Apple", 13)
s.show()

# child can't access private members of the class

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.__price)

class SmartPhone(Phone):
    def check(self):
        #print(self.__price)
        print(self.brand)

s=SmartPhone(20000, "Apple", 13)
s.show()
s.check()
class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val):
        self.__val=val

    def get_val(self):
        return self.__val
        
son=Child(100)
#print("Parent: Num:",son.get_num())
print("Child: Val:",son.get_val())
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
obj.display2()
# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()
### Super Keyword
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent's buy method
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()
# can super access parent data?
# using super outside the class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent's  buy method
        super().buy()
        #print(super().brand)
        #print(self.brand)

s=SmartPhone(20000, "Apple", 13)
#s.brand
s.buy()
# super -> constuctor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print('Inside smartphone constructor')
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)
##### Inheritance in summary

- A class can inherit from another class.

- Inheritance improves code reuse

- Constructor, attributes, methods get inherited to the child class

- The parent has no access to the child class

- Private properties of parent are not accessible directly in child class

- Child class can override the attributes or methods. This is called method overriding

- super() is an inbuilt function which is used to invoke the parent class methods and constructor
class Parent:

    def __init__(self,num):
      self.__num=num

    def get_num(self):
      return self.__num

class Child(Parent):
  
    def __init__(self,num,val):
      super().__init__(num)
      self.__val=val

    def get_val(self):
      return self.__val
      
son=Child(100,200)
print(son.get_num())
print(son.get_val())
class Parent:
    def __init__(self):
        self.num=100

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var=200
        
    def show(self):
        print(self.num)
        print(self.var)

son=Child()
son.show()
class Parent:
    def __init__(self):
        self.__num=100

    def show(self):
        print("Parent:",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print("Child:",self.__var)

obj=Child()
obj.show()
# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

obj1=SmartPhone(1000,"Apple","13px")
obj1.buy()
# multilevel
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass


obj1=SmartPhone(1000,"Apple","13px")
obj1.buy()
obj2=FeaturePhone(10,"Lava","1px")
obj2.buy()
# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
