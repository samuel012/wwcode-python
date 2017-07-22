""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

"""
>> How much is your total bill? 150
>> How much is your payment? 200
>> Hi! Your change is 50.00
"""

total_bill = input('How much is your total bill? ')
payment = input('How much is your payment? ')
change = float(payment) - float(total_bill)

print('Hi! Your change is {:.2f}'.format(change))