#TASK ONE

def count_unique_values(lst):
    unique_values = set(lst)
    count = len(unique_values)
    return count

#we are making a list of random integer values
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 2, 2, 2]
result = count_unique_values(my_list)
print(f"Number of unique values: {result}")

#TASK TWO

def generate_square_dict(n):
    square_dict = {i: i*i for i in range(1, n+1)}
    return square_dict

#lets try this using tge number 5 
n = 5
result_dict = generate_square_dict(n)
print(result_dict)

#TASK THREE:
def sum_of_numbers(n):
    numbers = [int(input("Enter number: ")) for _ in range(n)]
    total_sum = sum(numbers)
    return total_sum

#in this one we consider n = 6
n = 6
result_sum = sum_of_numbers(n)
print(f"Sum of {n} numbers: {result_sum}")
