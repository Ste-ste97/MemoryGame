import random
def displayCardsAera(hideallElements):
    count = 0
    for x in range(3):
        for y in range(4):
            print(hideallElements[count],end =" ")
            count+=1
        print('\n')
        
   
def  match(indexCard1,indexCard2):
    # Ο Χρήστης διαλέγει 2 κάρτες επιλέγοντας 2 θέσεις της τράπουλας
    value = allElements[indexCard1]
    value2 = allElements[indexCard2]

    #Υπολογίζει την θέση που βρίσκονται μέσα σε κάθε πίνακα και αν έχουν την ίδια θέση τότε οι δύο κάρτες ταιριάζουν διαφορετικά δεν ταιριάζουν
    if (value in letters6):
        index = letters6.index(value)
    else:
        index = numbers6.index(value)

    if (value2 in letters6):
        index2 = letters6.index(value2)
    else:
        index2 = numbers6.index(value2)

    if(index == index2):
        return 1
    else:
        return 0
            
def turnLookCard(indexCard):
    return ((bool(hideallElements[indexCard] != '?')))


print('Memory Game!')

numbers10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters10 = ['μηδέν', 'ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε', 'έξι', 'εφτά', 'οκτώ', 'εννιά']

numbers6 = []
letters6 = []

# Διάλεξε έξι τυχαίους αριθμούς από κάθε λίστα
while len(numbers6) < 6:
    index = random.randint(0,9)
    if not(numbers10[index] in numbers6):
        numbers6.append(numbers10[index])
        letters6.append(letters10[index])
    


# Βάλε σε μια λίστα (έστω allElements), όλα τα στοιχεία των λιστών numbers6 και letters 6
allElements = []
hideallElements = ['?','?','?','?','?','?','?','?','?','?','?','?']

for x in range(len(numbers6)):
  allElements.append(numbers6[x])
  allElements.append(letters6[x])


#Ανακάτεψε όλα τα στοιχεία της λίστας έτσι ώστε να μην είναι δίπλα διπλα εκείνα που αντιστοιχούν
random.shuffle(allElements)

# Debuging
print('Numbers 10 list is: ', numbers10)
print('letters 10 list is: ', letters10)
# Debuging
print('Numbers 6 list is: ', numbers6)
print('letters 6 list is: ', letters6)
print('allElements6 list is: ',allElements)
print('\n')

attemps = 7
remainingPairs = 6
clicked = 0

while (remainingPairs > 0 and attemps > 0 ):
    print('======================New round=======================')
    displayCardsAera(hideallElements)
    indexCard1 = (int) (input("Enter index card 1 1-12:"))
    indexCard1= indexCard1- 1

    while turnLookCard(indexCard1):
        indexCard1 = (int) (input("Enter valid index card 1 1-12:"))
        indexCard1= indexCard1- 1

    indexCard2 = (int) (input("Enter index card 2 1-12:"))
    indexCard2 = indexCard2- 1  
    while (indexCard1 == indexCard2) or turnLookCard(indexCard2):
        indexCard2 = (int) (input("Enter  valid index card 2 1-12:"))
        indexCard2 = indexCard2- 1   
    
    attemps= attemps-1
    hideallElements[indexCard1] = allElements[indexCard1]
    hideallElements[indexCard2] = allElements[indexCard2]
    print('\n')
    print('allElements6 list is:',allElements)
    displayCardsAera(hideallElements)

    if match(indexCard1,indexCard2):
        print('These two cards match \n')
        remainingPairs= remainingPairs - 1
       
    else:
        print('These two cards do not match\n')
        hideallElements[indexCard1] = '?'
        hideallElements[indexCard2] = '?'
    print("Finding Pairs ",6-remainingPairs)
    print('Attemps ', attemps)
    print('\n')

if(remainingPairs == 0):
    print('You win')
else: 
    print('You lose')
    