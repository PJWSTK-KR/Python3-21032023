def find_min(numbers = []):
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]
    min_number = numbers[0]
    for number in numbers[1:len(numbers)]:
        if int(number) < int(min_number):
            min_number = number
    return min_number


def find_max(numbers = []):
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]
    max_number = numbers[0]
    for number in numbers[1:len(numbers)]:
        if int(number) > int(max_number):
            max_number = number
    return max_number


numbers = input("liczby >")
numbers = numbers.split(",")
print("min=" + find_min(numbers))
print("max=" + find_max(numbers))
