even_numbers = []
odd_numbers = []
for i in range(1, 100):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print('even', even_numbers, '\n')
print('odd', odd_numbers)