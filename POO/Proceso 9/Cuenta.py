class Cuenta:
    def __init__(self, numero, saldo):
        self.numero= str(numero)
        self.saldo= int(saldo)
        
    def getSaldo(self) -> int:
        print(self.saldo)
        return self.saldo
    
    def getNumero(self) -> str:
        print(self.numero)
        return self.numero
    
    def __str__(self) -> str:
        print(f'cuenta={self.numero},saldo={self.saldo}')
        
    def compareTo(self,x) -> int:
        if self.saldo>x.saldo or self.saldo<x.saldo:
            return self.saldo-x.saldo
        else:
            return 0
        
    def depositar(self,x) -> None:
        self.saldo+=x
        
    def girar(self,x) -> bool:
        if (self.saldo-x)>0:
            self.saldo-=x
            return (self.saldo-x)>0
        else: 
            return (self.saldo-x)>0

c=Cuenta('1', 100)
d=Cuenta('2', 200)
c.getSaldo()
c.getNumero()
c.__str__()
print(c.compareTo(d))
c.depositar(20)
print(c.girar(400))
    