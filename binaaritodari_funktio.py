"""
 binaaritodari_funktio.py
 Matias Kaakinen, matias.kaakinen@tuni.fi
 Syksy 2019
"""

from numpy import math
from decimal import Decimal

def x_yli_yn(nopat, määrä):
    x_yli_yn = math.factorial(nopat) // (math.factorial(määrä) * math.factorial(nopat - määrä))
    return x_yli_yn

def binääritodari(kerroin, määrä, nopat):
    """Laskee binäärijakaumaa käyttäen todennäköisyyden saada annettu määrä
    tiettyjä silmälukuja annetulla määrällä noppia. Ohjelma puhuu kuutosista,
    mutta vastaava toimii mille tahansa tietylle silmälukujen joukolle (esim. 1,6
    tai 1,1 tai 1,2,3). Ohjelmassa lukujen järjestyksellä ei ole väliä.
    nopat - käyttäjän valitsema määrä noppia
    määrä - käyttäjän valitseman silmälukujen joukon laajuus
    """
    binääritodari = kerroin * ((1 / 6) ** määrä) * ((5 / 6) ** (nopat - määrä))
    print(str(round(binääritodari * 100, 1)) + "%")

def kertymä_(kerroin, määrä, nopat):
    for luku in range(1,määrä+1):
        binääritodari(kerroin, luku, nopat)
        return kertymä_

def main():
    nopat = int(input())
    määrä = int(input())
    kerroin = x_yli_yn(nopat, määrä)
    piste = binääritodari(kerroin, määrä, nopat)
    kertymä_(kerroin, määrä, nopat)
    print(kertymä_)
      
if __name__ == "__main__":
    main()