"""
Ce code est déstiner à fusioner avec le premier càd main.py
"""

import pygame
pygame.init()
pygame.display.set_caption("The Messager Game")
ecran = pygame.display.set_mode((640,480))

on = True

while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False


class Joueur():

    def __init__(self,atk,protec,acc,esquive,pv,nb_pv,classe,arme): #tous des int sauf arme qui est une instance de la classe arme
        self.atk=atk
        self.protec=protec
        self.acc=acc
        self.esquive=esquive
        self.classe=classe
        self.pv=pv
        self.nb_pv=nb_pv
        self.arme=arme
        self.inv=[(3,"potion"),(1,"carte")]

    def SetAtk(self,nb=1,bool=True):
        if bool:
            self.atk+=nb
        else:
            self.atk-=nb

    def SetProtec(self,nb=1,bool=True):
        if bool:
            self.protec+=nb
        else:
            self.protec-=nb

    def SetAcc(self,nb=1,bool=True):
        if bool:
            self.acc+=nb
        else:
            self.acc-=nb

    def SetEsquive(self,nb=1,bool=True):
        if bool:
            self.esquive+=nb
        else:
            self.esquive-=nb

    def SetProtec(self,nb=1,bool=True):
        if bool:
            self.protec+=nb
        else:
            self.protec-=nb

    def SetPv(self,nb=1,bool=True):
        if bool:
            self.pv+=nb
        else:
            self.pv-=nb

    def SetStatNb_pv(self,nb=1,bool=True):
        if bool:
            self.nb_pv+=nb
        else:
            self.nb_pv-=nb

    def ChangeArme(self,nv_arme):
        self.inv.append((1,self.arme.nom))
        self.arme=nv_arme    #instance de la classe arme


class Arme():
    def __init__(self,nom,atk,acc,obtention,rarete):
        self.nom=nom
        self.atk=atk
        self.acc=acc
        self.obtention=obtention
        self.rarete=rarete

    def SetAtk(self,nb=1,bool=True):
        if bool:
            self.atk+=nb
        else:
            self.atk-=nb

    def SetAcc(self,nb=1,bool=True):
        if bool:
            self.acc+=nb
        else:
            self.acc-=nb
