"'@version 1.2 @author Shrey'"
""'create method to calculate the median for modularity "'
"'Used method call in the prinitng statement '"

def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        return numbers[int(len(numbers)/2)]
    else:
        index = int(len(numbers)/2)
        return (numbers[index-1]+numbers[index])/2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(f"The median is : {median(numbers)}")
