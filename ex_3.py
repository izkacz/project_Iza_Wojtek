# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci) -> [int, int]:
    liczba_studentow = [val for val in studenci if isinstance(val, str)]
    woman: int = 0
    man: int = 0
    for students in liczba_studentow:
        if students.split()[0].endswith("a"):
            woman += 1
        else:
            man += 1
    return [woman, man]
