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


    # Montar sanduiche
    async def assemble_sandwich(self):
        await asyncio.sleep(5)
        print('Montando o sanduiche')

    # Fazer milk shake
    async def make_milkshake(self):
        await asyncio.sleep(6)
        print('Fazendo o milksheke')

    async def snack(self):
        await asyncio.gather(
            self.bake_the_bread(),
            self.fry_hamburger(),
            self.make_milkshake()
        )
        
        self.assemble_sandwich()


sync_sponger_bob = SyncSpongerBob()
asyncio.run(sync_sponger_bob.snack())