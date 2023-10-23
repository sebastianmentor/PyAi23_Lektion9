import os 
import json
from enum import Enum
import rich.traceback

rich.traceback.install()

class TransaktionsTyp(Enum):
    INSÄTTNING = 1
    UTTAG = 2
    SKAPAD = 3

class Transaktion:
    def __init__(self, kontonummer, transaktionstyp:TransaktionsTyp, summa) -> None:
        self.kontonummer = kontonummer
        self.typ = transaktionstyp
        self.summa = summa

    def hämta_tranasktion(self) -> dict:
        return dict(kontonummer= self.kontonummer,
                    transaktion=self.typ.name,
                    summa=self.summa
                    )

class Bankkonto:
    def __init__(self, kontonummmer, saldo = 0) -> None:
        self._kontonummer = kontonummmer
        self._saldo = saldo

    def hämta_kontonummer(self):
        return self._kontonummer
    
    def hämta_saldo(self):
        return self._saldo
    
    def uppdatera_saldo(self,nytt_saldo):
        self._saldo = nytt_saldo

    def __str__(self):
        return f'{self._kontonummer} har saldo {self._saldo}'
    
class Bankomat:
    def __init__(self, lista_med_bankkonton,transaktionshistorikfil) -> None:
        self._fil_med_transaktionshistorik = transaktionshistorikfil
        self._bankkonton = {}
        self._fyll_upp_med_bankkonton(lista_med_bankkonton)

    @staticmethod
    def spara_transaktion(transaktion:Transaktion, fil:str):
        if os.path.exists(fil):
            with open(fil, 'a') as f:
                f.write(json.dumps(transaktion.hämta_tranasktion())+'\n')

    @staticmethod
    def skapa_transaktion(kontonummer:int, typ:TransaktionsTyp, summa:int) -> Transaktion:
        return (Transaktion(kontonummer,typ.name,summa))

    def lägg_till_nytt_bankkonto(self, bankkonto:Bankkonto):
        if bankkonto.hämta_kontonummer() in self._bankkonton:
            print('Kontonummer finns redan')
        else:
            self._bankkonton[bankkonto.hämta_kontonummer()] = bankkonto

    def _fyll_upp_med_bankkonton(self, lista:list[Bankkonto]):
        for konto in lista:
            self._bankkonton[konto.hämta_kontonummer()] = konto

    def antal_konton(self)->int:
        return len(self._bankkonton)
        
    def sätta_in_pengar(self, kontonummer, summa):
        if kontonummer in self._bankkonton.keys():
            if summa > 0:
                b: Bankkonto = self._bankkonton[kontonummer]
                b.uppdatera_saldo(b.hämta_saldo() + summa)
                t = Transaktion(kontonummer, TransaktionsTyp(1),summa)
                Bankomat.spara_transaktion(t,self._fil_med_transaktionshistorik)
            else:
                raise ValueError
        else:
            print('Kontot finns inte')
        
    def ta_ut_pengar(self, kontonummer, summa):
        if kontonummer in self._bankkonton.keys():
            if summa > 0:
                b: Bankkonto = self._bankkonton[kontonummer]
                if b.hämta_saldo() > summa:
                    b.uppdatera_saldo(b.hämta_saldo()-summa)
                else:
                    print('För lite pengar!')
            else:
                raise ValueError
        else:
            print('Kontot finns inte')
    
    def hämta_bankkonto(self, kontonummer):
        return self._bankkonton[kontonummer] if kontonummer in self._bankkonton else None
    
 


lista_med_konton = []
for i in range(1001,1101):
    lista_med_konton.append(Bankkonto(i))

bankomat = Bankomat(lista_med_konton,'transaktionshistorik.txt')

print(bankomat.antal_konton())
bankomat.lägg_till_nytt_bankkonto(Bankkonto(1100))
bankomat.lägg_till_nytt_bankkonto(Bankkonto(1101))
print(bankomat.antal_konton())

bankomat.sätta_in_pengar(1001, 500)
print(bankomat.hämta_bankkonto(1001).hämta_saldo())
bankomat.ta_ut_pengar(1001, 600)