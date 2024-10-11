import asyncio

async def sum(a, b):
    return a + b

async def print_sum(a, b):
    result = await sum(a, b)
    print(f'Resultado igual a {result}')


envent_loop = asyncio.new_event_loop()
envent_loop.run_until_complete(print_sum(2, 3))