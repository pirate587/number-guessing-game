import random
number = random.randint(1,100)

def start():
    print("hY! your name please:")
    name = input()
    print("so "+name+" i am going to think of a number in between 1 to 100 you have to guess it!")
    print("hmmm")
    print("come on guess")
def pick():
    cnt = 0

    while cnt < 6:
        cnt = cnt+1
        inp = int(input("your guess:"))
        try:
            guess = inp
            if guess <= 100 and guess >=1:
                if cnt < 6:
                    if guess > number:
                      print("Too high!")
                    if guess < number:
                      print("Too low")
                    if guess != number:
                      print("Sorry ! wrong guess")
                if guess == number:
                    break
            if guess>100 or guess <1:
                print("Wrong number , enter your guess between 1 to 100")
        except:
            print("that's not a number ")


    if  guess == number:
        print("Wow champ! you got it right")
    if guess!= number:
        print("nope i was thinking of"+str(number))

playagain = "yes"
while playagain == "yes" or playagain == "Yes" or playagain == "Y" :
    start()
    pick()
    print("gonna play again?")
    playagain = input()






