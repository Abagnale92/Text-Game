#coding=utf-8

from progetto import Personaggi
from progetto import Armi


classi = {"guerriero": Personaggi.Guerriero, "ladro": Personaggi.Ladro, 
          "arciere": Personaggi.Arciere, "mago": Personaggi.Mago}

armi = {"spada": Armi.usaSpada, "lancia": Armi.usaLancia, "pugnali": Armi.usaPugnali, 
        "scimitarra": Armi.usaScimitarra, "arco": Armi.usaArco, 
        "balestra": Armi.usaBalestra, "bacchetta": Armi.usaBacchetta, 
        "bastone": Armi.usaBastone, "mani nude": Armi.usaManiNude}

def continua(messaggio):
    print(messaggio, end='')
    input()

def scegliPersonaggio(nome):
    """ Permette all'utente di scegliere uno dei personaggi disponibili 
        e si occupa di istanziarlo. """
    while (True):
        risp = input("Scegli un personaggio tra:\n>  "
                      + "  ".join(sorted(classi)) + "\n> ").casefold()
        if (risp in classi):
            p = classi[risp](nome)
        else:
            print(">>> Valore non valido.")
            continue
        continua(p.descrizione)
        car = p.caratt
        print("Caratteristiche:", end=' ')
        for k in sorted(car):
            print(k, car[k], sep=' = ', end='; ')
        input()
        risp = input("Digita 'ok' per confermare: ")
        if (risp == 'ok'):
            return p
            
def scegliArma(p):
    """ Permette all'utente di scegliere una tra le armi disponibili 
        e si occupa di attribuirla al personaggio precedentemente istanziato. """
    while (True):
        risp = input("Scegli la tua arma tra:\n>  "
                + "  ".join(sorted(armi)) + "\n> ").casefold()
        if (risp in armi):
            a = armi[risp]
        else:
            print(">>> Valore non valido.")
            continue
        risp = input("Digita 'ok' per confermare: ").casefold()
        if ((risp == "ok")):
            p.usaArma = a
            break

if __name__ == '__main__':
    
    nome = input("Benvenuto! Digita il tuo nome: ").title()
    p = scegliPersonaggio(nome)
    scegliArma(p)
    p.gioca()

