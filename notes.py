Fr =  {"TE": {'1': 5, '2': 3, '3': 2.5, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0,
        'Francais':0}

Co =  {"TE": {'1': 5.5, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

All =  {"TE": {'1': 5.5, '2': 5.5, '3': 5, '4': 5.5, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 5.5, '2': 5.5, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Eng =  {"TE": {'1': 5, '2': 5.5, '3': 5.5, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Math =  {"TE": {'1': 5.5, '2': 6, '3': 6, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Geo =  {"TE": {'1': 6, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0,
        'SciencesHumaines': 0}

Hist =  {"TE": {'1': 3, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Chem =  {"TE": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Bio =  {"TE": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Phys =  {"TE": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

Mathop =  {"TE": {'1': 6, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        "TA": {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0},
        'Grade': 0}

#print(Fr['TA']['1'])
x = 0
oneint = 0
TAoneint = 0
nNoten = 0
TAnNoten = 0
finNote = 0
TAfinNote = 0
Gradelist =[]

def fach(note, i, TAorTE):


    if i+1 == 1:
        return Fr[TAorTE][f'{note+1}']
    if i+1 == 2:
        return Co[TAorTE][f'{note+1}']
    if i+1 == 3:
        return All[TAorTE][f'{note+1}']
    if i+1 == 4:
        return Eng[TAorTE][f'{note+1}']
    if i+1 == 5:
        return Math[TAorTE][f'{note+1}']
    if i+1 == 6:
        return Geo[TAorTE][f'{note+1}']
    if i+1 == 7:
        return Hist[TAorTE][f'{note+1}']
    if i+1 == 8:
        return Chem[TAorTE][f'{note+1}']
    if i+1 == 9:
        return Bio[TAorTE][f'{note+1}']
    if i+1 == 10:
        return Phys[TAorTE][f'{note+1}']
    if i+1 == 11:
        return Mathop[TAorTE][f'{note+1}']
'''
def Wfach(number):
    if i+1 == 1:
        Fr['Grade'] = number
        print( Fr['Grade'])
    if i+1 == 2:
        Co['Grade'] = number
        print( Co['Grade'])
    if i+1 == 3:
        All['Grade'] = number
        print( All['Grade'])
    if i+1 == 4:
        Eng['Grade'] = number
        print( Eng['Grade'])
    if i+1 == 5:
        Math['Grade'] = number
        print( Math['Grade'])
    if i+1 == 6:
        Geo['Grade'] = number
        print( Geo['Grade'])
    if i+1 == 7:
        Hist['Grade'] = number
        print( Hist['Grade'])
    if i+1 == 8:
        Chem['Grade'] = number
        print( Chem['Grade'])
    if i+1 == 9:
        Bio['Grade'] = number
        print( Bio['Grade'])
    if i+1 == 10:
        Phys['Grade'] = number
        print( Phys['Grade'])
    if i+1 == 11:
        Mathop['Grade'] = number
        print( Mathop['Grade'])'''

#Notes TE
for i in range(11):

    for note in range(12):
        noten = fach(note, i, "TE")

        #print(noten, note+1)

        if noten != 0:
            oneint = oneint+noten
            nNoten = nNoten+1

        else:
            pass

    for note in range(12):
        noten = fach(note, i, "TA")

        #print(noten, note+1)

        if noten != 0:
            TAoneint = TAoneint+noten
            TAnNoten = TAnNoten+1

        else:
            pass

    if oneint != 0:
        #print(oneint,TAoneint)

        if TAoneint != 0:
            finNote = (oneint+(TAoneint/TAnNoten))/(nNoten +1)
        else:
            finNote = oneint/nNoten

    Gradelist.append(finNote)

    oneint = 0
    nNoten = 0
    finNote = 0
    TAoneint = 0
    TAnNoten = 0

print(Gradelist)

for number in Gradelist:
    if x+1 == 1:
        Fr['Grade'] = number
        print( Fr['Grade'])
    if x+1 == 2:
        Co['Grade'] = number
        print( Co['Grade'])
    if x+1 == 3:
        All['Grade'] = number
        print( All['Grade'])
    if x+1 == 4:
        Eng['Grade'] = number
        print( Eng['Grade'])
    if x+1 == 5:
        Math['Grade'] = number
        print( Math['Grade'])
    if x+1 == 6:
        Geo['Grade'] = number
        print( Geo['Grade'])
    if x+1 == 7:
        Hist['Grade'] = number
        print( Hist['Grade'])
    if x+1 == 8:
        Chem['Grade'] = number
        print( Chem['Grade'])
    if x+1 == 9:
        Bio['Grade'] = number
        print( Bio['Grade'])
    if x+1 == 10:
        Phys['Grade'] = number
        print( Phys['Grade'])
    if x+1 == 11:
        Mathop['Grade'] = number
        print( Mathop['Grade'])
    
    x = x+1

if Co['Grade']!=0:  
    Fr['Francais'] = 4/5*Fr['Grade']+1/5*Co['Grade']
else:
    Fr['Francais']= Fr['Grade']

if Geo['Grade'] and Hist['Grade']!=0:    
    Geo['SciencesHumaines'] = 1/2*Geo['Grade']+1/2*Hist['Grade']

elif Geo['Grade']!=0:
    Geo['SciencesHumaines']=Geo['Grade']

elif Hist['Grade']!=0:
    Geo['SciencesHumaines']=Hist['Grade']

print(f"Francais: {Fr['Francais']}")
print(f"Allemand: {All['Grade']}")
print(f"Anglais: {Eng['Grade']}")
print(f"Math: {Math['Grade']}")
print(f"Sciences Humaines: {Geo['SciencesHumaines']}")
print(f"Chimie: {Chem['Grade']}")
print(f"Biologie: {Bio['Grade']}")
print(f"Physique: {Phys['Grade']}")
print(f"Math OP: {Mathop['Grade']}")
