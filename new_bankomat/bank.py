from bankkonto import Bankkonto, NegativtNummerError
from tansaktion import Transaktion, TransaktionsTyp, Transaktionsloggare
from enum import Enum

class Bankmeddelande(Enum):
    OK = 1
    KONTO_FINNS_REDAN = 2
    KONTO_FINNS_INTE = 3
    INTE_TILLRÄCKLIGT_SALDO = 4
    INTE_ETT_TAL = 5
    

class Bank:
    def __init__(self, transaktionsfil:str, transaktionslogger:Transaktionsloggare) -> None:
        self._bankkonton:dict[str,Bankkonto] = {}
        self._transaktionsfil = transaktionsfil
        self._transaktionslogger = transaktionslogger

    def _lägg_till_nytt_konto(self, konto:Bankkonto) -> None:
        self._bankkonton[konto.hämta_kontonummer()] = konto

    def _ta_bort_konto(self, kontonummer:int) -> Bankmeddelande:
        
        if self.kolla_om_konto_redan_finns(kontonummer):
            bankkonto_att_ta_bort = self._bankkonton.pop(kontonummer)
            del bankkonto_att_ta_bort
            return Bankmeddelande(1)
        else:
            return Bankmeddelande(3)

    def skapa_nytt_konto(self, kontonummer:int) -> Bankmeddelande:

        if self.kolla_om_konto_redan_finns(kontonummer):
            return Bankmeddelande(2)
        else:
            nytt_bankkonto = Bankkonto(kontonummer)
            self._lägg_till_nytt_konto(nytt_bankkonto)

            return Bankmeddelande(1)
        
    def avsluta_konto(self, kontonummer:int) -> Bankmeddelande:
        pass
        
    def hämta_saldo_från_konto(self, kontonummer:int) -> int|Bankmeddelande:

        if kontonummer in self._bankkonton:
            return self._bankkonton[kontonummer].hämta_saldo()
        else:
            return Bankmeddelande(3)
        
    def kolla_om_konto_redan_finns(self,kontonummer:int) -> bool:
        return True if kontonummer in self._bankkonton else False
    
    def sätt_in_pengar_på_konto(self,summa:int, kontonummer:int) -> Bankmeddelande:

        if not self.kolla_om_konto_redan_finns(kontonummer): return Bankmeddelande(3) 
        
        try:
            self._bankkonton[kontonummer].insättning(summa)
        except NegativtNummerError as e:
            print(f'Ett fel har inträffat: {e}')
        except TypeError as e:
            print(f'Otillåten typ: {e}')
        else:
            return Bankmeddelande(1)


    def ta_ut_pengar_från_konto(self, summa:int, kontonummer:int) -> Bankmeddelande:
        
        if not self.kolla_om_konto_redan_finns(kontonummer): return Bankmeddelande(3)

        try:
            lyckades = self._bankkonton[kontonummer].uttag(summa)
        except NegativtNummerError as e:
            print(f'Ett fel har inträffat: {e}')
        except TypeError as e:
            print(f'Otillåten typ: {e}')
        else:
            if lyckades:
                return Bankmeddelande(1)
            else:
                return Bankmeddelande(4)