


'''                             
===================================
        Python Django
    Interview Preparation
===================================                             


Prepared by Muhammad Nouman (In Roman Urdu Language)
Date: [22/january/2026]
Version: 1.0


1.Introduction to Python and Django

what is Python?:
i).High-level programming language, easy syntax,
   used for web, data science, AI.
    
    Example:
        print("Hello World").

2.how many data type in python?
  python may kafi data type hain,
  jin may se kuch important data
  type hain jin ko hum mukhtalif
  categories may divide kar saktay hain:
    like
    
    i).Numeric data types:
        -int: integer numbers, like 1, 2, 3.                           
        -float: decimal numbers, like 1.2, 3.12,
        -complex: complex numbers, like 2+3j.
          interview Answer:
          Numeric data types wo hotay hain jin mein
          numbers store kiye jate hain,
          aur Python mein built-in numeric
          data types int, float aur complex hain.
   ii).Sequence data types:
         -list: ordered, mutable collection, like [1,2,3].
         -tuple: ordered, immutable collection, like (1,2,3).
         -range: sequence of numbers, like range(1,10).
            interview Answer:
            Sequence data types wo hotay
            hain jin mein data
            ordered hota hai aur index ke
            zariye access kiya jata hai.

  iii).Text data type:
        -Strring: sequence of characters, like "Hello".
   iv).Set data type:
        -set: unordered, mutable collection of unique items, like {1,2,3}.
         interview Answer: 
         Set data type wo hota hai jo unordered aur mutable
         collection of unique items ko store karta hai,
         aur Python mein built-in set data type set hai.
    v).Mapping data type:
        -dectionary: key-value pairs, like {'a':1,'b':2}.
        interview Answer: 
         Mapping data type wo hota hai
         jo key–value pairs mein data store karta hai,
         aur Python mein built-in mapping data type dictionary hai.
   vi).Boolean data type:
        -bool: True or False values.
          interview Answer:
          Boolean data type wo hota hai
          jo sirf do values ko represent
          karta hai: True aur False,
          aur Python mein built-in boolean data type bool hai.

  vii).Binary data types:
        -bytes: immutable sequence of bytes, like b'hello'.
        -bytearray: mutable sequence of bytes, like bytearray(b'hello').
        -memoryview: memory view object, like memoryview(b'hello').
         interview Answer:
          Binary data types wo hotay hain
          jo binary data ko represent karte hain,
           aur Python mein built-in binary data
           types bytes, bytearray hain.         
            memoryview ek object hai jo binary data
            ko bina copy banaye access karta hai,
            is se performance aur memory efficient hoti hai.    

  viii. Big picture (complete data types recap)
        -Numeric → int, float, complex
        -Sequence → list, tuple, string, range
        -Set → set
        -Mapping → dict
        -Boolean → True / False
        -Binary → bytes, bytearray
          concise way to create lists.
          Example:
          [x for x in range(10) if x % 2 == 0]
    ix. what is deffrence betwwen indexing and slicing?
       Indexing se hum sequence me sirf ek element access
       karte hain, jab ke slicing se hum ek range select karke
       naya sequence return karte hain.


Example:
'''
# Numeric data types
a = 10          # int
b = 3.14       # float
c = 2 + 3j     # complex
# Sequence data types
my_list = [1, 2, 3]          # list
my_tuple = (1, 2, 3)         # tuple
my_range = range(1, 10)      # range
# Text data type
my_string = "Hello, World!"  # string
# Set data type
my_set = {1, 2, 3}           # set
# Mapping data type
my_dict = {'a': 1, 'b': 2}   # dictionary
# Boolean data type
is_true = True                # bool
is_false = False              # bool
# Binary data types
my_bytes = b'hello'          # bytes
my_bytearray = bytearray(b'hello')  # bytearray
my_memoryview = memoryview(b'hello') # memoryview
'''
2.  what is mutable and immutable data types in python?
      i. Mutable data types wo hote hain
         jin ki values ko change kiya ja sakta hai
     ii. Immutable data types wo hote hain
         jin ki values ko change nahi kiya ja sakta.
        Example of Mutable data types:
'''
# Mutable data types
my_list = [1, 2, 3]
my_list[0] = 10  # Changing the first element
print(my_list)   # Output: [10, 2, 3]
my_dict = {'a': 1, 'b': 2}
my_dict['a'] = 10  # Changing the value for key 'a'
print(my_dict)     # Output: {'a': 10, 'b': 2}
my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to the set
print(my_set)  # Output: {1, 2, 3, 4}
'''
Example of Immutable data types:
'''
# Immutable data types
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error
print(my_tuple)  # Output: (1, 2, 3)
my_string = "Hello"
# my_string[0] = "h"  # This will raise an error
print(my_string)  # Output: Hello
my_int = 10
# my_int[0] = 20  # This will raise an error
print(my_int)  # Output: 10
'''
3.  what is type casting in python?
    Type casting aik process hai jisme hum aik data 
    type ko dusre data type me convert karte hain.
    Python me type casting do tarah se hoti hai: implicit aur explicit

    i).Implicit Type Casting:
        Implicit type casting me Python
        automatically aik data type ko
        dusre data type me convert kar deta hai
        jab zarurat hoti hai.
        Example:
'''# Implicit Type Casting
a = 10        # int
b = 3.14      # float
c = a + b    # int + float = float
print(c)     # Output: 13.14
print(type(c))  # Output: <class 'float'>
'''
    ii).Explicit Type Casting:
        Explicit type casting me hum
        manually aik data type ko
        dusre data type me convert karte hain
        using built-in functions jaise int(), float(), str(), etc.
        Example of Implicit Type Casting:
'''
# Explicit Type Casting
a = 10        # int
b = float(a)  # int to float
print(b)      # Output: 10.0
print(type(b))  # Output: <class 'float'>
c = str(a)    # int to string
print(c)      # Output: '10'
print(type(c))  # Output: <class 'str'>
'''
4. what is python functions?
    i). Function aik reusable block of code 
        hai jo specific task perform karta hai.
   ii). Function ko define karne ke liye
        def keyword use hota hai.
  iii). Function ko call karne ke liye 
        function name ke sath parentheses use hoti hain.
    Example:
'''
def mera_function(name):
    print(f"Hello, {name}!")    
