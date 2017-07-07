'''Grundlagen der Informatik II, SS 2017
Autor/en(Matrikelnummer): Michael Vogt (4391254), Fany Bowt (4345894), Jisoo Choi(3103933)
Datum: 07.07.2017

Uebungszettel 2
Allgemeine Beschreibung der Loesung und eventuelle Referenzen
(mind. 2-3 Saetze): In diesem Aufgabenzettel wurde eine Art des Sortes aus der Vorlesung verwendet. Hier wurde Mergesort benutzt.
'''

'''Zwei Daten vergleichen und in einer neuen List einfügen. '''
def merge(left, right):
    result = []                                   ''' die dritte Liste für zusammenmachen '''

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])           '''left[0] in das Ende der neuen Liste einfügen '''
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

def merge_reverse(left, right):                   ''' merge funktion für to_sort_reverse '''
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(right[0])           '''right[0] in das Ende der neuen Liste einfügen '''
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
	
def to_sort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    
    leftList = list[:mid]                             '''eine Liste zu zwei Teillisten spliten '''
    rightList = list[mid:]

    leftList = to_sort(leftList)                      '''rekursive Funktionen'''
    rightList = to_sort(rightList)

    return merge(leftList, rightList)                 '''Hier werden alle Teillisten berechnet. '''


''' Test code für Sort Algorithmus '''

list = [3, 78, 1, 9, 65, 12, 6, 0, 38, 17, 3, 91, 96, 15, 28, 70, 87, 45, 56, 10]
print("Gespeicherte Liste : " +str(list))
up = input("Eingabe für up(0 oder 1): ")
print(up + " wurde als Ups Wert eingegeben.")
up=int(up)

while up > -1:
    if up == 1:
        print("Sort anfangen mit to_sort")
        newList = to_sort(list)
        print(newList)
        print("Fertig! Ciao!")
        break
    elif up == 0:
        print("Sort anfangen mit to_sort_reverse")
        newList = to_sort_reverse(list)
        print(newList)
        print("Fertig! Tschüss!")
        break
    if up not in range(0,1):
        for i in range(0,4):
            print("Geben Sie bitte richtige Nummer ein.")
            print("Sie haben noch " + str(4-i) + " Versuch(e).")

            up = input("Eingabe für up(0 oder 1): ")
            up=int(up)
            
        print("Oh Mann, Sie haben gar kein Bock drauf! Alles klar, Tschüss!!")
        break