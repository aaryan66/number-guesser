from cmath import e
import random
print("""Welcome to the number game app
Here we you need to choose a secret
number which is between 1 - 10 and you
will get only 3 chances""");

#secret number
secret_number = int(random.uniform(0,10))
guess_count = 0
guess_limit = 3


while guess_count<guess_limit:
   guess = int(input("Number : "))
   guess_count  += 1
   if guess == secret_number:
    print("Congratulations you won")
    break 
else : 
    print ("sorry you failed")
    print (f"The real answer was {secret_number}")


