user_input = input("Введите элементы списка через запятую: ")
source_list = user_input.replace("/", ",").replace(".", ",").replace(";", ",").replace(":", ",").split(",")

number_list = []

for item in source_list:
    number_list.append(int(item))

final_list = list(set(number_list))

result = ", ".join(map(str, final_list))
print(result)




