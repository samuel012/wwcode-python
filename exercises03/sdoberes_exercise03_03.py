''' List Exercise 3
Write a program that accepts a series of numbers, outputs all odd numbers in a list in ascending order, 
and all even numbers in a list in descending order.
Sample Input: 1,2,35,45,7,8,912,23,1
Sample Output: [1, 1, 7, 23, 35, 45] # odd
               [912, 8, 2] # even
'''

comma_delimited_string = input('Sample Input: ')
even_numbers = []
odd_numbers = []
iterable_map = map(int, comma_delimited_string.split(','))

for num in iterable_map:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

odd_numbers.sort()
print(odd_numbers)

even_numbers.sort(reverse=True)
print(even_numbers)