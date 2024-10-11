from time import sleep
import asyncio

class SyncSpongerBob:

    # assar o pão
    async def bake_the_bread(self):
        await asyncio.sleep(3)
        print('Assando o pão')

    # Fritar hamburger
    async def fry_hamburger(self):
        await asyncio.sleep(10)
        print('Fritando o humburger')

    # Fazer milk shake
    async def make_milkshake(self):
        await asyncio.sleep(8)
        print('Fazendo o milksheke')
        
    # Montar sanduiche
    async def mount_sandwich(self):
        await asyncio.gather(
            self.bake_the_bread(),
            self.fry_hamburger(),
        )
        print('Montando o sanduiche 2')

        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())

    async def snack(self):
        await asyncio.gather(self.make_milkshake(), self.mount_sandwich())


sync_sponger_bob = SyncSpongerBob()
asyncio.run(sync_sponger_bob.snack())