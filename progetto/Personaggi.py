#coding=utf-8

from progetto.Personaggio import Personaggio, Nemico, continua, rand, LIVMAX

class Guerriero(Personaggio):
    """ Una delle tipologie di personaggio disponibili. """
    
    # costruttore
    
    def __init__(self, nome):
        super().__init__(nome)
        self.__VITAMAX = 30
        self.vita = self.__VITAMAX
        self.caratt = {'forza': 10, 'destrezza': 5, 'precisione': 5, 'volontà': 1}
        self.descrizione = ("Un combattente con straordinaria capacità di combattimento ed ineguagliabile "
                            + "abilità con le armi.")
        self.prologo = ("Il valoroso guerriero ha l'arduo compito di liberare la principessa " 
                        + "dalle grinfie del malvagio dragone del castello.")
        self.epilogo = ("Il valoroso guerriero, dopo tante intrepide battaglie, salva la principessa "
                        + "dalle grinfie del malvagio dragone.")
    
    # metodi primitivi implementati
        
    def prosegui(self):
        continua("Il valoroso guerriero avanza con audacia tra i corridoi del castello.")
        n = rand.randint(1, 3)
        if (self.livello > 1 & n == 1):
            continua("In uno dei corridoi, il guerriero trova il mantello della resistenza!")
            self.caratt['forza'] += 2
            continua("> Forza +2")
            self.caratt['volontà'] += 2
            continua("> Volontà +2")
                           
    def creaNemico(self):
        if (self.livello < LIVMAX / 2):
            return Nemico("Orco", 10, 10)
        elif (self.livello < LIVMAX):
            return Nemico("Demone", 20, 10)
        else:
            return Nemico("Dragone", 30, 15)
        
    def attSpeciale(self):
        return self.usaArma(self.caratt) + self.VITAMAX - self.vita


class Ladro(Personaggio):
    """ Una delle tipologie di personaggio disponibili. """

    # costruttore

    def __init__(self, nome):
        super().__init__(nome)
        self.__VITAMAX = 25
        self.vita = self.__VITAMAX
        self.caratt = {'forza': 5, 'destrezza': 10, 'precisione': 5, 'volontà': 1}
        self.descrizione = ("Uno scaltro e abile esploratore e una spia che vince le battaglie "
                            + "giocando sporco.")
        self.prologo = ("L'inafferrabile ladro è alla ricerca del leggendario tesoro delle antiche miniere "
                + "infestate da numerosi banditi.")
        self.epilogo = ("Dopo aver sconfitto il temibile capobanda dei banditi, il ladro " + 
                           "raggiunge l'agognato tesoro.")
        
    # metodi primitivi implementati
        
    def prosegui(self):
        n = rand.randint(1, 3)
        if (self.livello > 1 & n == 1):
            continua("Il ladro si trova di fronte ad un bivio...")
            n = rand.randint(0, 1)
            if (n):
                continua("Il ladro va a destra...")
            else:
                continua("Il ladro va a sinistra...")
            n = rand.randint(0, 1)
            if (n):
                continua("...e trova i guanti della destrezza!")
                self.caratt['destrezza'] += 3
                continua("> Destrezza +3")
            else:
                continua("...ma non trova nulla di prezioso!")
        continua("L'inafferrabile ladro avanza silenzioso nel buio dei cunicoli della miniera.")
                           
    def creaNemico(self):
        if (self.livello < LIVMAX):
            return Nemico("Bandito", 10, 10)
        else:
            return Nemico("Capobanda", 25, 10)
        
    def attSpeciale(self):
        return self.usaArma(self.caratt) + self.caratt['destrezza'] / 2


class Arciere(Personaggio):
    """ Una delle tipologie di personaggio disponibili. """

    # costruttore

    def __init__(self, nome):
        super().__init__(nome)
        self.__VITAMAX = 20
        self.vita = self.__VITAMAX
        self.caratt = {'forza': 5, 'destrezza': 5, 'precisione': 10, 'volontà': 1}
        self.descrizione = "Un astuto ed abile combattente delle terre selvagge."
        self.prologo = ("Il baldo arciere errante viaggia solitario nella fitta foresta "
                        + "alla ricerca di grosse prede da catturare.")
        self.epilogo = ("Sconfitto il feroce troll di montagna, l'arciere torna al suo villaggio "
                        + "con un ricco bottino.")
        
    # metodi primitivi implementati
        
    def prosegui(self):
        continua("Il baldo arciere avanza tra gli alberi della foresta.")
        n = rand.randint(1, 3)
        if (self.livello > 1 & n == 1):
            continua("L'arciere trova un'erba curativa!")
            self.vita += 3
            continua("> Vita +3")
                           
    def creaNemico(self):
        if (self.livello < LIVMAX - 1):
            return Nemico("Lupo", 10, 5)
        elif (self.livello < LIVMAX):
            return Nemico("Orso", 15, 5)
        else:
            return Nemico("Troll", 20, 10)
        
    def attSpeciale(self):
        return self.usaArma(self.caratt) * 2
        
        
class Mago(Personaggio):
    """ Una delle tipologie di personaggio disponibili. """
    
    # costruttore

    def __init__(self, nome):
        super().__init__(nome)
        self.__VITAMAX = 15
        self.vita = self.__VITAMAX
        self.caratt = {'forza': 1, 'destrezza': 5, 'precisione': 5, 'volontà': 10}
        self.descrizione = "Un potente incantatore con innati poteri magici istruito nelle arti arcane."
        self.prologo = ("L'intrepido mago si mette alla ricerca di un antico artefatto "
                           + "magico per studiarlo e scoprire i segreti che nasconde.")
        self.epilogo = ("Il mago trova finalmente l'antico artefatto e acquisisce nuovi misteriosi "
                        + "poteri magici.")
        
    # metodi primitivi implementati
    
    def prosegui(self):
        continua("L'intrepido mago prosegue il suo cammino, attratto dal potere dell'artefatto.")
        n = rand.randint(1, 3)
        if (self.livello > 1 & n == 1):
            continua("Appare uno strano individuo che pone al mago uno strano indovinello...")
            n = rand.randint(0, 1)
            if (n):
                continua("...ma il mago, pronto, dà la risposta giusta!")
                self.caratt['volontà'] += 4
                continua("> Volontà' +4")
            else:
                continua("...ma il mago, confuso, dà una risposta errata!")
                self.caratt['volontà'] -= 4
                continua("> Volontà' -4")
                           
    def creaNemico(self):
        if (self.livello < LIVMAX - 1):
            return Nemico("Folletto", 10, 5)
        else:
            return Nemico("Stregone", 20, 10)
        
    def attSpeciale(self):
        return sum(self.caratt.values()) / 2
            
