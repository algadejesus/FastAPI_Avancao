from time import sleep

class SyncSpongerBob:

    # assar o pão
    def bake_the_bread(self):
        sleep(3)
        print('Assando o pão')

    # Fritar hamburger
    def fry_hamburger(self):
        sleep(10)
        print('Fritando o humburger')


    # Montar sanduiche
    def assemble_sandwich(self):
        sleep(5)
        print('Montando o sanduiche')

    # Fazer milk shake
    def make_milkshake(self):
        sleep(6)
        print('Fazendo o milksheke')

    def snack(self):
        self.bake_the_bread()
        self.fry_hamburger()
        self.assemble_sandwich()
        self.make_milkshake()
        
sync_sponger_bob = SyncSpongerBob()
sync_sponger_bob.snack()