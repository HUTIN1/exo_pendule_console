#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:14:05 2020

@author: nathan
"""
"""
le programme principal du pendul
"""

from fct import choimot, ouvrfichier, affich, verifmot, score

from random import randint



faute = 0       #nombre de faute
scoremax = 8    #le score max lors de sa session
mpasse = []     #les lettres déjà utilisé par le joueur lors d'une partie
mot = choimot(ouvrfichier())    #mot aléatoire
mtrouver=mot[0]      #mot actuel du joueur
for i in range(len(mot)):
    mtrouver = mtrouver + "_"    
n = 1   #pour savoir si le joueur ve continuer a jouer(1 continuer, 0 pour arrêter)

#boucle pour rejouer à l'inifni
while n == 1:
    faute = 0
    mpasse = []
    mot = choimot(ouvrfichier())
    mtrouver = mot[0]
    for i in range(len(mot)):
        mtrouver = mtrouver + "_" 
    affich(mtrouver,faute,mot)
    #boucle pour la parite actuel
    while  (faute != 8) and (mot != mtrouver) :
        mtrouver, mpasse, faute = verifmot(mot,mtrouver,mpasse,faute)
        affich(mtrouver,faute,mot)
        
    scoremax = score(scoremax,faute)
    n = int(input("Voulez-vous rejouez? (0 ou 1):"))
    