mera_function("Nouman")  # Output: Hello, Nouman!
'''
5. what is lambda function in python?
    i). Lambda function aik anonymous
        function hai jo single expression ko evaluate karta hai.
    ii). Lambda function ko define karne
         ke liye lambda keyword use hota hai.
    iii). Lambda function ko call karne ke liye
          function name ke sath parentheses use hoti hain.

        interview Answer:
            Lambda function ek anonymous,
            single-line function hai jo temporary
            use ke liye short tasks perform karta hai
            aur automatically expression return karta hai  
    Example:
'''
# Lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25
'''
6. what is difference between list
   and tuple in python?
     
     List aur Tuple dono sequence data types
     hain jo multiple values ko store karte hain.
    
     Lekin in dono me kuch differences hain:
    1. Mutability:
            - List mutable hoti hai,
              yani iski values ko change kiya ja sakta hai.
            - Tuple immutable hoti hai,
              yani iski values ko change nahi kiya ja sakta.
    2. Syntax:
            - List ko square brackets []
              me define kiya jata hai.
            - Tuple ko parentheses () 
              me define kiya jata hai.
    3. Performance:
            - Tuple list se thodi fast hoti hai
              kyun ke ye immutable hoti hai.
    4. Use Cases:
            - List ko jab values ko change karna
              ho tab use kiya jata hai.
            - Tuple ko jab values ko change nahi
              karna ho tab use kiya jata hai.
    Example:
'''
# List example
my_list = [1, 2, 3]
my_list[0] = 10  # Changing the first element
print(my_list)   # Output: [10, 2, 3]
# Tuple example
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error
print(my_tuple)  # Output: (1, 2, 3)
'''
7. what is difference between deep 
   copy and shallow copy in python?
   
    -Deep Copy aur Shallow Copy dono objects ki copies banate hain,
      lekin in dono me kuch differences hain:
    1. Shallow Copy:
        - Shallow Copy ek naya object banata hai
           jo original object ke references ko point karta hai.
        - Agar original object ke andar koi mutable 
           object hai aur usko change kiya jata hai,
            to shallow copy me bhi wo change reflect hota hai.
    2. Deep Copy:
            - Deep Copy ek naya object banata hai
                jo original object ke tamam nested objects ki
                bhi copies banata hai.
            - Agar original object ke andar koi mutable object hai
                aur usko change kiya jata hai,
                to deep copy me wo change reflect nahi hota.
    Example:
'''
import copy
# Original list with nested list
original_list = [1, 2, [3, 4]]
# Shallow Copy
shallow_copied_list = copy.copy(original_list)
# Deep Copy
deep_copied_list = copy.deepcopy(original_list)
# Modifying the nested list in original list
original_list[2][0] = 30
print("Original List:", original_list)           # Output: [1, 2, [30, 4]
print("Shallow Copied List:", shallow_copied_list)  # Output: [1, 2, [30, 4]
print("Deep Copied List:", deep_copied_list)      # Output: [1, 2, [3, 4]
'''


 8. What is iteration?
        Iteration ek process hota hai jo ek
         iterable object ko iterate karta hai.
          Iteration ko iterate karte waqt,
           iteration ek next element return karta hai.
        
    usecases of iteration?
        - Looping through data structures (list, tuple, dictionary, set)
        - Data processing
        - Generating sequences
        - Implementing algorithms
    Example:
'''
def mera_apna_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break
# list, range, tuple are iterable objects
a = [1, 2, 3, 4, 5]
b = range(1, 10)
c = (1, 2, 3, 4, 5)
d= {'a':1,'b':2,'c':3}
e = {1,2,3,4,5}
mera_apna_for_loop(a)
mera_apna_for_loop(b)
mera_apna_for_loop(c)
mera_apna_for_loop(d)
mera_apna_for_loop(e)   
'''
    output:
    1
    2
    3
    4       
    5
    1                       
    .
    .
    .

9.what is iterator?

     Iterator wo object hai jo next()
     function ke through items ko ek-ek
     karke return karta hai.
     Iterator state maintain karta hai
     jisse pata hota hai kaunsa item last return hua.
     usecases of iterator?
        - Looping through data structures (list, tuple, dictionary, set)
        - Data processing
        - Generating sequences
        - Implementing algorithms
Example:
'''
def mera_apna_iterator(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break
# list, range, tuple are iterable objects
a = [1, 2, 3, 4, 5] 
b = range(1, 10)
c = (1, 2, 3, 4, 5)
d= {'a':1,'b':2,'c':3}
e = {1,2,3,4,5}
mera_apna_iterator(a)
mera_apna_iterator(b)
mera_apna_iterator(c)
mera_apna_iterator(d)
mera_apna_iterator(e)
''' 

10.what is iterable?
     Iterable ek object hota hai jisko hum
     loop ke zariye iterate kar sakte hain
     usecases of iterable?
        - Looping through data structures (list, tuple, dictionary, set)
        - Data processing
        - Generating sequences
        - Implementing algorithms
    Example:
    '''
def mera_apna_iterable(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break           
# list, range, tuple are iterable objects
a = [1, 2, 3, 4, 5]
b = range(1, 10)
c = (1, 2, 3, 4, 5)
d= {'a':1,'b':2,'c':3}
e = {1,2,3,4,5}
mera_apna_iterable(a)
mera_apna_iterable(b)
mera_apna_iterable(c)
mera_apna_iterable(d)
mera_apna_iterable(e)

''' 

11.Difference between iterable and iterator?
   i.Iterable:
     - Iterable ek aisa object hota hai
       jisko hum loop ke zariye iterate kar sakte hain.
     - Iterable objects me list,
       tuple, string, dictionary, set, range shamil hain.
     - Iterable object me __iter__() method hota hai jo iterator return
            karta hai.
            example:
 ...
'''
my_list = [1, 2, 3]
iterator = iter(my_list)  # my_list is iterable
print(next(iterator))  # prints 1
print(next(iterator))  # prints 2
print(next(iterator))  # prints 3
print(next(iterator))  # raises StopIteration
'''

   ii.Iterator:
      - Iterator ek aisa object hota hai jo
        iterable objects ko iterate karta hai.
      - Iterator object me next() method
        hota hai jo next element return karta hai.
      - Iterator object me __iter__()
        method hota hai jo khud ko return karta hai.        
'''
my_list = [1, 2, 3]
iterator = iter(my_list)  # my_list is iterable
print(next(iterator))  # prints 1
print(next(iterator))  # prints 2
print(next(iterator))  # prints 3     
'''
12.what is generator?
      Generator ek function hai jo yield keyword use
      krte hain or value ko one by one return krte hain
        usecases of generator?
            - Large data sets ko handle krne k liye
            - Memory efficient programming k liye
            - Infinite sequences ko create krne k liye      

        Example:
'''
def mera_generator():
    yield 1
    yield 2
    yield 3
gen = mera_generator()
print(next(gen))  # prints 1
print(next(gen))  # prints 2
print(next(gen))  # prints 3
print(next(gen))  # raises StopIteration 

'''
    i. Difference between generator and iterator?
        a).Generator:
            - Generator ek special type ka iterator hota hai
                jo function ke zariye create hota hai.
            - Generator function me yield keyword use hota hai
                jo value ko one by one return karta hai.
            - Generator function state ko maintain karta hai,
                jisse next value return karne ke liye function
                wapas se call karne ki zarurat nahi hoti.
            - Memory efficient hota hai kyun ke ye saari
                values ek sath memory me store nahi karta.
   Example:
'''
def mera_generator():
    yield 1
    yield 2
    yield 3
gen = mera_generator()
print(next(gen))  # prints 1
print(next(gen))  # prints 2
print(next(gen))  # prints 3
print(next(gen))  # raises StopIteration
'''
        b).Iterator:
            - Iterator ek object hota hai jo iterable objects ko iterate karta hai.
            - Iterator object me next() method hota hai jo next element return karta hai.
            - Iterator object me __iter__() method hota hai jo khud ko return karta hai.
    Example:
'''
my_list = [1, 2, 3] 
iterator = iter(my_list)  # my_list is iterable
print(next(iterator))  # prints 1
print(next(iterator))  # prints 2
print(next(iterator))  # prints 3
'''

13.what is decorator?
      Decorator ek function hota hai jo dusre 
      function ki functionality ko bina change
      kiye enhance karta hai.
        decorators Python me bohot commonly
        use hote hain, especially Django me.
        usecases of decorator?
                - Logging
                - Authentication
                - Caching
                - Input validation  
        Example:
'''
def mera_decorator(func):
    def wrapper():
        print("Function call hone wala hai")
        func()
        print("Function call ho chuka hai")
    return wrapper
@mera_decorator
def mera_function():
    print("Hello World")
mera_function() 
'''
Output:
Function call hone wala hai
Hello World
Function call ho chuka hai
'''
'''
14. What is OOP?
      OOP (Object-Oriented Programming)
       ek programming paradigm hai jo
        real-world entities ko objects
         aur classes ki form mein represent karta hai.
    example:
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")        
'''
i. What are the main pillars of OOP?
    OOP ke 4 pillars hain:
      i. Encapsulation,
     ii. Inheritance,
    iii. Polymorphism,
     iv. Abstraction.
    

    i).what is Encapsulation
        Encapsulation ka matlab hai data aur 
        methods ko aik class me band karna 
        aur data ko direct access se protect karna.
        encapsulation se data security aur integrity ensure hoti hai.
  ii). what is getter and setter?
        getter aur setter methods encapsulation ka part hain.                                       
            why using getters and setters?.
                Getter aur Setter methods, encapsulation me private data
                ko access aur modify karne ke liye use hote hain.
                    i). Getter private variable ki value read / get karne ke liye hota hai
                    ii). Setter private variable ki value update / change karne ke liye hota hai
            Example:
