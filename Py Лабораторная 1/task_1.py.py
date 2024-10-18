numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]



prop = 4

sum_numbers = sum(numbers[:prop]) + sum(numbers[prop+1:])
col_numbers = len(numbers)
sr_numbers = (sum_numbers/col_numbers)

numbers[prop] = sr_numbers
print("Измененный список:", numbers)