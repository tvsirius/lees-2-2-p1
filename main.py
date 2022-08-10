import threading
from time import sleep


x=[]


def cook(name='блюдо', t=5):
    print(f'Начали готовить {name}')
    sleep(t)
    print(f'{name} готово!')
    x.append(name)


t1 = threading.Thread(target=cook, args=('Борщ',))
t2 = threading.Thread(target=cook, args=('Пельмени', 10))
t3 = threading.Thread(target=cook, args=('Плов',))

#
# cook("Борщ")
# cook("Пельмени")
# cook("Плов")

t1.start()
t2.start()
t3.start()

t2.join(timeout=15)

print(x)