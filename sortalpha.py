textfile = open('file_unsorted.txt')
x = 0
text = ''
textlist = []
Ramdeeznuts = ''
for chars in open('file_unsorted.txt'):
    #print(chars)
    x = x+1
    #print(x)
    for letter in chars:
        #print(letter)
        if letter != ' ':
            text = text+letter

        elif letter == ' ':
            text = text + f'{letter}\n'
    
    for words in text:

        if words != '\n':

            if words!= ' ':
                Ramdeeznuts = Ramdeeznuts+words

        if words == ' ':
            textlist.append(Ramdeeznuts.lower())
            Ramdeeznuts = ''


#print(text)

textlist.sort()
print(textlist)

for word in textlist:

    with open('finalfile.txt', 'a') as f:
        f.write(word+'\n')
    
