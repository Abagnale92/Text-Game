#coding=utf-8

from random import Random

""" Metodi utilizzati dal pattern dello Strategy """

rand = Random()

def usaSpada(caratt):
    danno = rand.randint(1, caratt['forza'])
    return danno * 3/2

def usaPugnali(caratt):
    danno = rand.randint(1, caratt['destrezza'])
    return danno * 3/2

def usaArco(caratt):
    danno = rand.randint(1, caratt['precisione'])
    return danno * 3/2

def usaBacchetta(caratt):
    danno = rand.randint(1, caratt['volontà'])
    return danno * 3/2

def usaLancia(caratt):
    danno = rand.randint(1, caratt['forza'])
    return danno + caratt['destrezza'] * 1/4

def usaScimitarra(caratt):
    danno = rand.randint(1, caratt['destrezza'])
    return danno + caratt['precisione'] * 1/4

def usaBalestra(caratt):
    danno = rand.randint(1, caratt['precisione'])
    return danno + caratt['forza'] * 1/4

def usaBastone(caratt):
    danno = rand.randint(1, caratt['volontà'])
    n = max(caratt.values())
    return danno + rand.randint(1, n) * 1/4

def usaManiNude(caratt):
    n = max(caratt.values())
    return rand.randint(1, n)
