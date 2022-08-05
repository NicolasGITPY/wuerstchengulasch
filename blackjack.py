#blackjack
import random
import re

hand = [':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,']
turn = 0

#cardgen
def shuffle(turn, hand):
    while True:
        cardnumber = random.randint(1,13)

        if cardnumber > 10:
            match cardnumber:
                case 11:
                    hand[turn] = 'B'
                case 12:
                    hand[turn] = 'D'
                case 13:
                    hand[turn] = 'K'

        elif cardnumber == 1:
            hand[turn] = 'A'

        else:
            hand[turn] = f'{cardnumber}'

        #print(hand)

        #cardcolor

        cardcolor = random.randint(1,4)

        match cardcolor:
                case 1:
                    hand[turn] = hand[turn]+' herz'
                case 2:
                    hand[turn] = hand[turn]+' pic'
                case 3:
                    hand[turn] = hand[turn]+' caro'  
                case 4:
                    hand[turn] = hand[turn]+' clee' 

        #print(hand)
        
        redundant = 0

        if hand[turn] in hand:
            for cards in hand:
                if cards == hand[turn]:
                    redundant = redundant+1
        
        if redundant > 1:
            hand.remove(hand[turn])
            hand.append('')
            #print(turn)

        if redundant == 1:
            turn = turn +1

        if turn == 52:
            break

#print(hand)

carten = hand
cardsleft = 51

#pick random card
def randomcard(cardsleft, carten):
    randomcardnumber = random.randint(1, cardsleft)

    cardpicked = carten[randomcardnumber]
    carten.pop(randomcardnumber)
    cardsleft = cardsleft -1 
    return cardpicked

def cardvalues(carte, cardvalue):

    cardchars = ''
    cardchars = carte.split(' ')
    value = 0

    match cardchars[0]:
        case '1':
            value = 1
        case '2':
            value = 2
        case '3':
            value = 3
        case '4':
            value = 4
        case '5':
            value = 5
        case '6':
            value = 6
        case '7':
            value = 7
        case '8':
            value = 8
        case '9':
            value = 9
        case '10':
            value = 10
        case 'B':
            value = 10
        case 'D':
            value = 10
        case 'K':
            value = 10
        case 'A':
            if cardvalue > 21:
                value = 1
            else:
                value = 11
    
    return value

while True:
    shuffle(turn, hand)
    #print(hand)
    playerhand = ['','','','','','','','','','']
    dealerhand = ['','','','','','','','','','']
    round = 0

    n = 0
    handvalue = 0
    dealerhandvalue = 0
    balance = 0

    while True:

        if round == 0:
            wordup = open('bank.txt', 'r')
            bet = int(input('Einsatz: '))

            for text in wordup:
                balance  = balance +int(text)


            print(balance)

            balance = balance - bet

        if round >= 2:
            
            playerhand[round] = playerhand[round] + randomcard(cardsleft, carten)
            cardsleft = cardsleft -1 

        else:
            playerhand[round] = playerhand[round] + randomcard(cardsleft, carten)
            cardsleft = cardsleft -1 
            dealerhand[round] = dealerhand[round] + randomcard(cardsleft, carten)
            cardsleft = cardsleft -1 

        bingbong = 0

        round = round + 1

        if round == 2:

            while True:
                pämperäm = 0
                bingbong = bingbong + 1

                for i in range(10):
                    pämperäm = pämperäm+cardvalues(dealerhand[i], dealerhandvalue)
                
                if pämperäm < 17:
                    dealerhand[round+bingbong] = dealerhand[round+ bingbong] + randomcard(cardsleft, carten)
                    cardsleft = cardsleft -1 

                elif pämperäm >= 17:
                    break



        handvalue = 0
        n = 0

        for cartenens in playerhand:
            #print(cardvalues(playerhand[n]))
            handvalue = handvalue + cardvalues(playerhand[n], handvalue)

            if handvalue == 21:

                if cardvalues(playerhand[2], handvalue) == 0:
                    print('Blackjack!!!')

            if cardvalues(playerhand[n], handvalue) == 0:
                break

            n = n+1

        print(f'Punktzahl: {handvalue}')
        print(f'Carten: {playerhand}')
        print(f'Dealercarte n1: {dealerhand[0]}')

        if round >= 2:

            keeplayin = input('Noch ne carte?: ')

            if keeplayin == 'n':
                for i in range(10):
                #print(cardvalues(playerhand[n]))
                    dealerhandvalue = dealerhandvalue + cardvalues(dealerhand[i], dealerhandvalue)

                if handvalue == 21:

                    if cardvalues(playerhand[2], handvalue) == 0:
                        print('Blackjack!!!')
                        balance = balance + 3*bet
                        break

                if dealerhandvalue > handvalue:
                    if dealerhandvalue <= 21:
                        print('Dealer won!')
                        break
                    if handvalue > 21:
                        print('Draw!')
                        balance = balance + bet
                        break
                    else:
                        print('Player won!')
                        balance = balance + 2*bet
                        break

                elif dealerhandvalue < handvalue:
                    if handvalue <= 21:
                        print('Player won!')
                        balance = balance + 2*bet
                        break
                    if dealerhandvalue > 21:
                        print('Draw!')
                        balance = balance + bet
                        break
                    else:
                        print('Dealer won!')
                        break

                elif dealerhandvalue == handvalue:
                    print('Draw!')
                    balance = balance + bet
                    break

                break

            if handvalue > 21:
                if dealerhandvalue > 21:
                    print('draw')
                    balance = balance + bet
                else:
                    print('You lost !')
                break

    print(playerhand)
    print(handvalue)
    print(dealerhand)
    print(dealerhandvalue)
    print(balance)

    with open('bank.txt', 'w') as f:
        f.write(f'{balance}')
    
    again = input('Nochmal?: ')
    if again == 'y':
        hand = [':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,',':,,']
        turn = 0
        cardsleft = 51
        pass
    else:
        break