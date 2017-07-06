'''Grundlagen der Informatik II, SS 2017
Autor/en(Matrikelnummer): Fany, Mike, Jisoo Choi(3103933)
Datum: 07.07.2017

Uebungszettel 2
Allgemeine Beschreibung der Loesung und eventuelle Referenzen
(mind. 2-3 Saetze):

Aufgabe 1 - Sortieren (5 Punkte)
Schreiben Sie eine Funktion in Python, die zwei Parameter annimmt: ein Array der
Grösse 20 (ganze Zahlen) namens to_sort und ein Bit namens up. Die Funktion
soll das Array to_sort entweder von klein nach gross sortieren, wenn up == 1,
oder von gross nach klein, wenn up == 0.
Für das Sortieren selbst können Sie entweder Bubble-Sort oder Mergesort implementieren.
Sie dürfen dabei allerdings keine fremde Bibliotheken oder Funktionen benutzen
(z.B. die Funktion sorted(...)). Selbst geschriebene Hilfsfunktionen dürfen Sie
natürlich benutzen.

Aufgabe 2 - Pyramide (5 Punkte)
Nutzen Sie die Sortierfunktion aus Aufgabe 1 (ohne Veränderungen) um ein Array
auf folgende Weise zu sortieren: zuerst kommen alle gerade Zahlen, sortiert von klein
nach gross, danach alle ungerade Zahlen, sortiert von gross nach klein. Beispiel:
unsortiertes Array:
[ 3, 78, 1, 9, 65, 12, 6, 0, 38, 17, 3, 91, 96, 15, 28, 70, 87, 45, 56, 10]
Pyramiden-sortiert:
[ 0, 6, 10, 12, 28, 38, 56, 70, 78, 96, 91, 87, 65, 45, 17, 15, 9, 3, 3, 1]
'''


''' to_sort der Größe 20'''

'''up'''
'''from pprint import pprint'''
#!/usr/bin/python


U=[]

'''von klein nach groß'''
def to_sort(U):
    if len(U) <=1:
        return U
        '''U.split() in L, R'''
    for i in range(0, len(U)-1):
        if U[i]<U[i+1]:
            pass
        elif U[i]>U[i+1]:
            temp = U[i+1]
            U[i+1] = U[i]
            U[i] = temp

    h = round(1/2*len(U)-1)
    L = U[0:h]
    R = U[h+1:]
    to_sort(L)
    to_sort(R)
    return MERGE(R, L)

def to_sort_umgekehrt(U):
    if len(U) <=1:
        return U
    U.split in L, R
    L = to_sort_umgekehrt(L)
    R = to_sort_umgekehrt(R)
    return MERGE(L,R)

def MERGE(L,R):
    N = []
    def insert_last(N, A):
        N.extend([A])

    def delete_first(U):
        for i in range (0, len(U)-1):
            U[i] = U[i+1]
            U = U[:len(U)-2]
            return U

    while len(L) and len(R) != 0:
        if L[0] <= R[0]:
            insert_last(N, L[0])
            delete_first(L)
        else:
            insert_last(N, R[0])
            delete_first(R)
    while len(L)>0:
        insert_last(N, L[0])
        delete_first(L)
    while len(R)>0:
        insert_last(N, L[0])
        delete_first(L)
    return N





'''if (up == 0):
def "von groß nach klein"
'''

if __name__ == '__main__':

    li=[3, 78, 1, 9, 65, 12, 6, 0, 38, 17, 3, 91, 96, 15, 28, 70, 87, 45, 56, 10]
    print(li)
    up = input("Eingabe(0 oder 1): ")
    up=int(up)
    print(str(up) + " wurde als Ups Wert eingegeben.")

    while up == 0 or up == 1:
        if up == 1:
            print("Sort anfangen mit to_sort")
            to_sort(li)
            print(li)
        elif up == 0:
            print("Sort anfangen mit to_sort_umgekehrt")
    if up not in range(0,1):
        print("Geben Sie bitte richtige Nummer ein.")