import random


numright = 0
numwrong = 0
round = 1
board = "|---------------------/-------------------|"
strings = ''
n = 0
po = 0
helpme = []


while True:
    round = round +1
    guess = int(input("what's your guess?: "))

    randnum = random.randint(1,10)
    #guess = randnum1à
    eval = guess - randnum
    #print(strings)


    if round <0:
        #board = strings |------------------/------------/---------|
        #                |--------------------/--------------------|
        #                |-----------------/---/-------------------|
        pass

    if eval == 0:
        for thing in board:
            print(thing)
            n = n+1
            
            if thing == '/':
                print(n)
                po = n
                pass

            elif thing != '/':
                helpme.append(thing)
                if po+10 == n:
                    if po != 0:
                        helpme.append('/')
                
            print(helpme)

    if eval > 0:

        for thing in board:
            n = n+1

            if po != 0:

                if n == po - eval:
                    helpme.append('/')

                else:
                    helpme.append(thing)

            else:
                if n == 23 - eval:
                    helpme.append('/')

                elif thing != '/':
                    helpme.append(thing)

                else:
                    helpme.append('-')

    if eval < 0:

        for thing in board:
            n = n+1

            if po != 0:

                if n == po - (eval*-1) :
                    helpme.append('/')

                else:
                    helpme.append(thing)

            else:

                if n == 23 - (eval*-1) :
                    helpme.append('/')

                elif thing != '/':
                    helpme.append(thing)

                else:
                    helpme.append('-')
    board = ''
    for bozo in helpme:
        board = board +bozo

    print(board, 'yes')

    helpme = []
    n = 0