'''
class EmployeeEncapsulation:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Salary update ho gayi: {self.__salary}")
        else:
            print("Invalid amount!")

emp1 = EmployeeEncapsulation("Ali", 50000)
print(emp1.get_salary())
emp1.set_salary(60000)

'''
ii) what is Inheritance?
     Inheritance aik OOP concept hai jisme child class,
     parent class ki properties
     aur methods ko inherit karti hai.
     Inheritance code reusability aur
     maintainability improve karta hai.
        types of Inheritance:
            - Single Inheritance
            - Multi-level Inheritance
            - Multiple Inheritance

        i.what is single Inheritance?:
            Single Inheritance me aik child
            class sirf aik hi parent class se
            inherit karti hai.
            Yeh sab se simple aur commonly used
            inheritance type hai.
            example:'''
class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")
child = Child()
child.parent_method()  # Parent method
child.child_method()   # Child method
'''
       ii.what is multi-level Inheritance?:
            Multi-level Inheritance me aik child class
            parent class se inherit karti hai,
            or parent grand parent class se inherit karti hai.
            Is me inheritance ka ek chain banta hai.
        Example:
'''
class GrandParent:
    def grandparent_method(self):
        print("GrandParent method")
class ParentMultiLevel(GrandParent):
    def parent_method(self):
        print("Parent method")
class ChildMultiLevel(ParentMultiLevel):
    def child_method(self):
        print("Child method")
child = ChildMultiLevel()
child.grandparent_method()  # GrandParent method
child.parent_method()       # Parent method
child.child_method()        # Child method
'''
    iii.what is multiple Inheritance?:
        Multiple Inheritance me aik child class ek
        se zyada parent classes se inherit karti hai.
        Is me child class multiple classes ki properties 
        aur methods use kar sakti hai.
    Example:
                '''
class ParentOne:
    def method_one(self):
        print("Method from Parent One")
class ParentTwo:
    def method_two(self):
        print("Method from Parent Two")
class ChildMultiple(ParentOne, ParentTwo):
    def child_method(self):
        print("Child method")
child = ChildMultiple()         
child.method_one()  # Method from Parent One
child.method_two()  # Method from Parent Two
child.child_method()  # Child method    

'''
iii) what is  Polymorphism?
      Polymorphism aik OOP concept hai jisme same method ya 
      function different data types ya objects ke
      liye different behavior provide karta hai.       
     Same method name, lekin different behavior.
        types of Polymorphism:
            - Method Overloading
            - Method Overriding
        i) what is Method Overloading?
            Method Overloading same class me same methods ko
            deffrent parameter k lia use krna  versions hote hain
            jo different parameters accept karte hain.
            Python me method overloading directly support nahi hoti,
            lekin hum default arguments ya *args, **kwargs ka use karke achieve kar sakte hain.
            Example:
