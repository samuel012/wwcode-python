''' List Exercise 4 

Suppose you and your friend Sally goes to the supermarket. You have the following items on your shopping list:
   tomatoes, carrots, beans, milk, cabbage, corn, papaya, orange
Sally has the following on her list:
   milk, tacos, cabbage, fish, beans, tuna, corn, pasta

You and Sally decide to accomplish grocery shopping together.

1. Write a program that outputs a new shopping list containing both of your lists, without the repeated entries, in alphabetical order
'''

makeshift_horizontal_rule = '-' * 50

print(f"\n{makeshift_horizontal_rule}\nQuestion 1\n")

# your solution here
my_list = ['tomatoes', 'carrots', 'beans', 'milk', 'cabbage', 'corn', 'papaya', 'orange']
sallys_list = ['milk', 'tacos', 'cabbage', 'fish', 'beans', 'tuna', 'corn', 'pasta']

set_items = set(my_list)
set_items.update(sallys_list)
sorted_unique_list = sorted(set_items)
print(f"Our joint shopping list: {sorted_unique_list}")


'''
While shopping, you bumped into your friend Kris. Kris saw your list, and advised you not to get the fifth item as they ran out already.
A little while later, your other friend Nat called and asked you to get peanut butter and ice cream

2. Output the item that ran out, and your updated groceries list which includes Nat's, in alphabetical order
'''

# your solution here
print(f"\n{makeshift_horizontal_rule}\nQuestion 2\n")
print(f"Fifth item that already ran out: {sorted_unique_list[4]}")

sorted_unique_list.extend(('peanut butter', 'ice cream'))
sorted_unique_list.sort()
print(f"Updated list: {sorted_unique_list}")


'''
You were finally heading to the checkout counters; however, you noticed that the lines were too long. You and Sally decided to split the
groceries alternatively, with you lining up with the first item, Sally the second item, you the third, and so on.

3. Output your final list, and output Sally's list
'''


# your solution here
print(f"\n{makeshift_horizontal_rule}\nQuestion 3\n")
print(f"My final list: {sorted_unique_list[::2]}")
print(f"Sally's final list: {sorted_unique_list[1::2]}")