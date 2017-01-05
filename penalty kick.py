import random

score = [0,0]
round = 0

def shoot():
    direction = ['left','middle','right']
    print ('choose a direction to shoot……')
    print ('left,middle,right')
    you = raw_input()
    while you not in direction:
        print ('please choose the target on the gate……')
        you = raw_input()
    if you in direction:
        print ('you shoot "%s"'  %you)
        com = random.choice(direction)
        print ('the computer saved "%s"' %com)
        if you != com:
            score[0] += 1
            print ('GOAL!')
        else:
            print ('be saved……')
        print ('%d(you) : %d(com)' %(score[0],score[1]) )

def save():
    direction = ['left','middle','right']
    print ('choose a direction to save……')
    print ('left,middle,right')
    you = raw_input()
    while you not in direction:
        print ('please choose the right direction to save……')
        you = raw_input()
    if you in direction:
        print ('you saved "%s"'  %you)
        com = random.choice(direction)
        print ('the computer shooted "%s"' %com)
        if you != com:
            score[1] += 1
            print ('GOAL!')
        else:
            print ('be saved……')
        print ('%d(you) : %d(com)' %(score[0],score[1]) )

while 1 == 1:
    round += 1
    print ('ROUND %d' %round)
    print('your turn...')
    shoot()
    print("computer's turn...")
    save()
    if round == 5:
        if score[0]>score[1]:
            print('YOU WIN!!The final score is %d : %d' %(score[0],score[1]))
            break
        elif score[0]<score[1]:
            print('COMPUTER WIN!!The final score is %d : %d' %(score[0],score[1]))
            break
        else:
            continue
    elif round > 5:
        if score[0]>score[1]:
            print('YOU WIN!!The final score is %d : %d' %(score[0],score[1]))
            break
        elif score[0]<score[1]:
            print('COMPUTER WIN!!The final score is %d : %d' %(score[0],score[1]))
            break
        else:
            continue
    else:
        continue
