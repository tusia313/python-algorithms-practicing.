# -*- coding: utf-8 -*-

def greet(name):
    print ("Cześć, " + name + "!")
    greet2(name)
    print ("Przygotowanie do pozegnania...")
    bye()

def greet2(name):
    print ("Jak się masz " + name + "?")

def bye():
    print ("Ok, cześć!")

greet("Marta")