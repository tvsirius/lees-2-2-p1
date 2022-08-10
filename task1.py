import threading
from time import sleep
import time
'''


x=[]


def cook(name='блюдо', t=5):
    print(f'Начали готовить {name}')
    sleep(t)
    print(f'{name} готово!')
    x.append(name)


t1 = threading.Thread(target=cook, args=('Борщ', 8))
t2 = threading.Thread(target=cook, args=('Рис', 4))
t3 = threading.Thread(target=cook, args=('Суши', 6))

t1.start()
t2.start()

t2.join()
print('Рис можно использовать для приготовления суши')
t3.start()

t1.join()
t3.join()

print(f'Готово, блюда: {x} на столе')
'''

def func():
    for i in range(1000000000):
        pass

def test_1():
    t = time.time()
    func()
    func()
    func()
    func()
    func()
    print(time.time() - t)


def test_2():
    t = time.time()
    t1=threading.Thread(target=func)
    t2=threading.Thread(target=func)
    t3=threading.Thread(target=func)
    t4=threading.Thread(target=func)
    t5=threading.Thread(target=func)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print(time.time() - t)

test_1()
test_2()