import threading
from time import sleep


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
