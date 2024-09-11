user_input1 = input("Введите элементы 1-го списка: ")
user_input2 = input("Введите элементы 2-го списка: ")

source_list1 = user_input1.replace("/", ",").replace(".", ",").replace(";", ",").replace(":", ",").split(",")
source_list2 = user_input2.replace("/", ",").replace(".", ",").replace(";", ",").replace(":", ",").split(",")

number_list1 = []

for item in source_list1:
    number_list1.append(int(item))

number_list2 = []

for item in source_list2:
    number_list2.append(int(item))

for i in number_list1:
    if i in number_list2:
        number_list1.remove(i)

result = ", ".join(map(str, number_list1))
print(result)

