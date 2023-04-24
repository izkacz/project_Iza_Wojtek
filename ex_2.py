def policz_studentow(studenci) -> int:
    liczba_studentow = len([val for val in studenci if isinstance(val, str)])
    return liczba_studentow
