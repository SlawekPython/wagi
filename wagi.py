import sys

package_weight = 0
package_number = 0
empty_box_weight = 0

for nr in range(int(sys.argv[1])):
    print("Dodaj element do paczki - waga musi być od 1 do 10 kg")
    element = float(input())

    if element < 1 or element > 10:
        print("Błędna wartość elementu")
        break
    elif element == 0:
        break

    elif package_weight + element <= 20:
        package_weight = package_weight + element
        #print(package_weight)

    elif package_number +=1
        empty_box_weight = 20 - package_weight

    else:
        empty_box_weight = empty_box_weight + empty_box_weight
        sum_sent_loaded_empty_kg = package_number * 20
        sum_of_empty_kg_sent = sum_sent_loaded_empty_kg - empty_box_weight

print(f"Liczba paczek wysłanych: {package_number}")
print(f"Suma kilogramów wyslanych: {package_weight}kg")
print(f"Sum of empty kilogram: {sum_of_empty_kg_sent}kg")

#print(f"Sum of empty kilograms: {sum_of_empty_kilograms}")