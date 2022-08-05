from numToLetter import transformer
#NOTE mehr wörtebücher(mehr sprachen), funktioniert jetzt, benötigte dateien: numToLetter.py, dict_EN.txt, dict_DE.txt, dict_FR.txt
worter = open('dict.txt')

worterlist = []

guesslist = []
guesslist1 = []
guesslist2 = []
guesslist3 = []
guesslist4 = []
guesslist5 = []
guesslist6 = []
guesslist7 = []

alphabet = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,'12': 0, '13': 0,'14': 0,
                '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0,'24': 0, '25': 0,'26': 0,'27': 0,'28': 0,'29': 0,}

gudGuess = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ', '10': ' ', '11': ' ','12': ' ', '13': ' ','14': ' ',
                    '15': ' ', '16': ' ', '17': ' ', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ','24': ' ', '25': ' '}

lang = input('Welche sprache?(FR,DE,EN): ')
print(lang)

if lang.lower() == 'fr':
    for i in open("dict_FR.txt", "r"):
        if len(i)-1 >25:
            pass

        else:
            worterlist.append(i)

if lang.lower() == 'de':
    for i in open("dict_DE.txt", "r"):

        if len(i)-1 < 3:
            pass

        if len(i)-1 >25:
            pass

        else:
            worterlist.append(i)

if lang.lower() == 'en':

    for i in open("dict_EN.txt", "r"):

        if len(i)-1 < 3:
            pass

        if len(i)-1 >25:
            pass

        else:
            worterlist.append(i)

lenword = int(input('Wörterlänge: '))

wrongGuess = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ', '10': ' ', '11': ' ','12': ' ', '13': ' ','14': ' ',
                '15': ' ', '16': ' ', '17': ' ', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ','24': ' ', '25': ' '}

f = 0
i = 0
n = 0
z = 0
x = 0
a = 0

new_W_Letter = False
new_T_Letter = False

isImposter = False
sus = 1

guesses = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,'12': 0, '13': 0,'14': 0}

