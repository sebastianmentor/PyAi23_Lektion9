class NegativtNummerError(Exception):
    def __init__(self) -> None:
        self._message = 'Negativa nummer är inte tillåtna!'

    def __str__(self) -> str:
        return self._message
    
class Bankkonto:
    def __init__(self, kontonummmer:int, saldo:int = 0) -> None:
        self._kontonummer = kontonummmer
        self._saldo = saldo

    def hämta_kontonummer(self)->int:
        return self._kontonummer
    
    def hämta_saldo(self)->int:
        return self._saldo

    def insättning(self,insättning:int):
        if insättning < 0:
            raise NegativtNummerError
        
        else:
            self._saldo+=insättning

    def uttag(self,uttag:int) -> bool:
        if uttag < 0: 
            raise NegativtNummerError
        
        elif uttag < self._saldo:
            self._saldo -= uttag
            return True
        
        else:
            return False

    def __str__(self) -> str:
        return f'Kontonummer:{self._kontonummer}\nSaldo:{self._saldo}'
    
    def __repr__(self) -> str:
        return f'Bankkonto("{self._kontonummer}","{self._saldo}")'
    

if __name__ == "__main__":
    try:
        b = Bankkonto(1001)
        b.insättning('-1')
    except NegativtNummerError as e:
        print(f'Error {e}')
    except ValueError as e:
        print(f'Error {e}')
    except TypeError as e:
        print(f'Error {e}')

