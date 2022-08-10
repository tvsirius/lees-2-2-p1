from time import sleep

def cook(name):
    print(f'Подготовить блюдо {name}')
    print(f'Поставить {name} на плиту')
    sleep(20)
    print(f'Блюдо {name} готово')

cook('Лапша')
cook('Курка')
cook('Пельмени')

