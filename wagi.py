import sys

#Napisz program do obsługi ładowarki paczek. Każda paczka może maksymalnie zmieścić 20 kg towaru.
# Do paczki dodawane są elementy. Każdy z nich może ważyć od 1 do 10 kg.
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg,
# paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), a bieżący element powinien zostać dodany do nowej paczki.
#Wszystkie elementy powinny zostać wysłane.
#Program powinien pobierać maksymalną liczbę elementów do wysyłki.
# Jeśli podano element o wadze 0, program powinien zakończyć działanie, tak jakby maksymalna liczba paczek została osiągnięta.
#Na koniec działania program powinien wyświetlić w podsumowaniu:

#Liczbę paczek wysłanych
#Liczbę kilogramów wysłanych
#Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
#Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
#Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.

package_weight = 0
package_number = 0

for nr in range(int(sys.argv[1])):
    print("Dodaj element do paczki - waga musi być od 1kg do 10 kg")
    element = float(input())
    if element == 0 or element < 1 or element > 10:
        break
    if package_weight + element <= 20:
        package_weight = package_weight + element
    else:
        package_number +=1

print(f"Liczba paczek wysłanych: {package_number}")
print(f"Package weight: {package_weight}kg")
#print("Suma \"pustych" - kilogramów")