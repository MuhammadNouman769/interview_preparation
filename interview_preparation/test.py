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
mera_apna_for_loop('f list{a}')
mera_apna_for_loop(b)
mera_apna_for_loop(c)
mera_apna_for_loop(d)
mera_apna_for_loop(e)