


'''                             ============== Python Django Interview Preparation ==============                             


Prepared by Muhammad Nouman (In Roman Urdu Language)
Date: [22/january/2026]
Version: 1.0


1. Introduction to Python and Django

    Python Kya Hai?:
                   i). High-level programming language, easy syntax,
                       used for web, data science, AI.
                       
                       Example:
                            print("Hello World").
                            
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
                                        jisse SQL Injection attacks se bachav hota hai.
                                        
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

 2. What is iteration?
        Iteration ek process hota hai jo ek iterable object ko iterate karta hai.
        Iteration ko iterate karte waqt, iteration ek next element return karta hai.
        
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

3. what is iterator?
        Iterator ek object hota hai jo iterable objects ko iterate karta hai.
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

4. what is iterable?
        Iterable ek object hota hai jisko hum loop ke zariye iterate kar sakte hain
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

5. Difference between iterable and iterator?
        Iterable:
                - Iterable ek aisa object hota hai jisko hum loop ke zariye iterate kar sakte hain.
                - Iterable objects me list, tuple, string, dictionary, set, range shamil hain.
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

        Iterator:
                - Iterator ek aisa object hota hai jo iterable objects ko iterate karta hai.
                - Iterator object me next() method hota hai jo next element return karta hai.
                - Iterator object me __iter__() method hota hai jo khud ko return karta hai.        
'''
                    my_list = [1, 2, 3]
                    iterator = iter(my_list)  # my_list is iterable
                    print(next(iterator))  # prints 1
                    print(next(iterator))  # prints 2
                    print(next(iterator))  # prints 3     
'''
7. what is generator?
        Generator ek function hai jo yield keyword use krte hain or value ko one by one return krte hain

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
Difference between generator and iterator?
        Generator:
                - Generator ek special type ka iterator hota hai jo function ke zariye create hota hai.
                - Generator function me yield keyword use hota hai jo value ko one by one return karta hai.
                - Generator function state ko maintain karta hai,
                  jisse next value return karne ke liye function wapas se call karne ki zarurat nahi hoti.
                - Memory efficient hota hai kyun ke ye saari values ek sath memory me store nahi karta.
                
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
8. what is decorator?
        Decorator ek function hota hai jo dusre function ki functionality ko bina change kiye enhance karta hai.
        decorators Python me bohot commonly use hote hain, especially Django me.
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



9. What is OOP?
        OOP (Object-Oriented Programming) ek programming paradigm hai jo
        real-world entities ko objects aur classes ki form mein represent karta hai.
        example:
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")        
'''
        1. What are the main pillars of OOP?
        OOP ke 4 pillars hain: Encapsulation, Inheritance, Polymorphism, Abstraction.
        
        i). Encapsulation
                    Encapsulation ka matlab hai data aur methods ko aik class me band karna 
                    aur data ko direct access se protect karna.
                    encapsulation se data security aur integrity ensure hoti hai.
                    
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
                  Inheritance aik OOP concept hai jisme child class, parent class ki properties
                  aur methods ko inherit karti hai.
                  Inheritance code reusability aur maintainability improve karta hai.

                  types of Inheritance:
                        - Single Inheritance
                        - Multi-level Inheritance
                        - Multiple Inheritance

                    what is single Inheritance?:
                       Single Inheritance me aik child class sirf aik hi parent class se inherit karti hai.
                       Yeh sab se simple aur commonly used inheritance type hai.
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
                    what is multi-level Inheritance?:
                        Multi-level Inheritance me aik child class  parent class se inherit karti hai,
                        or parent   grand parent class se inherit karti hai.
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
                    what is multiple Inheritance?:
                        Multiple Inheritance me aik child class ek se zyada parent classes se inherit karti hai.
                        Is me child class multiple classes ki properties aur methods use kar sakti hai.
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
                    Polymorphism aik OOP concept hai jisme same method ya function different data types ya objects ke
                    liye different behavior provide karta hai.
                    Same method name, lekin different behavior.
                    overloading aur overriding polymorphism ke do main types hain.
                    1. Method Overloading:
                        Method Overloading me aik class me same method name ke multiple versions hote hain  
                        jo different parameters accept karte hain.
                        Python me method overloading directly support nahi hoti,
                        lekin hum default arguments ya *args, **kwargs ka use karke achieve kar sakte hain. 
                         
                    Example:
                    '''
class Dog:
    def sound(self):
        print("Dog wao wao karta hai")

class Cat:
    def sound(self):
        print("Cat meow karti hai")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


                    '''
                    iv) what is Abstraction?
                    Abstraction aik OOP concept hai jisme complex implementation details ko hide karke
                    sirf essential features ko expose kiya jata hai.
                    Sirf important cheezain dikhana aur
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
            10. What is Middleware?
                Middleware Django ka component hai jo request aur response ke beech processing ka kaam karta hai.
                Middleware ek tarah ka bridge hai jo Django application aur web server ke beech hota hai.
                Middleware request ko process karta hai before it reaches the view,
                aur response ko process karta hai before it is sent to the client.
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
                11. what is  method overriding in Python?
                        Method Overriding me child class parent class ke method ko redefine karke
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
                                 
            12.  what is __init__ Method?
                    __init__ method ek special method hai jo class ka object create hone
                    par automatically call hota hai.Iska use object ki initial state set karne ke liye hota hai.
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
                     what is Django ORM?
                                Django ORM (Object-Relational Mapper) Django ka built-in powerful feature hai
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
'''            

