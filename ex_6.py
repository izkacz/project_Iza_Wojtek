# sprawdz, czy nawias ma swoja pare, jesli ma swroc True, jesli nie False

def para_nawiasow(tekst: str) -> bool:
    liczba_nawiasow_otwierajacych = tekst.count("(")
    liczba_nawiasow_zamykajacych = tekst.count(")")
    if liczba_nawiasow_otwierajacych == liczba_nawiasow_zamykajacych:
        wynik = True
    else:
        wynik = False
    return wynik