'''
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
calc = Calculator()
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9
'''
iv) what is Method Overriding?
    Method Overriding me child class parent class ke method ko redefine karke
    apna behavior implement karti hai.
    Example:


'''class ParentClass:
    def show(self):
        print("Parent class method")
class ChildClass(ParentClass):
    def show(self):
        print("Child class method")
child = ChildClass()
child.show()  # Child class method
'''
Output:
Child class method

iv) what is Abstraction?
    Abstraction aik OOP concept hai 
    jisme complex implementation details
    ko hide karke sirf essential features ko
    expose kiya jata hai.
    yani Sirf important cheezain dikhana aur
    implementation details hide karna.
    Example:
                    '''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class CarVehicle(Vehicle):
    def start(self):
        print("Car start ho rahi hai")

class Bike(Vehicle):
    def start(self):
        print("Bike start ho rahi hai")

car = CarVehicle()
bike = Bike()

car.start()
bike.start()
'''
what is *args and **kwargs in python?
    *args aur **kwargs dono
    function arguments ko handle karne ke liye use hote hain.
     i.Jab hum function bana rahe ho aur humein
       pehle se nahi pata kitne arguments pass honge,
       tab *args ka use karte hain.
       Ye tuple ke form mein values ko receive karta hai.
    Example of *args:
