def help():
    print("""
Das ist ein Rechner, wenn auch ein sehr unhandlicher, aber auf jeden Fall ein
Rechner. Als erstes gibst du zwei Zahlen ein und danach die Rechenoption.
Nachdem du das eingegeben hast wird es berechnet. Beim Addieren und
Subtrahieren steht es so da wie man es in der wirklichkeit schriftlich
berechnen würde. Beim Multiplizieren auch. Leider gibt es noc ein paar Fehler.
Beim Dividieren steht einfach nur das Ergbebnis, da es einfach zu schwer ist.
Wahlweise mit Rest oder Nachkommastellen.
""")


# Testing GitHub


def length(a):
    a = str(object=a)
    a = len(a) - 1
    return int(a)


def mul(a, b):
    a = int(a)
    b = int(b)
    a_str = str(a)
    b_str = str(b)
    a_len = length(a)
    b_len = length(b)
    if a < b:
        if a and b <= 10:
            print(a, "x", b, "=", a * b)
        else:
            if b < 100:
                a1 = int(a_str[a_len])
                a2 = int(a_str[a_len - 1])
                print(b, "x", a)
                print("----------")
                print(a2 * b * 10)
                print("", a1 * b)
                print("----------")
                print(a * b)
            elif b < 1000:
                a1 = int(a_str[a_len])
                a2 = int(a_str[a_len - 1])
                a3 = int(a_str[a_len - 2])
                print(b, "x", a)
                print("----------")
                print(a3 * b * 100)
                print("", a2 * b * 10)
                print(" ", a1 * b)
                print("----------")
                print(a * b)
            elif b < 10000:
                a1 = int(a_str[a_len])
                a2 = int(a_str[a_len - 1])
                a3 = int(a_str[a_len - 2])
                a4 = int(a_str[a_len - 3])
                print(b, "x", a)
                print("----------")
                print(a4 * b * 1000)
                print("", a3 * b * 100)
                print(" ", a2 * b * 10)
                print("  ", a1 * b)
                print("----------")
                print(a * b)
            elif b < 100000:
                a1 = int(a_str[a_len])
                a2 = int(a_str[a_len - 1])
                a3 = int(a_str[a_len - 2])
                a4 = int(a_str[a_len - 3])
                a5 = int(a_str[a_len - 4])
                print(b, "x", a)
                print("----------")
                print(a5 * b * 10000)
                print("", a4 * b * 1000)
                print(" ", a3 * b * 100)
                print("  ", a2 * b * 10)
                print("   ", a1 * b)
                print("----------")
                print(a * b)
            elif b < 1000000:
                a1 = int(a_str[a_len])
                a2 = int(a_str[a_len - 1])
                a3 = int(a_str[a_len - 2])
                a4 = int(a_str[a_len - 3])
                a5 = int(a_str[a_len - 4])
                a6 = int(a_str[a_len - 5])
                print(b, "x", a)
                print("----------")
                print(a6 * b * 100000)
                print("", a5 * b * 10000)
                print(" ", a4 * b * 1000)
                print("  ", a3 * b * 100)
                print("   ", a2 * b * 10)
                print("    ", a1 * b)
                print("----------")
                print(a * b)

    else:
        if a < 100:
            b1 = int(b_str[b_len])
            b2 = int(b_str[b_len - 1])
            print(a, "x", b)
            print("----------")
            print(b2 * a * 10)
            print("", b1 * a)
            print("----------")
            print(a * b)
        elif a < 1000:
            b1 = int(b_str[b_len])
            b2 = int(b_str[b_len - 1])
            b3 = int(b_str[b_len - 2])
            print(a, "x", b)
            print("----------")
            print(b3 * a * 100)
            print("", b2 * a * 10)
            print(" ", b1 * a)
            print("----------")
            print(a * b)
        elif a < 10000:
            b1 = int(b_str[b_len])
            b2 = int(b_str[b_len - 1])
            b3 = int(b_str[b_len - 2])
            b4 = int(b_str[b_len - 3])
            print(a, "x", b)
            print("----------")
            print(b4 * a * 1000)
            print("", b3 * a * 100)
            print(" ", b2 * a * 10)
            print("  ", b1 * a)
            print("----------")
            print(a * b)
        elif a < 100000:
            b1 = int(b_str[b_len])
            b2 = int(b_str[b_len - 1])
            b3 = int(b_str[b_len - 2])
            b4 = int(b_str[b_len - 3])
            b5 = int(b_str[b_len - 4])
            print(a, "x", b)
            print("----------")
            print(b5 * a * 10000)
            print("", b4 * a * 1000)
            print(" ", b3 * a * 100)
            print("  ", b2 * a * 10)
            print("   ", b1 * a)
            print("----------")
            print(a * b)
        elif a < 1000000:
            b1 = int(b_str[b_len])
            b2 = int(b_str[b_len - 1])
            b3 = int(b_str[b_len - 2])
            b4 = int(b_str[b_len - 3])
            b5 = int(b_str[b_len - 4])
            b6 = int(b_str[b_len - 5])
            print(a, "x", b)
            print("----------")
            print(b6 * a * 100000)
            print("", b5 * a * 10000)
            print(" ", b4 * a * 1000)
            print("  ", b3 * a * 100)
            print("   ", b2 * a * 10)
            print("    ", b1 * a)
            print("----------")
            print(a * b)
