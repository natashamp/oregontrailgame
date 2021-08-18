import random
health = 5
food = 500
miles = 2000
cday = 1
cmonth = 3
months31 = [3,5,7,8,10,12]
months30 = [4,6,9,11]
rdays = 0
dTrav = 0
danger1 = random.randint(1,15)
danger2 = random.randint(16,23)
devents = ['there is a bison herd crossing','you have cholera','you have dysentery','you have a fever','you have a snakebite','you have typhoid','you are hit with exhaustion','you broke your leg','you broke your arm']



def addDays(days):
        global food,health,cday, cmonth, months31, months30,food,danger1,danger2,devents,miles,dTrav
        cday +=days
        if cmonth in months31:
            if cday > 31:
                cmonth +=1
                cday -= 31
                danger1 = random.randint(1,15)
                danger2 = random.randint(16,23)
        else:
            if cday > 30:
                cmonth += 1
                cday -= 30
                danger1 = random.randint(1,15)
                danger2 = random.randint(16,23)
        food -=(5*days)
        if danger1 < cday:
            health -=1
            d=random.randint(0,3)
            print(devents[d])
            if d==0:
                   health -=2
            danger1=99
        if danger2 < cday:
           health -= 1
           danger2 = 99
           d = random.randint(0,3)
           print(devents[d])
           if d == 0:
                health -=2
                return addDays(days)
def hunta():
    global food
    global devents
    if devents == 'there is a bison herd crossing':
        food += 100
    else:
        print('unvalid choice')
        addDays(random.randint(2,5))
     

def miless():
    global miles
    g =  random.randint(30,60)
    addDays(random.randint(2,5))
    miles -= g
    

def daystrav():
    global dTrav
    h =  random.randint(30,60)
    dTrav += h
    addDays(random.randint(2,5))

def healtha():
    global health
    if health < 5:
        health += 1
        addDays(random.randint(2,5))


def events():
    global devents
    global health
    health -= 1
    import random
    print(devents[random.randint(0,9)])

def death():
    global health, food, dTrav
    if health == 0:
        game_over = True
        print('GAME OVER')

    elif food == 0:
        game_over = True
        print('GAME OVER')

    elif miles == 0:
        game_over = True
        print('YOU WIN')
        








name = input('what is you name?')
print(name, 'you have to get to Oregon by 12/31')
game_over = False
while not game_over:

    print(' ')
    print('health = ', health)
    print('food = ', food)
    print('miles = ', miles)
    print('distance traveled = ', dTrav)
    print('date = ', cmonth ,'/', cday)
    options = input('1:travel, 2:rest, 3:hunt, 4:status, 5:help, 6:quit')
          


    if options == '1':
        import random
        miless()
        daystrav()
        food -= 5
        
    elif options == '2':
        healtha()
        food -= 5
        
    elif options == '3':
        hunta()


    elif options == '4':
        pass

    elif options == '5':
        print('get help')

    elif options == '6':
        game_over = True
        print('GAME OVER')

    else:
        print('invalid choice')


        events()
        death()
        