'''
def mera_function(*args):
    for arg in args:
        print(arg)
mera_function(1, 2, 3, 4, 5)
'''
Output:
1
2
3
4
5
    ii.Jab hum function bana rahe ho aur humein
       pehle se nahi pata kitne keyword arguments
       pass honge, tab **kwargs ka use karte hain.
       Ye dictionary ke form mein values ko receive karta hai.
    Example of **kwargs:
'''
def mera_function_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
mera_function_kwargs(a=1, b=2, c=3)
'''
Output:
a: 1
b: 2
c: 3



14. what is synchronous and asynchronous programming in python?
     i).Synchronous Programming:
        Synchronous programming may code
        line by line  execute hota hain,
        yani ek task complete hone ke baad
        hi dusra task start hota hai.
        Isme program ka flow linear hota hai.
         Key Points:
            Blocking hota hai (wait karta hai)
            Simple aur easy to understand
            Slow ho sakta hai jab I/O tasks (API, database, file, network) hoon
    Example:
'''
import time
def task1():
    print("Task 1 start")
    time.sleep(2)
    print("Task 1 done")
def task2():
    print("Task 2 start")
    time.sleep(1)
    print("Task 2 done")
task1()
task2()
'''
Output:
Task 1 start
Task 1 done
Task 2 start
Task 2 done

     ii).Asynchronous Programming:
          Asynchronous programming me multiple
          tasks parallel jaisay chal sakte hain.
          Jab koi task wait me ho, CPU dusra kaam kar leta hai.
          Key Points:
            Non-blocking hota hai
            Fast hota hai I/O operations ke liye
            async aur await keywords use hotay hain
            Mostly APIs, web servers, real-time apps me use hota hai
           
        Example:
'''
import asyncio
async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 done")
async def task2():
    print("Task 2 start")   
    await asyncio.sleep(1)
    print("Task 2 done")
async def main():
    await asyncio.gather(task1(), task2())
asyncio.run(main())
'''
Output:
Task 1 start
Task 2 start
Task 2 done
Task 1 done

15. what is GIL in python?
        GIL Python ka ek lock hai jo ek time
        par sirf ek thread ko python bytecode execute
        karne deta hai, is liye CPU-bound
        multithreading limited hoti hai lekin 
        I/O-bound tasks me effective rehti hai
        GIL ka main purpose memory management ko simplify karna hai
        aur thread safety ensure karna hai.
        GIL ki wajah se Python me true parallelism achieve karna mushkil hota hai,
        lekin I/O-bound tasks me multi-threading kaafi effective hoti hai.
        Example:
'''
import threading
import time 
def cpu_bound_task():
    count = 0
    for _ in range(10**7):
        count += 1
threads = []
for i in range(4):
    thread = threading.Thread(target=cpu_bound_task)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
'''
16. what is multithreading and multiprocessing in python?
    i).Multithreading:
        Multithreading ek technique hai jisme 
        ek hi process ke andar multiple threads
        one by one execute hote hain
          key Points:
            - Threads lightweight hote hain
            - Threads same memory space share karte hain
            - Python me GIL ki wajah se CPU-bound tasks me limited hoti hai
            - Multithreading I/O-bound tasks ke liye effective hoti hai

    Example:
'''
import threading
import time
def io_bound_task():
    print("I/O task start")
    time.sleep(2)
    print("I/O task done")
threads = []
for i in range(4):
    thread = threading.Thread(target=io_bound_task)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
'''
    ii).Multiprocessing:
        Multiprocessing me multiple processes hote hain
        jo independently execute karte hain.
        Har process apna memory space use karta hai.    
        Multiprocessing CPU-bound tasks ke liye effective hoti hai.
    Example:
'''
import multiprocessing
import time
def cpu_bound_task():
    count = 0
    for _ in range(10**7):
        count += 1
processes = []
for i in range(4):
    process = multiprocessing.Process(target=cpu_bound_task)
    processes.append(process)
    process.start()
for process in processes:
    process.join()
'''

17. What is Middleware?
    Middleware Django ka component hai
    jo request aur response ke beech 
    processing ka kaam karta hai.
    Middleware ek tarah ka bridge hai
    jo Django application aur web server
    ke beech hota hai.
   
    Middleware ka use common tasks ke liye hota hai jaise:
    - Authentication
    - Security (CSRF, XSS)
    - Logging
    - Performance optimization
    Example:
'''
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response       
    def __call__(self, request):
        # Request processing
        print("Request received:", request.path)
        response = self.get_response(request)
        # Response processing
        print("Response sent with status:", response.status_code)
        return response
'''
'''




'''
18. what is  method overriding in Python?
    Method Overriding me child class parent
    class ke method ko redefine karke
    apna behavior implement karti hai.
                
        Example:
