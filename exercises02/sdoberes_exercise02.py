""" Aling Nena's Reward System Challenge
Author:
Description: This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s
Sari-sari store.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]

input_text = input('Please enter text: ')

input_array = input_text.split()
reward_number = int(input_array[0])
first_name = input_array[1]
middle_name = input_array[2]
last_name = input_array[3]
gender = input_array[4]

sentence1 = f'Hi {first_name.title()} {middle_name.title()}. {last_name.title()}! '
sentence2 = f'You have successfully redeemed reward #{reward_number} - {rewards[reward_number - 1]}! Thank you for choosing Aling Nena\'s Sari-sari store.'
print(sentence1 + sentence2)
