import sys

package_weight = 0
package_number = 0
max_empty_box_weight = 0
max_empty_box_nr = 0
sum_weight = 0

for nr in range(int(sys.argv[1])):
    print("Dodaj element do paczki - waga musi być od 1 do 10 kg")
    element = float(input())

    if element == 0:
        break
    elif element < 1 or element > 10:
        print("Błędna wartość elementu")
        break
    sum_weight = sum_weight + element
    if package_weight + element <= 20:
        package_weight = package_weight + element

    else:
        package_number +=1
        print(f"paczka numer: {package_number} waży {package_weight}")
        empty_box_weight = 20 - package_weight
        if empty_box_weight > max_empty_box_weight:
            max_empty_box_weight = empty_box_weight
            max_empty_box_nr = package_number

        print(f"puste kilogramy w paczce numer {package_number} {empty_box_weight}")

if package_weight > 0:
    package_number +=1
    empty_box_weight = 20 - package_weight
    if empty_box_weight > max_empty_box_weight:
        max_empty_box_weight = empty_box_weight
        max_empty_box_nr = package_number

sum_sent_loaded_empty_kg = package_number * 20
sum_of_empty_kg_sent = sum_sent_loaded_empty_kg - sum_weight

print(f"Liczba paczek wysłanych: {package_number}")
print(f"Suma kilogramów wyslanych: {package_weight}kg")
print(f"Sum of empty kilogram: {sum_of_empty_kg_sent}kg")
print(f"Paczka z największo liczbą pustych kg: {max_empty_box_nr}")
