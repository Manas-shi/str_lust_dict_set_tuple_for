number_of_elements = int(input("Введите количество элементов в списке: "))

element_list = []

for element in range(number_of_elements):
    user_input = int(input(f"Введите элемент {element + 1}: "))
    element_list.append(user_input)

sorted_list = sorted(element_list)

print(sorted_list)