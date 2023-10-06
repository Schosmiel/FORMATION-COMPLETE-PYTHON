somme_tous_entiers = 0
somme_entiers_pairs = 0
somme_entiers_impairs = 0
somme_nombres_premiers = 0
a=0
b=0
c=0
d=0

for i in range(101):
    #a+=1
    somme_tous_entiers += i
    if i % 2 == 0:
        #b+=1
        somme_entiers_pairs += i
    else:
        #c+=1
        somme_entiers_impairs += i

    if i > 1:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            #d+=1
            somme_nombres_premiers += i
#print(a, "est le nombre total des entiers")
print("Somme de tous les entiers de 0 à 100:", somme_tous_entiers)
#print(b, "est le nombre total des entiers paire")
print("Somme des entiers pairs de 0 à 100:", somme_entiers_pairs)
#print(c, "est le nombre total des entiers impaire")
print("Somme des entiers impairs de 0 à 100:", somme_entiers_impairs)
#print(d, "est le nombre total des nombres premier")
print("Somme de tous les nombres premiers de 0 à 100:", somme_nombres_premiers)







