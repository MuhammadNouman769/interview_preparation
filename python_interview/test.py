

# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return len(self.items) == 0

#     def insert(self, item):
#         self.items.append(item)

#     def delete(self):
#         if self.isEmpty():
#             print("Queue is empty")
#             return None
#         else:
#             return self.items.pop(0)

# q = Queue()
# q.insert(10)
# q.insert(2)
# q.insert(3)

# print(q.delete())  # 10
# print(q.delete())  # 2
# print(q.delete())  # 3
# print(q.delete())  # Queue is empty


# numbers = {"apple", "banana", "cherry", "cherry"}
# print(numbers)
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)   # Union
# print(A & B)   # Intersection
# print(A - B)   # Difference

# implicit_type_conversion example
# a = 10
# b = 20.1
# c = a + b
# print(type(c))
# explicit_type_conversion example
# a = 10
# b = 20.1
# c = a + int(b)
# print(c)

# lamda = double = lambda a, b, c: (a + b - c) 
# print(lamda(5, 5, 10))

# def appl(fx, value):
#     return 6  + fx(value)
# print(appl(cube,2))  

# import time

# def task1():
#     time.sleep(1)
#     print("Task 1 done")

# def task2():
#     print("Task 2 done")

# task1()
# task2()
# import asyncio

# async def task1():
#     await asyncio.sleep(10)
#     print("Task 1 done")

# async def task2():
#     print("Task 2 done")

# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

import threading
import time 
def cpu_bound_task():
    count = 1
    for _ in range(10**7):
        count += 1
threads = []
for i in range(4):
    thread = threading.Thread(target=cpu_bound_task)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()