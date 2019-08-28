#coding=utf-8

from random import Random
from abc import ABCMeta, abstractmethod

class Personaggio(metaclass = ABCMeta):
    """ Personaggio tramite il quale l'utente può giocare una partita. """
    
    # costruttore

    def __init__(self, nome):
        self.nome = nome
        self.livello = 1
        self.gameOver = "Mi dispiace, non sei riuscito a portare a termine la tua missione."
    
    # metodo template
    
    def gioca(self):
        """ Gestisce l'intero ciclo di gioco di una partita. """
        continua(self.prologo)
        while (self.livello <= LIVMAX):
            self.prosegui()
            if (self.combatti(self.creaNemico())):
                self.livello += 1
            else:
                print(self.gameOver)
                return
        print(self.epilogo)
        return
    
    # metodo comune
    
    def combatti(self, nemico):
        """  Gestisce il processo di combattimento tra il personaggio e un nemico. """
        continua("E' comparso un nuovo nemico: " + nemico.nome + "!")
        while (True):
            continua("> Vita " + self.nome + ": " + str(self.vita) + "\n"
                    + "> Vita " + nemico.nome + ": " + str(nemico.vita))
            while (True):
                risp = input("Digita 'a' per attaccare o 's' per usare l'abilità speciale: ").casefold()
                if (risp == 'a'):
                    continua(self.nome + " sferra un attacco!")
                    danno = self.usaArma(self.caratt)
                    nemico.infliggi(danno)
                    continua(nemico.nome + " subisce " + str(danno) + " danni!")
                    break
                elif (risp == 's'):
                    continua(self.nome + " usa un'abilità speciale...")
                    if (rand.randint(0, 1)):
                        danno = self.attSpeciale()
                        nemico.infliggi(danno)
                        continua("...e " + nemico.nome + " subisce " + str(danno) + " danni!")
                        break
                    else:
                        continua("...ma l'attacco fallisce!")
                        break
                else:
                    continua(">>> Comando non valido")
            if (not nemico.sconfitto()):
                continua(nemico.nome + " si prepara ad attaccare!")
                danno = nemico.attacca()
                self.vita -= danno
                continua(self.nome + " subisce " + str(danno) + " danni!")
            else:
                continua(nemico.nome + " è stato sconfitto!")
                return True
            if (self.vita <= 0):
                continua(self.nome + " è stato sconfitto!")
                return False
    
    # metodi primitivi astratti
    
    @abstractmethod
    def prosegui(self):
        """ Avvia e gestisce un eventuale avvenimento tra un combattimento e l'altro. """
        pass
    
    @abstractmethod
    def creaNemico(self):
        """ Genera un nemico da combattere per il personaggio. """
        pass
    
    @abstractmethod
    def attSpeciale(self):
        """ Calcola e restituisce un danno differente da quello calcolato dall'attacco base. """
        pass
    
    
def continua(messaggio):
    print(messaggio, end='')
    input()
    
rand = Random()
LIVMAX = 5

    
class Nemico:
    """ Avversario del personaggio in un combattimento. """
    
    def __init__(self, nome, vita, attacco):
        self.nome = nome
        self.vita = vita
        self.attacco = attacco
    
    def attacca(self):
        """ Calcola e restituisce il danno inflitto dall'attacco del nemico. """
        return rand.randint(1, self.attacco)
    
    def infliggi(self, danno):
        """ Infligge al nemico il danno generato dall'attacco del personaggio. """
        self.vita -= danno
    
    def sconfitto(self):
        """ Determina se il nemico sia stato sconfitto. """
        return self.vita <= 0

