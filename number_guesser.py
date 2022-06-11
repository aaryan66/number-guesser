import random
print ('Welcome to the number guesser app')

secretnumber = random.uniform(0,10)
guess_count = 0
guess_limit = 5

while guess_count<guess_limit : 
    print("Number :")
    guess = int(input())
    