# Projekt SM

## Opis projektu
Projekt zakłada sterowanie obrotami silnika po przez sterownik PID realizowanego za pomocą modułu NUCLEO F746ZG.  
Wartość prędkości zadanej ustawiamy za pomocą enkodera lub za pośrednictwem programu wykonanego w języku phyton. Następnie moduł nukleo nastawia sterowanie na silnik by kręcił się z zadaną prędkością.  
Pomiar prędkości silnika realizowany jest po przez pomiar wzrostów rezystancji na fotorezystorze spowodowany przysłonięciem diody umieszczonej za silnikiem co jeden obrót. Dodaliśmy również funkcjonalność opserwacji pracy silnika na wykresie w czasie rzeczywistym w programie w języku phyton.  
Silnik wyposarzony jest w śmigło, które skonstrułowane jest tak by tylko raz na obrót było w stanie zasłonić diodę. Jest to nasza pętla ujemnego sprzężenia zwrotnego.
	
## Komponenty projektu
* Moduł NUCLEO F746 ZG
* Silnik 3C146312
* Enkoder z przyciskiem - Iduino SE055
* Tranzystor S9013
* Fotorezystor
* Bateria 9V
* Dioda, 3 rezystory, przełącznik
* Moduł zasilający MB102
* Powerbank
