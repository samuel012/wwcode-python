''' Lists Exercise 2: Working list '''

makeshift_horizontal_rule = '-' * 50

# Make a list that includes four careers, such as 'programmer', 'truck driver', etc....
careers = ['programmer', 'project manager', 'scrum master', 'technical architect']


# Use the list.index() function to find the index of one career in your list.
print(f"The index of the career 'technical architect' is {careers.index('technical architect')}\n{makeshift_horizontal_rule}")


# Use the in function to show that this career is in your list.
careers_to_check = ['fireman', 'programmer']
for random_career in careers_to_check:
    in_or_not_in_list = 'in my list' if random_career in careers else 'not in my list'
    print(f"The career '{random_career}' is {in_or_not_in_list}.")
print(f"{makeshift_horizontal_rule}")


# Use the append() function to add a new career to your list.
careers.append('business analyst')
print(careers)
print(f"{makeshift_horizontal_rule}")


# Use the insert() function to add a new career at the beginning of the list.
careers.insert(0, 'software tester')


# Use a loop to show all the careers in your list.
for idx, career in enumerate(careers):
    print(f"Career #{idx + 1}: {career}")