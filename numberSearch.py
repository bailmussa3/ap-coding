numbers = [1, 5, 10, 20, 39, 48, 83, 89, 72, 90]
max_number = numbers[0]
for number in numbers:
  # 3. Compare and update if a larger number is found
  if number > max_number:
    max_number = number
print(f"The largest number in the list is: {max_number}")

Smallest= find_smallest_number 