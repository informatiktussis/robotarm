'''Grundlagen der Informatik II, SS 2017
Autor/en(Matrikelnummer): Michael Vogt (4391254), Jisoo Choi(3103933)
Datum: 07.07.2017
Uebungszettel 2 Aufgabe 2.
Allgemeine Beschreibung der Loesung und eventuelle Referenzen
In diesem Aufgabenzettel wurde eine Art des Sortes aus der Vorlesung verwendet. Hier wurde Mergesort benutzt.
Dieser Code ist mit dem aus Aufgabe 2. Nur wurde die if-Bedingung verändert falls UP == 1 ist, so dass die Liste
TO_SORT Pyramiden-sortiert sortiert wird.
'''

'''Zwei Daten vergleichen und in einer neuen List einfügen. '''
def merge(left, right): 
    result = []                                 # Es wird eine leere Liste "results" erstellt

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])           # left[0] in das Ende der neuen Liste einfügen 
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result

def merge_reverse(left, right):                 #  merge funktion für to_sort_reverse 
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(right[0])         #  right[0] in das Ende der neuen Liste einfügen 
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result


def to_sort_reverse(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    
    leftList = list[:mid]
    rightList = list[mid:]

    rightList = to_sort_reverse(rightList)
    leftList = to_sort_reverse(leftList)

    return merge_reverse(leftList, rightList)
	
def to_sortfunc(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    
    leftList = list[:mid]                           #  eine Liste zu zwei Teillisten spliten.
    rightList = list[mid:]

    leftList = to_sortfunc(leftList)                    #  rekursive Funktionen.
    rightList = to_sortfunc(rightList)

    return merge(leftList, rightList)                # Hier werden alle Teillisten berechnet. 


''' Eingabe für Sortier-Algorithmus '''

TO_SORT = [3, 78, 1, 9, 65, 12, 6, 0, 38, 17, 3, 91, 96, 15, 28, 70, 87, 45, 56, 10] # Die zu sortierende Liste
print("Gespeicherte Liste : " +str(TO_SORT)) # Die obige Liste wird geprintet...
up = input("Eingabe (1) um den obigen Array Pyramiden-sortiert zu erhalten: ") # Die Eingabe
up=int(up)

while up > -1:
    if up == 1: # Wenn die Eingabe = 1 ist.
        neue = [] # Es werden zwei leere Listen erstellt
        neue2 = []
        for x in TO_SORT: 
            if x % 2 == 0:# Hier wird dann jedes Element überprüft ob es sich um eine gerade Zahl handelt in TO_SORT
                neue.append(x) # und in die erste neue Liste gespeichert

        for y in TO_SORT: # Hier dann ob es eine ungearde Zahl ist
            if y % 2 != 0:
                neue2.append(y) # und werden wieder alle ungearden in neue2 gespeichert

        #Das heißt bis hierhin haben wir 2 Listen: Eine mit nur geraden und eine mit ungeraden Zahlen

        print("Sort anfangen mit to_sort")
        newList = to_sortfunc(neue) #Die geraden werden von klein nach groß Sortiert durch to_sortfunc (und in newList eingespeichert)
        newList2 = to_sort_reverse(neue2) #und die ungeraden von groß nach klein mit to_sort_reverse (und in newList2 gespeichert)
        print(newList+newList2) # Und werden dann addiert geprintet.
        print("Fertig! Ciao!")
        break # Ende des Programms
   

         #Noch eine kleine Extra-Funktion wenn man eine Falsche Eingabe tätigt..
    if up != 1:
        print("Geben Sie bitte richtige Nummer (1) ein.")
        print("Das Programm wird beendet.")
        break # Ende des Programms

