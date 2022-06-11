import random
print ('Welcome to the number guesser app')

secretnumber = random.uniform(0,10)
guess_count = 0
guess_limit = 5

while guess_count<guess_limit : 
    print("Number :")
    guess = int(input())
    guess_count +=1
    if guess == secretnumber : 
        print('You won')
        break
    else  :
        print('You lost try again')
        print(f"The real answer was {secretnumber}")