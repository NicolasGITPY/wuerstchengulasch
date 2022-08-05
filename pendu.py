'''
--|-----|-
  |     0
  |    \|/
  |    / \
__|________  
'''
import random

mots = open("dict.txt")

zal = 0

worterlist = []

lang = input('Welche sprache?(FR,DE,EN): ')

if lang.lower() == 'fr':
    for i in open("dict_FR.txt", "r"):

        zal = zal+1

        if len(i)-1 >40:
            pass
        
        else:
            worterlist.append(i)

if lang.lower() == 'de':
    for i in open("dict_DE.txt", "r"):

        if len(i)-1 < 3:
            pass

        if len(i)-1 >40:
            pass

        else:
            zal = zal+1
            worterlist.append(i)

if lang.lower() == 'en':
    for i in open("dict_EN.txt", "r"):

        if len(i)-1 < 3:
            pass

        if len(i)-1 >40:
            pass

        else:
            zal = zal+1
            worterlist.append(i)

wpos = random.randrange(0, zal)

reponse = worterlist[wpos]
reponse_liste = []
liste_dessays = []
empty_str = ""
letter_pos =[]
cj = 0

bruuuuh = []

print(len(reponse)-1)

lettres = { '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ', '10': ' ', '11': ' ', '12': ' ', '13': ' ', '14': ' ', '15': ' ', '16': ' ', '17': ' ', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ', '24': ' ', '25': ' ', '26': ' ', '27': ' ', '28': ' ', '29': ' ', '30': ' ', '31': ' ', '32': ' ', '33': ' ', '34': ' ', '35': ' ', '36': ' ', '37': ' ', '38': ' ', '39': ' ', '40': ' ',}

n_fautes = 0
n_trouves = 0

for lettre in reponse:
    reponse_liste.append(lettre)

pondu = {
    '0': '____________', '1': '__|_________', '2': '  |', '3': '  |', '4': '  |', '5': '--|------|- ', '6': '      0', '7': '     \|/', '8': '     / \ ',
}

def Le_pondu(pondu):

    if n_fautes == 1:
        print(pondu['0'])
        print(' ')
        print(lettres_trouves)

    elif n_fautes == 2:
        print(pondu["4"])
        print(pondu["3"])
        print(pondu["2"])
        print(pondu['1'])
        print(' ')
        print(lettres_trouves)

    elif n_fautes == 3:
        print(pondu["5"])
        print(pondu["4"])
        print(pondu["3"])
        print(pondu["2"])
        print(pondu['1'])
        print(' ')
        print(lettres_trouves)

    elif n_fautes == 4:
        print(pondu["5"])
        print(pondu["4"] + pondu['6'])
        print(pondu["3"])
        print(pondu["2"])
        print(pondu['1'])
        print(' ')
        print(lettres_trouves)

    elif n_fautes == 5:
        print(pondu["5"])
        print(pondu["4"] + pondu['6'])
        print(pondu["3"] + pondu['7'])
        print(pondu["2"])
        print(pondu['1'])
        print(' ')
        print(lettres_trouves)

    elif n_fautes == 6:
        print(pondu["5"])
        print(pondu["4"] + pondu['6'])
        print(pondu["3"] + pondu['7'])
        print(pondu["2"] + pondu['8'])
        print(pondu['1'])
        print(' ')
        print(lettres_trouves)

while True:
    essay = input('Devinez une lettre: ')

    if essay in liste_dessays:
        print('Tu as déja deviné cette lettre!')
        
    else:
        
        '''for letter in range(len(reponse)-1):
            print(letter)
            cj = cj+1

            if letter != " ":
                empty_str = empty_str + "_"

            else:
                pass

        print(empty_str)'''

        for i in range(len(reponse)-1):

            if essay == reponse_liste[i]:
                lettres[f'{i+1}'] = essay
                n_trouves = n_trouves+1
            
            elif lettres[f'{i+1}'] == ' ':
                lettres[f'{i+1}'] = '_'

        lettres_trouves = (lettres['1'] + lettres['2'] + lettres['3'] + lettres['4'] + lettres['5'] + lettres['6'] + lettres['7'] + lettres['8'] + 
                            lettres['9'] + lettres['10'] + lettres['11'] + lettres['12'] + lettres['13']+lettres['14'] + lettres['15'] + lettres['16'] + lettres['17'] 
                            + lettres['18'] + lettres['19'] + lettres['20'] + lettres['21'] +lettres['22'] + lettres['23'] + lettres['24'] + lettres['25'])

        if essay in reponse:
            print('\n'+lettres_trouves+'\n')
            liste_dessays.append(essay)

        elif essay not in reponse_liste:
            n_fautes = n_fautes+1
            print(' ')
            Le_pondu(pondu)
            print(' ')
            print('Faux!\n')
            liste_dessays.append(essay)

    print(liste_dessays)

    if n_fautes == 6:
        Le_pondu(pondu)
        print('Perdu!')
        print(reponse)
        break

    elif n_trouves == len(reponse)-1:
        Le_pondu(pondu)
        print('Gagné!')
        break
