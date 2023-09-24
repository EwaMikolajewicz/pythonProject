"""
Ćwiczenie nr 06.08:
Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu
w każdej krotce z podanej listy niepustych krotek.
Przykładowa lista: `[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]`
Oczekiwany wynik : `[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]`
Wskazówka:
* Napisz funkcję pomocniczą last(n), która zwróci ostatni element z podanej listy/krotki
* użyj pomocniczej funckji we wbudowanej funkcji `sorted()` przekazując ją jako parametr `key=last`
"""