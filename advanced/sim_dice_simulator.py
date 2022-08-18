import random

while True:
    input('enter to roll dice🎲')
    roll = random.randint(1, 6)
    print('print you rolled dice and get 🎲:',roll)
    if roll == 1: 
        print('💀You Lose!💀')
        break
    elif roll == 6 :
        print('👑You Win👑')
        break
    else:
        print ('keep rolling....')