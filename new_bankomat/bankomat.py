from .bankkonto import Bankkonto
from .tansaktion import Transaktion, TransaktionsTyp, Transaktionsloggare
import json
import os

class Bankomat:
    def __init__(self, lista_med_bankkonton,transaktionslog) -> None:
        self._transaktionslog = transaktionslog
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
                Bankomat.spara_transaktion(t,self._transaktionslog)
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
