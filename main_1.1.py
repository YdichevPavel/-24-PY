numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

for i in range(0, len(numbers)-1):
    if numbers[i] == None:
        none_element = i

numbers.pop(none_element)

len_ = len(numbers)+1
sum_ = sum(numbers)
average = sum_/len_

numbers.insert(none_element, average)

print("Измененный список:", numbers)