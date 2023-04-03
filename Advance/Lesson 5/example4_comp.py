import asyncio


@asyncio.coroutine
def async_worker(number, divider):
    print('Worker {} started'.format(number))
    yield from asyncio.sleep(0)
    print(number / divider)


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(220, 10)),
    event_loop.create_task(async_worker(50, 25)),
    event_loop.create_task(async_worker(250, 25)),
    event_loop.create_task(async_worker(600, 15)),
    event_loop.create_task(async_worker(50, 2)),
    event_loop.create_task(async_worker(1050, 25)),
    event_loop.create_task(async_worker(700, 35)),
]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()
