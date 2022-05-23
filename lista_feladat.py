lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#1. Hány szám van a listában? Készíts függvényt lista_elemek_szama() néven,  amely visszatér egy lista elemeinek a számával


def lista_elemek_szama(a):
    b = 0
    for i in a:
        b = b+1
    return b


print(lista_elemek_szama(lista))


#2. Melyik a legkisebb szám a listában? Készíts függvényt legkisebb() néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.

def legkisebb(a):
    b = a[0]
    for i in a:
        if b > i:
            b = i
    return b
    
print(legkisebb(lista))


#3. Mennyi a lista számainak összege? Készíts függvényt osszeg() néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.

def osszeg(a):
    b = 0
    for i in a:
        b = b+i
    return b
        
print(osszeg(lista))


#4. Mennyi a lista számainak szorzata? Készíts függvényt szorzat() néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával.

def szorzat(a):
    b = 1
    for i in a:
        b = b*i
    return b

print(szorzat(lista))


#5. Melyik a legnagyobb szám a listában? Készíts függvényt legnagyobb() néven,  amely visszatér egy számokat tartalmazó lista legnagyobb számával.

def legnagyobb(a):
    b = a[0]
    for i in a:
        if b < i:
            b = i
    return b
    
print(legnagyobb(lista))



#6. Melyik a legelső szám a listában? Készíts függvényt legelso() néven,  amely visszatér egy számokat tartalmazó lista legelso számával.

def legelso(a):
    return a[0]

print(legelso(lista))
    

#7. Melyik a utolso szám a listában? Készíts függvényt utolso() néven,  amely visszatér egy számokat tartalmazó lista utolso számával.

def utolso(a):
    return a[-1]

print(utolso(lista))



#8. Mennyi a páros számok száma a listában? Készíts függvényt parosok_szama() néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával.

def parosok_szama(a):
    b = 0
    for i in a:
        if i % 2 == 0:
            b = b+1
    return b

print(parosok_szama(lista))



#9. Első kettő. Készíts függvényt elso_ketto() néven,  amely visszatér egy számokat tartalmazó lista első két számával mint listával. 

def elso_ketto(a):
    return [a[0], a[1]]

print(elso_ketto(lista))


#10. Első és utolsó Készíts függvényt elso_utolso() néven,  amely visszatér egy számokat tartalmazó lista első ás utolsó számával mint listával.

def elso_utolso(a):
    return [a[0], a[-1]]

print(elso_utolso(lista))