'''
class ParentClass:
    def show(self):
        print("Parent class method")
class ChildClass(ParentClass):
    def show(self):
        print("Child class method")
child = ChildClass()
child.show()  # Child class method
'''
Output:
Child class method
                    
19. what is __init__ Method?
    __init__ method ek special method hai jo class
    ka object create hone par automatically call
    hota hai.Iska use object ki 
    initial state set karne ke liye hota hai.
Example:
        '''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Asif", 20)
print(student1.name)
print(student1.age) 
'''
Output:
Asif
20
''' 
'''
20.what is Django ORM?
    Django ORM (Object-Relational Mapper)
    Django ka built-in powerful feature hai
    jo Python classes ke through database operations simplify karta hai.
        Developers ko direct SQL queries likhne ki zarurat nahi hoti
        ORM automatically database ke saath interact karta hai 
Key Features of Django ORM
            1 database:
                Django ORM multiple databases support karta hai
                jaise SQLite, PostgreSQL, MySQL, Oracle.
            2. Model Definition:
                Django ORM me models Python classes hoti hain
                jo database tables ko represent karti hain.
            3. QuerySet API:
                Django ORM QuerySet API provide karta hai
                jo database queries ko Python code ke zariye likhne ki sahulat deta hai.
            4. Relationships Handling:
                Django ORM foreign keys, many-to-many relationships
                aur one-to-one relationships ko easily handle karta hai.
            5. Migrations:
                Django ORM database schema changes ko manage karne ke liye
                migrations ka use karta hai.
Example of Django ORM:
'''
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
# Creating a new book record
new_book = Book(title="Django for Beginners", author="John Doe", published_date="2023-01-01")
new_book.save()
# Querying books
books = Book.objects.filter(author="John Doe")
for book in books:
    print(book.title)
 '''       
21.what is migrations in Django?
    Migration Django ka system hai jo models
    ke changes ko database schema mein safely apply karta hai.
    Key Features of Django Migrations:
        1. Automatic Generation:
            Django migrations automatically generate hoti hain
            jab hum apne models me changes karte hain.
        2. Version Control:
            Migrations database schema changes ko version control karti hain,
            jisse hum easily changes ko track kar sakte hain.
        3. Rollback Support:
            Migrations me rollback support hota hai,
            jisse hum previous schema state par wapas ja sakte hain.
        4. Dependency Management:
            Migrations dependencies ko manage karti hain,
            jisse changes correct order me apply hoti hain.
    Example of Django Migrations:

what is migrate?
      Migrate migration files ko database schema mein apply karta hai.
22.what is schema?
      Schema database ka structure hota hai jo tables,
      fields, relationships ko define karta hai.

23.how many types of relationships are there in django?
        Django me 3 types of relationships hoti hain:
        1. One-to-One Relationship
        2. One-to-Many Relationship
        3. Many-to-Many Relationship
    
    i).one-to-one relationship in django?
            One-to-One relationship me ek model ka ek record
            sirf dusre model ke ek record se linked hota hai.
            Example:     
'''    
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()

'''
    ii).one-to-many relationship in django?
            One-to-Many relationship me ek model ka ek record
            multiple records se linked hota hai.
            Example:
'''
from django.db import models
class AuthorOneToMany(models.Model):
    name = models.CharField(max_length=100)
class BookOneToMany(models.Model):  
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorOneToMany, on_delete=models.CASCADE)       
'''
    iii).many-to-many relationship in django?
            Many-to-Many relationship me ek model ke multiple records
            dusre model ke multiple records se linked hote hain.
            Example:
'''
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
'''24.what is select_related and prefetch_related in django?
    i).select_related:
        select_related foreign key aur one-to-one relationships
        ke liye use hota hai.
        Ye SQL join use karke related objects ko
        single query me fetch karta hai.
    Example:
'''
# Using select_related
books = Book.objects.select_related('author').all()
for book in books:
    print(book.title, book.author.name)
'''
    ii).prefetch_related:
        prefetch_related many-to-many aur reverse foreign key relationships
        ke liye use hota hai.
        Ye separate queries use karke related objects ko fetch karta hai
        aur phir Python me unhe combine karta hai.
    Example:
'''
# Using prefetch_related
authors = Author.objects.prefetch_related('book_set').all()
for author in authors:
    for book in author.book_set.all():
        print(author.name, book.title)  
'''25.what is n+1 problem in django?
        N+1 problem ek performance issue hai
        jo tab hota hai jab ek query ke baad
        related objects ke liye additional queries execute hoti hain.
        Isse database me unnecessary load badhta hai
        aur application slow ho jata hai.
        Example of N+1 Problem:
'''
# N+1 problem example
books = Book.objects.all()
for book in books:
    print(book.title, book.author.name)  # Additional query for each book
'''
        Solution using select_related:
