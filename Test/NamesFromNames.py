from random import shuffle
from nltk.corpus import words
from nltk.corpus import wordnet


listOfNames=['renjith','siddharth','anoop','rahul','midhun','anil','subin']
noShuffles=5
newNameSize=3
listOfChars=[]
commonAlph=[]
temp=''

for names in listOfNames:
    for alph in names:
        listOfChars.append(alph)

#now there is unique list of alphabets
uniqueAlph=list(set(listOfChars))

for eachUnique in uniqueAlph:
    if(listOfChars.__contains__(eachUnique)):
        commonAlph.append(eachUnique)
print(sorted(commonAlph))

while (noShuffles>0):
    shuffle(commonAlph)
    newname=temp.join(commonAlph[0:newNameSize])
    if (newname) in words.words():
        try:
            syns=wordnet.synsets(newname)
            print("newname is: ", newname)
            print("synonym is: ", syns[0].lemmas()[0].name())
            print("meaning is: ", syns[0].definition(),"\n")
            #print (newname,syns[0].definition())
        except IndexError:
            print("\n")
            continue
    noShuffles=noShuffles-1