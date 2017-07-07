'''Grundlagen der Informatik II, SS 2017
Autor/en(Matrikelnummer): Michael Vogt (4391254), Jisoo Choi(3103933)
Datum: 07.07.2017
Uebungszettel 2, Aufgabe 1.
Allgemeine Beschreibung der Loesung und eventuelle Referenzen
In diesem Aufgabenzettel wurde eine Art des Sortes aus der Vorlesung verwendet. Hier wurde Mergesort benutzt.
'''

'''Zwei Daten vergleichen und in einer neuen List einfügen. '''
def merge(left, right):
    result = []                                 # Es wird eine leere Liste "results" erstellt

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])           #left[0] in das Ende der neuen Liste einfügen
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

def merge_reverse(left, right):                 #   merge funktion für to_sort_reverse 
    result = [] # Es wird eine leere Liste "results" erstellt

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
    
    leftList = list[:mid]                           #eine Liste zu zwei Teillisten spliten 
    rightList = list[mid:]

    leftList = to_sortfunc(leftList)                    # rekursive Funktionen
    rightList = to_sortfunc(rightList)

    return merge(leftList, rightList)                # Hier werden alle Teillisten berechnet. 


''' Eingabe für Sortier-Algorithmus '''

TO_SORT = [3, 78, 1, 9, 65, 12, 6, 0, 38, 17, 3, 91, 96, 15, 28, 70, 87, 45, 56, 10] #Die zu sortierende Liste aus 20 ganzen Zahlen.
print("Gespeicherte Liste : " +str(TO_SORT)) # Wird geprintet...
up = input("Eingabe (1) für klein nach groß, und (0) für groß nach klein: ")
up=int(up)

while up > -1:
    if up == 1: #Wenn up = 1 ist 
        print("Sort anfangen mit to_sort")
        newList = to_sortfunc(TO_SORT) #durch aufrufen der function to_sortfunc mit dem Argument TO_SORT wird TO_SORT von klein nach groß sortiert.
        print(newList) #Die neue Liste wird geprintet
        print("Fertig! Ciao!")
        break # Ende des Programms
    elif up == 0: # Wenn up = 0 ist
        print("Sort anfangen mit to_sort_reverse")
        newList = to_sort_reverse(TO_SORT) # mit to_sort_reverse wird TO_SORT von groß nach klein sortiert.
        print(newList) #Die neue Liste wird geprintet
        print("Fertig! Tschüss!")
        break # Ende des Programms
    if up != 0 or up != 1:
        print("Geben Sie bitte eine richtige Nummer (0 oder 1) ein.")
        print("Das Programm wird beendet.")
        break # Ende des Programms

        