# Oblicz liczbę nawiasów w zmiennej, zwroc: [otwierajace, zamykajace]

def nawiasy(tekst: str) -> [int, int]:
    liczba_nawiasow_otwierajacych = tekst.count("(") + tekst.count("{") + tekst.count("[")
    liczba_nawiasow_zamykajacych = tekst.count(")") + tekst.count("}") + tekst.count("]")
    return [liczba_nawiasow_otwierajacych, liczba_nawiasow_zamykajacych]
