######### zakladne riesenie

# strana = 5  
# obvod = 4 * strana
# print(obvod)

######### riesenie s vypisanim hlasky a pre cele cisla 

# strana = int(input("Zadaj dĺžku strany štvorca: "))
# obvod = 4 * strana
# print(f"Obvod štvorca je {obvod}")

######### riesenie pre desatine cisla ale stale vies zadat aj text a padne to

# strana = float(input("Zadaj dĺžku strany štvorca: "))
# obvod = 4 * strana
# print(f"Obvod štvorca je {obvod}")

#########resenie vyhodnocuje ci si zadal desatine, cele cislo, prazdne pole, text - program po tomto nespadne ale upozorni na konkretnu chybu ktoru si spravil 

# side = input("Zadaj cislo (cele alebo desatine)")

# try: # Najprv skúsime previesť na celé číslo
#     result = int(side)
#     print(f"Super cislo {result}, ktore si zadal je cele cislo")
# except ValueError: # Ak to nešlo, skúsime previesť na desatinné číslo (float)
#     try:              
#         result = float(side)
#         print (f"Super cislo {result} ktore si zadal je desatine cislo")
#     except ValueError: # Ak ani to nešlo, vstup nebol číslo
#         print (f"cislo {side}, ktore si zadal nie je cele ani desatine cislo" ) 
#         result = None # finta ak viem ze cislo nie je pouzitelne tak ho nastavim na hodnotu none a pridam podmienku v if.

# if result is not None:
#     circuit = 4 * result 
#     print(f"Obvod stvorca so stranou {result} je {circuit}")
# else:
#     print(f"Neviem vypocitat obvod hodnota ktoru si zadal je v nespravnom tvare")
#     print(f"Tu je to co si zadal {side}")

# if side.strip() == "": # musi tam byt aj side (predstavuje premennu v ktorej je hodnota ktoru si zadal), lebo strip nie je samostatna metoda  
#     print("Nic si nezadal")

######### riesenie pridava možnosť opakovať zadanie, kým nezadáš platné číslo pomocou while cyklu - vysvetlenie dole pod programom

# while True: 
#     side = input("Zadaj cislo (cele alebo desatine)")

#     try: # Najprv skúsime previesť na celé číslo
#         result = int(side)  
#         print(f"Super cislo {result}, ktore si zadal je cele cislo")
#         break
#     except ValueError: # Ak to nešlo, skúsime previesť na desatinné číslo (float)
#         try:              
#             result = float(side)
#             print (f"Super cislo {result} ktore si zadal je desatine cislo")
#             break
#         except ValueError: # Ak ani to nešlo, vstup nebol číslo
#             print (f"cislo {side}, ktore si zadal nie je cele ani desatine cislo. Skus to znova.\n" ) 
           
#             result = None # finta ak viem ze cislo nie je pouzitelne tak ho nastavim na hodnotu none a pridam podmienku v if.

# if result is not None:
#     circuit = 4 * result 
#     print(f"Obvod stvorca so stranou {result} je {circuit}")
# else:
#     print(f"Neviem vypocitat obvod hodnota ktoru si zadal je v nespravnom tvare")
#     print(f"Tu je to co si zadal {side}")

# if side.strip() == "": # musi tam byt aj side (predstavuje premennu v ktorej je hodnota ktoru si zadal), lebo strip nie je samostatna metoda  
#     print("Nic si nezadal")


# Čo sa tu deje:
# while True: = nekonečný cyklus, ktorý beží stále, kým nedáme break

# Ak je vstup platné číslo (int alebo float), uloží sa do result a cyklus sa ukončí

# Ak nie, program vypíše upozornenie a pýta sa znova

# Po cykle sa vypočíta obvod (4 * result)

######## pridanie moznosti koniec
while True: 
    side = input("Zadaj cislo (cele alebo desatine) alebo napis koniec pre ukoncenie:")

    if side.strip() == "":
        print("Nic si nezadal \n")
        continue # vrati sa na zaciatok cyklu

    if side.lower() == "koniec":
        print("Program ukonceny pouzivatelom.")
        break # ukonci cely cyklus a teda program

    try: # Najprv skúsime previesť na celé číslo
        result = int(side)  
        print(f"Super cislo {result}, ktore si zadal je cele cislo")
    except ValueError: # Ak to nešlo, skúsime previesť na desatinné číslo (float)
        try:              
            result = float(side)
            print (f"Super cislo {result} ktore si zadal je desatine cislo")
        except ValueError: # Ak ani to nešlo, vstup nebol číslo
            print (f"cislo {side}, ktore si zadal nie je cele ani desatine cislo. Skus to znova.\n" ) 
            continue # ide znova od zaciatku cyklu

    circuit = 4 * result 
    print(f"Obvod stvorca so stranou {result} je {circuit}")
