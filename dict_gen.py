lenngth = int(input('How big is the dict?: '))
type = input('value is str or int?: ')

dictionary = ''

if type == 'str':

    for i in range(lenngth):
        dictionary = dictionary + f"'{i+1}': ' ', "

if type == 'int':
    
    for i in range(lenngth):
        dictionary = dictionary + f"'{i+1}': {0}, "

print(dictionary)
