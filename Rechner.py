import funktionen as fn

fn.help()
schleife = 1
while schleife > -1:
    schleife2 = 1
    while schleife2 > -1:
        try:
            n1 = float(input("""
Gib deine erste Zahl ein: """))
            n2 = float(input("""
Gib deine zweite Zahl ein: """))
        except ValueError:
            print("""
Bitte gib eine Zahl ein.""")
            schleife2 += 1
        else:
            schleife3 = 1
            while schleife3 > -1:
                print("""
Gib für Addition '+', für Subtraktion '-', für Multiplikation '*' oder für
Division '/' ein!""")
                zeichen = input("""
Gib das Zeichen für die Rechenoption ein, die du berechnen willst: """)
                if zeichen == '+':
                    print(" ", n1)
                    print(zeichen, n2)
                    print("-----")
                    print(" ", n1 + n2)

                elif zeichen == '-':
                    print(" ", n1)
                    print(zeichen, n2)
                    print("-----")
                    print(" ", n1 - n2)

                elif zeichen == '*':
                    fn.mul(n1, n2)

                elif zeichen == '/':
                    schleife4 = 1
                    while schleife4 > -1:

                        print("""
Gib ein ob du das Ergebnis mit Rest oder ohne Rest(also eine Kommazahl) haben
willst!""")
                        print("""
Gib 'Rest' für das Ergebnis mit Rest ein und 'ohne Rest' für das Ergebnis ohne
Rest.""")

                        rest = input("""
Auswahl:""")

                        if rest == "Rest":
                            print(n1, zeichen, n2, "=", n1 // n2)
                            print(n1 % n2, "R")

                        elif rest == "ohne Rest":
                            print(n1, zeichen, n2, "=", n1 / n2)

                        else:
                            print("""
Ungültige Angabe!""")
                            schleife4 += 1
                else:
                    schleife3 += 1
                    print("""
Ungültiges Zeichen""")

                neustarten = input("""
Willst du dieses Programm neustarten?(ja/nein) """)
                schleife5 = 1
                while schleife5 > -1:
                    if neustarten == "ja":
                        schleife += 1
                    elif neustarten == "nein":
                        exit()
                    else:
                        schleife5 += 1
