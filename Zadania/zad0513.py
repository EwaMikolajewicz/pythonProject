"""
Napisz program, który wydrukuje następujący wzór liczbowy za pomocą pętli.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Wskazówka:
    Określ liczbę wierszy, tj. 5, ponieważ wzór zawiera pięć wierszy
    Uruchom zewnętrzną pętlę 5 razy, używając pętli for i funkcji range()
    Uruchom wewnętrzną pętlę i+1 razy używając pętli for i funkcji range()
        W pierwszej iteracji pętli zewnętrznej pętla wewnętrzna wykona 1 raz
        W drugiej iteracji pętli zewnętrznej pętla wewnętrzna wykona 2 razy
        W trzeciej iteracji zewnętrznej pętli pętla wewnętrzna zostanie wykonana 3 razy i tak dalej aż do rzędu 5
    Wypisz wartość j w każdej iteracji pętli wewnętrznej (j jest zmienną iteratora pętli wewnętrznej)
    Wyświetlaj pustą linię na końcu każdej iteracji zewnętrznej pętli (pusta linia po każdym wierszu)
"""