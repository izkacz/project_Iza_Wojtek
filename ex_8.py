# dla podanych dwoch punktow, oblicz, czy funkcja liniowa jest rozsnaca, czy malejaca
# dla niemalejacej zrwoc True
# dla malejacej zwroc False

def funkcja_liniowa(punkty) -> bool:
    a1 = (punkty[1][1] - punkty[0][1]) / (punkty[1][0] - punkty[0][0])
    if a1 >= 0:
        wynik = True
    else:
        wynik = False
    return wynik