'''
# Solution using select_related
books = Book.objects.select_related('author').all()
for book in books:
    print(book.title, book.author.name)  # Single query for all books and authors
'''
26.what is transaction in django?
   Transaction database operations ka ek 
   unit hai jo all-or-nothing principle pe kaam karta hai,
    Key Features of Django Transactions:
        1. Atomicity:
            Transactions atomic hoti hain,
            yani ya to saare operations successful hote hain
            ya koi bhi operation nahi hota.
        2. Consistency:
            Database hamesha valid state me rahe.
        3. Isolation:
            Ek transaction dusre transaction ko disturb na kare
        4. Durability:
            Commit hone ke baad changes permanent ho jate hain.
    Example of Django Transactions:
'''
from django.db import transaction   
@transaction.atomic
def transfer_funds(account_from, account_to, amount):
    account_from.balance -= amount
    account_to.balance += amount
    account_from.save()
    account_to.save()
'''27. what is list comprehension in python?
    List comprehension ek short-hand way
    hai list banane ka, for loop ke sath condition apply karke
    Example of List Comprehension:
'''
# Using list comprehension to create a list of squares
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
28. what is normalization in database?
        Normalization database design ka process hai
        jisme data ko organize kiya jata hai
        taake redundancy kam ho aur data integrity maintain rahe.
        Normalization ke different levels hote hain,
        jise normal forms kehte hain (1NF, 2NF, 3NF, BCNF).
        Example of Normalization:
        
        1NF: Har cell atomic ho aur repeating group na ho;
        2NF: Har non-key column poore primary key pe depend kare;
        3NF: Non-key column sirf primary key pe depend kare, dusre column pe nahi.
'''
# Unnormalized Table
'''
StudentID | StudentName | Course1 | Course2
----------------------------------------------      
1         | Ali         | Math    | Science
2         | Sara        | Math    | History
'''
# First Normal Form (1NF)
'''
StudentID | StudentName | Course
--------------------------------------
1         | Ali         | Math
1         | Ali         | Science
2         | Sara        | Math
2         | Sara        | History
'''
# Second Normal Form (2NF)
'''
Students Table:     
StudentID | StudentName
------------------------
1         | Ali         
2         | Sara    
Courses Table:
StudentID | Course
----------------------
1         | Math
1         | Science
2         | Math
2         | History
'''
# Third Normal Form (3NF)
'''
Students Table:
StudentID | StudentName
------------------------
1         | Ali         
2         | Sara    
Courses Table:
CourseID | CourseName
------------------------
1        | Math
2        | Science
3        | History
Enrollments Table:
StudentID | CourseID
------------------------
1         | 1
1         | 2
2         | 1
2         | 3

29. what is time complexity 
    Time Complexity ek DSA concept hai jo
    batata hai ke input size ke hisaab se
    algorithm ya code ko run karne me kitna time lagega.
30. what is space complexity 
    Space Complexity algorithm ki memory requirement ka measure hai,
    jo batata hai input size ke hisaab se kitni memory chahiye.    

31. what is Queue?
    Queue ek linear data structure hai jo  
    (FIFO) principle pe kaam karta hai.
    First In, First Out       

32. what is garbage collector?
    Garbage Collection Python ka automatic memory
    management system hai jo unused objects ko delete
    karke memory free karta hai.
what is REST APIs (DRF)?:
        REST (Representational State Transfer) APIs aik architectural style hai
        jo web services banane ke liye use hota hai.
                Ye APIs client aur server ke darmiyan data exchange karte hain
                HTTP methods jaise GET, POST, PUT, DELETE ka use hota hai
        Django REST Framework (DRF) Django ka powerful library hai
        jo RESTful APIs banane ke liye use hota hai.

    Key Features of Django REST Framework (DRF):
        1. Serialization:
            DRF data ko JSON, XML jaise formats me convert karne ke liye serializers provide karta hai.
        2. ViewSets and Routers:
            DRF ViewSets aur Routers provide karta hai jo API endpoints ko easily define karne me madad karte hain.
        3. Authentication and Permissions:
            DRF multiple authentication methods aur permission classes support karta hai.
        4. Browsable API:
            DRF ek browsable API interface provide karta hai jo developers ke liye API testing aur exploration ko asaan banata hai.
            Example of Django REST Framework (DRF):




2. Introduction to Django Framework      
    Django Kya Hai?:
        i). Django ek high-level Python web framework hai jo fast,
            secure aur scalable web applications banane ke liye use hota hai.
        ii). Yeh MVT (Model-View-Template) pattern follow karta hai,
            na k MVC (Model-View-Controller).                        
        iii). Batteries-Included Framework     
                Django ko "batteries-included" is liye kaha jata hai
                kyun ke isme bohot si cheezen built-in hoti hain:
                
        Example:
        - Authentication (login, logout, permissions)
            - Admin Panel (auto-generated)
            - ORM (database queries without SQL)
            - Forms & validations
            - URL routing
            - Security features
            
            Iska faida:
                - Developer ko har cheez zero se likhne ki zarurat nahi hoti,
                development fast ho jati hai.

iv). Security (Very Important for Interview) 
     Django security by default handle karta hai:             
     
     - SQL Injection protection
        a). SQL Injection kya hai?
            SQL Injection aik security attack hai jisme attacker malicious SQL code
            inject karta hai database mein.
            Isse attacker sensitive data chura sakta hai,
                manipulate kar sakta hai ya delete kar sakta hai.
            a). Malicious SQL kya hota hai?
                Malicious SQL wo code hota hai jo database ko nuksan pohcha sakta hai,
                jaise ke data chori kr lena, delete kar dena ya unauthorized access lena.
            b). Example of SQL Injection:
                Suppose ek login form hai jisme username aur password fields hain.
                Agar user input ko properly sanitize na kiya jaye,
                to attacker kuch aisa input de sakta hai:
                Username: ' OR '1'='1
                Password: ' OR '1'='1
                Is input se SQL query kuch aisi ban jayegi:
                SELECT * FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1';
                Yeh query hamesha true return karegi,
                jisse attacker unauthorized access le sakta hai.
            c). Consequences of SQL Injection:
                - Data theft
                - Data manipulation
                - Data deletion
                - Unauthorized access
        
        b). Django kaise protect karta hai?
        Django ORM automatically parameterized queries use karta hai,
        jisse SQL Injection attacks se protection  hoti hai.
        
    - Cross-Site Scripting (XSS)

        a).  Roman Urdu Vocabulary:
            - Security vulnerability → system ki kamzori
            - Attacker → hacker / attack karne wala
            - Malicious scripts → nuqsaan pohanchane wali JavaScript
            - Inject karna → zabardasti ghusa dena
            - Trusted website → wo website jahan users bharosa karte hain
        
        b). XSS ke nuksanat (Consequences)
                    i). Cookie Theft
                            - Cookie → browser mein saved login info
                            - Attacker user ki cookies chura kar uske account mein
                                login kar sakta hai.

                    ii). Session Hijacking
                            - Session → user ka login time
                            - Hijack → zabardasti control lena
                            - Attacker user ke login session ka control le leta hai.

                    iii). Phishing Attacks
                            - Phishing → fake pages bana kar password churaana
                            - User ko fake form dikha kar password le liya jata hai.

                        iv). Website Defacement

                            - Defacement → website ka look/text bigaarna
                            - Website par ghalat message ya images show hone lagti hain.
                                        
    a). XSS kya hai?
                XSS aik security vulnerability hai jisme attacker malicious scripts
                inject karta hai trusted websites mein.
                Isse attacker users ke browsers mein unwanted actions perform kar sakta hai,
                jaise ke cookies chura lena, session hijack karna ya phishing attacks karna.
            b). Example of XSS:
                Suppose ek comment section hai jisme users apne comments post kar sakte hain.
                Agar input ko properly sanitize na kiya jaye,
                to attacker kuch aisa comment post kar sakta hai:
                <script>alert('Hacked!');</script>
                Jab koi user yeh comment dekhega, to yeh script execute ho jayegi
                aur alert box show karegi.
            c). Consequences of XSS:
                - Cookie theft
                - Session hijacking
                - Phishing attacks
                - Defacement of websites
                
        b). Django kaise protect karta hai?
            Django templates by default auto-escaping enable karte hain,
            jisse malicious scripts automatically escape ho jati hain.
        
            a).  Mushkil alfaaz → Asaan matlab

                        - Auto-escaping → dangerous characters ko safe bana dena
                        - < → &lt;
                        - > → &gt;
                        - Example:
                        - User ne input diya:
                        - <script>alert('Hacked!');</script>
                        - Django isko browser ko aise bhejta hai:
                        - &lt;script&gt;alert('Hacked!');&lt;/script&gt;
                            - Browser isko text samajhta hai, code nahi
                            - Script execute nahi hoti 
            
            - Short Interview Answer:
                i).   XSS aik attack hai jisme attacker malicious JavaScript inject karta
                        hai jo users ke browser mein
                        execute hoti hai. Django templates by default auto-escaping ke
                        zariye XSS se protect karti hain.
                                                    
                            
        
        
    - Cross-Site Request Forgery (CSRF)
    - Clickjacking protection
    - Secure password hashing
    Iska faida:
            - Developers ko security features implement karne ki kam zarurat hoti hai,
                applications zyada secure hoti hain. 
            
            

v). Scalability:
Django applications easily scale ho sakti hain, chhoti se le kar bohot badi applications tak.
Examples: 
    - Instagram,
    - Pinterest,
        - Disqus,
        - Mozilla
        - Reddit
        
vi). Rapid Development:
        Django ka motto hai:
        Don’t Repeat Yourself (DRY)
        - Iska matlab hai ke code ko baar baar repeat na karo, reusable components banao.
        - Isse development fast hoti hai aur maintenance easy ho jata hai.
        - Example: Django ka admin panel automatically generate ho jata hai,
            jisse developers ko manually admin interface banane ki zarurat nahi hoti.
        - Less code
        - Reusable components
        - Fast feature development



'''            