while True:

    while True:
        getGuess = str(input('Buchstaben die nicht funktioniert haben (end): '))

        if getGuess == 'end':
            break

        else:
            n = n+1
            new_W_Letter = True
            wrongGuess[f'{n}'] = getGuess

    while True:
        getGud = str(input('Buchstaben die funktioniert haben (end): '))

        if getGud == 'end':
            break

        if getGud != 'end':
            i = i+1
            new_T_Letter = True
            gudGuess[f'{i}'] = getGud
            guesslist5.append(getGud)


    if a==0:
        a = a+1

        for word in worterlist:

            if len(word) == lenword+1:
                guesslist.append(word)

    guesslist1 = []

    for wort1 in guesslist:

        if not new_W_Letter:
            guesslist1 = guesslist
            break

        if new_W_Letter:

            for o in range(n):
                
                if wrongGuess[f'{o+1}'] not in wort1:
                    if wrongGuess[f'{o+2}'] == ' ':
                        guesslist1.append(wort1)

                elif wrongGuess[f'{o+1}'] in wort1:
                    break 
        else: 
            break
    
    if i == 0:
        guesslist4 = guesslist1

    #etranger
    # liste 1 leert sich wenn liste 2 geleert wird >:( FIXED (nicht .clear() benutzen)
    # liste 2 ist voll obwohl l.295 geleert wurde FIXED (nicht .clear() benutzen und leeren mit = [])

    guesslist2 = []

    for wort2 in guesslist1:

        if not new_T_Letter:
            guesslist2 = guesslist1
            break
        
        if new_T_Letter:

            for m in range(i):
                m = m+1

                if gudGuess[f'{m}'] in wort2:

                    if gudGuess[f'{m+1}'] == ' ':
                        guesslist2.append(wort2)
                        x = 0
                        break

                elif gudGuess[f'{m}'] not in wort2:
                    x = 0
                    break

    guesslist4 = []

    while f<i:
        f = f+1

        if new_T_Letter:
            if gudGuess[f'{f}'] != ' ':
                guesses[f'{f}']= int(input(f'Der wievielte buchstabe ist '+gudGuess[f'{f}']+' in dem wort?: '))

    for wort3 in guesslist2:

        if isImposter == False:

            for letter in wort3:
                if letter != '\n':
                    guesslist3.append(''+letter+'')

                elif letter == '\n':
                    isImposter = True
            
        if isImposter:
            
            if i == 0:
                guesslist4 = guesslist1
                #new_T_Letter = False
                #new_W_Letter = False
                isImposter = False
                sus = 1
                break

            if i != 0:
                for letter1 in guesslist3:

                    if gudGuess[f'{sus}'] != ' ':


                        if guesslist3[guesses[f'{sus}']-1] == gudGuess[f'{sus}']:
                            sus = sus+1

                        if guesslist3[guesses[f'{sus}']-1] != gudGuess[f'{sus}']:
                            guesslist3.clear()
                            isImposter = False
                            sus = 1
                        
                        if sus == i:
                            guesslist4.append(wort3)
                            guesslist3.clear()
                            isImposter = False
                            sus = 1
                            break

                    else:
                        break

    for mots in guesslist4:

        for lettres in mots:

            if lettres not in guesslist5:
                if lettres == 'a':
                    alphabet['1'] = alphabet['1']+1
                elif lettres == 'b':
                    alphabet['2'] = alphabet['2']+1
                elif lettres == 'c':
                    alphabet['3'] = alphabet['3']+1
                elif lettres == 'd':
                    alphabet['4'] = alphabet['4']+1
                elif lettres == 'e':
                    alphabet['5'] = alphabet['5']+1
                elif lettres == 'f':
                    alphabet['6'] = alphabet['6']+1
                elif lettres == 'g':
                    alphabet['7'] = alphabet['7']+1
                elif lettres == 'h':
                    alphabet['8'] = alphabet['8']+1
                elif lettres == 'i':
                    alphabet['9'] = alphabet['9']+1
                elif lettres == 'j':
                    alphabet['10'] = alphabet['10']+1
                elif lettres == 'k':
                    alphabet['11'] = alphabet['11']+1
                elif lettres == 'l':
                    alphabet['12'] = alphabet['12']+1
                elif lettres == 'm':
                    alphabet['13'] = alphabet['13']+1
                elif lettres == 'n':
                    alphabet['14'] = alphabet['14']+1
                elif lettres == 'o':
                    alphabet['15'] = alphabet['15']+1
                elif lettres == 'p':
                    alphabet['16'] = alphabet['16']+1
                elif lettres == 'q':
                    alphabet['17'] = alphabet['17']+1
                elif lettres == 'r':
                    alphabet['18'] = alphabet['18']+1
                elif lettres == 's':
                    alphabet['19'] = alphabet['19']+1
                elif lettres == 't':
                    alphabet['20'] = alphabet['20']+1
                elif lettres == 'u':
                    alphabet['21'] = alphabet['21']+1
                elif lettres == 'v':
                    alphabet['22'] = alphabet['22']+1
                elif lettres == 'w':
                    alphabet['23'] = alphabet['23']+1
                elif lettres == 'x':
                    alphabet['24'] = alphabet['24']+1
                elif lettres == 'y':
                    alphabet['25'] = alphabet['25']+1
                elif lettres == 'z':
                    alphabet['26'] = alphabet['26']+1
                elif lettres == 'é':
                    alphabet['27'] = alphabet['27']+1
                elif lettres == 'è':
                    alphabet['28'] = alphabet['28']+1
                elif lettres == 'î':
                    alphabet['29'] = alphabet['29']+1

    #print(guesslist)
    #print(guesslist1)
    #print(guesslist2) 
    #print(guesslist3)
    if len(guesslist4) < 100:
        print(guesslist4)
    print(f'Häufigster buchstabe: {transformer(max(alphabet, key= alphabet.get))}')
    print(f'Häufigkeit: {max(alphabet.values())}')

    weiter = input('Haben sie das wort gefunden? (j/n): ')

    for q in range(29):
        alphabet[f'{q}'] = 0
        alphabet['29'] = 0

    if weiter.lower() == 'j':
        break

    if weiter.lower() == 'n':
        #new_T_Letter = False
        #new_W_Letter = False
        guesslist1 = []
        guesslist2 = []
        guesslist3 = []
        guesslist4 = []