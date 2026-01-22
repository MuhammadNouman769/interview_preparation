


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
                   i). Django ek high-level Python web framework hai jo fast, secure aur scalable web applications banane ke liye use hota hai.
                  ii). Yeh MVT (Model-View-Template) pattern follow karta hai, na k MVC (Model-View-Controller).                        
                 iii). Batteries-Included Framework     
                            Django ko “batteries-included” is liye kaha jata hai kyun ke isme bohot si cheezen built-in hoti hain:
                            
                        Example:
                          - Authentication (login, logout, permissions)
                               - Admin Panel (auto-generated)
                                - ORM (database queries without SQL)
                                - Forms & validations
                                - URL routing
                                - Security features
                                
                                Iska faida:
                                          - Developer ko har cheez zero se likhne ki zarurat nahi hoti, development fast ho jati hai.
                
                  iv). Security (Very Important for Interview) 
                           Django security by default handle karta hai:             
                            - SQL Injection protection
                                      a). SQL Injection kya hai?
                                        SQL Injection aik security attack hai jisme attacker malicious SQL code inject karta hai database mein.
                                        Isse attacker sensitive data chura sakta hai, manipulate kar sakta hai ya delete kar sakta hai.
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
                                                Yeh query hamesha true return karegi, jisse attacker unauthorized access le sakta hai.
                                           c). Consequences of SQL Injection:
                                                - Data theft
                                                - Data manipulation
                                                - Data deletion
                                                - Unauthorized access
                                      
                                      b). Django kaise protect karta hai?
                                        Django ORM automatically parameterized queries use karta hai,
                                        jisse SQL Injection attacks se bachav hota hai.
                                        
                                 - Cross-Site Scripting (XSS)
                                    - Cross-Site Request Forgery (CSRF)
                                    - Clickjacking protection
                                    - Secure password hashing
                                    Iska faida:
                                            - Developers ko security features implement karne ki kam zarurat hoti hai, applications zyada secure hoti hain.                       
                        
                  v). Scalability:
                           Django applications easily scale ho sakti hain, chhoti se le kar bohot badi applications tak.
                           Examples: 
                                   - Instagram,
                                   - Pinterest,
                                      - Disqus,
                                        - Mozilla
                                        
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


SECTION 1: Object-Oriented Programming (OOP)
================================================

        1. What is OOP?
                        OOP ek programming style hai jisme hum real-life cheezon
                        ko objects aur classes ki form mein represent karte hain.
'''

# Example:
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} car {self.color} color ki hai.")

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.drive()
car2.drive()

'''
Output:
Toyota car Red color ki hai.
Honda car Blue color ki hai.
'''


'''
        2. Why OOP is used?
                            OOP ko is liye use kiya jata hai kyun ke ye:
                            - Code reusable banata hai
                            - Security provide karta hai
                            - Maintainable hota hai
                            - Real-world problems ko easily handle karta hai
'''

# Example:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposit ho gaye. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw ho gaye. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance!")

account1 = BankAccount("Ali", 5000)
account2 = BankAccount("Sara", 10000)

account1.deposit(2000)
account2.withdraw(3000)

'''
Output:
2000 deposit ho gaye. New balance: 7000
3000 withdraw ho gaye. Remaining balance: 7000
'''


'''
SECTION 2: Four Pillars of OOP
================================================
        i) Encapsulation
                            Encapsulation ka matlab data ko hide karna aur
                            sirf methods ke zariye access dena.
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
        ii) Inheritance
                        Inheritance ka matlab parent class ki properties
                        child class use kar sakti hai.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def employee_info(self):
        print(f"Salary: {self.salary}")

emp = Employee("Ali", 30, 50000)
emp.info()
emp.employee_info()

'''
        iii) Polymorphism
                            Same method name, lekin different behavior. 
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
Interview Tip:
Mobile ka power button – same hota hai,
lekin on aur off dono kaam karta hai.
'''


'''
iv) Abstraction

Sirf important cheezain dikhana aur
implementation details hide karna.
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
SECTION 3: OOP vs Procedural Programming
================================================
        Procedural:
        - Functions aur data separate hote hain

        OOP:
        - Data aur methods class ke andar hote hain
        '''

# Procedural Example
balance = 5000

def deposit(amount):
    global balance
    balance += amount

deposit(1000)
print(balance)

'''
Data aur function separate → security kam
'''

# OOP Example
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(self.__balance)

acc = Account(5000)
acc.deposit(1000)

'''
Data secure aur controlled → encapsulation
'''


'''
SECTION 4: Django / Backend Concepts
================================================
5. What is ORM?

Django ORM ek Object Relational Mapper hai
jo Python objects ke zariye database ke sath
kaam karne deta hai.
'''

'''
6. What is Method Overriding?

Child class parent class ke method ko
same name ke sath redefine karti hai.
'''

'''
7. What is Decorator?

Decorator ek function hota hai jo
dusre function ki functionality ko
bina change kiye enhance karta hai.

Django me decorators use hote hain:
- Authentication
- Authorization
- Permissions
'''

'''
8. What is Middleware?

Middleware Django ka component hai jo
request aur response ke darmiyan kaam karta hai.

Uses:
- Authentication
- Security (CSRF, XSS)
- Logging
- Performance optimization
'''


'''
SECTION 5: Very Common Interview Questions
================================================
- Difference between class and object?
- Encapsulation with example?
- Difference between abstraction and encapsulation?
- What is inheritance and why use it?
- What is polymorphism in simple words?
- Can polymorphism exist without inheritance?
- What is constructor? Is it inherited?
'''


'''
SECTION 6: Python-Specific OOP
================================================
- __init__
- self
- Instance vs class variables
- Method overriding in Python
'''


'''
SECTION 7: Job Description Reference
================================================
Job Title: Junior Django / Python Developer

Requirements:
- Python & Django (1+ year)
- Django ORM
- REST APIs (DRF)
- PostgreSQL / MySQL
- Git / GitHub
- Authentication & Security

Nice to Have:
- Docker
- AWS
- Celery / Redis
- CI/CD
'''
