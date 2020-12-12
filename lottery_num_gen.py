import random

randomList = []
# Set a length of the list to 5
for i in range(0, 5):
    # any random numbers from 0 to 1000
    randomList.append(random.randint(0, 69))

print("Here are your 5 Lottery numbers:")
print(randomList)

print('Here is your Powerball Number:')
print(random.randint(1,26))