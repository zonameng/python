import random
def anwer(AnwerNumber):
    if AnwerNumber == 1:
        return 'It is 1 !'
    elif AnwerNumber == 2:
        return 'It is 2 !'
    elif AnwerNumber == 3:
        return 'It is 3 !'
r = random.randint(1,3) 
getanwer = anwer(r)
print(getanwer)