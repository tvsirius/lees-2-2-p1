import asyncio

x = []


async def cook(name='блюдо', t=5):
    print(f'Начали готовить {name}')
    await asyncio.sleep(t)
    print(f'{name} готово!')
    x.append(name)


async def main():
    t1 = asyncio.create_task(cook('борщ'))
    t2 = asyncio.create_task(cook('плов', 7))
    t3 = asyncio.create_task(cook('спагетти с мясом курицы'))

    await t1
    await t2
    await t3


loop = asyncio.get_event_loop()

# tasks = asyncio.gather(cook('борщ'), cook('плов',7), cook('спагетти с мясом курицы'))


loop.run_until_complete(main())

print(x)