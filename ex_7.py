# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def wykres(wykres) -> bool:
    def wykres(wykres) -> bool:
        a1 = (wykres[1][1] - wykres[0][1]) / (wykres[1][0] - wykres[0][0])
        a2 = (wykres[2][1] - wykres[0][1]) / (wykres[2][0] - wykres[0][0])
        if a1 == a2:
            wynik = True
        else:
            wynik = False
        return wynik
