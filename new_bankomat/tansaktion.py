from enum import Enum

class TransaktionsTyp(Enum):
    INSÄTTNING = 1
    UTTAG = 2
    SKAPAD = 3
    AVSLUTAD = 4

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

class Transaktionsloggare:
    pass