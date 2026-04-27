#   Oppgave 1: 
#   applikasjon.py: 
def kvadratTall(tall):
return tall ** 2
#   test_applikasjon.py: 
def test_kvadratTall():
assert kvadratTall(2) == 4
assert kvadratTall(4) == 16
assert kvadratTall(10) == 100

def test_addisjon_feil_input(): 
    with pytest.raises(TypeError): 
        kvadratTall("a")
# Oppgave 2:
# applikasjon.py: 
def addisjon(a, b): 
return a + b 

def subtraksjon(a, b):
return a - b

def multiplikasjon(a, b):
return a * b

#   test_applikasjon.py: 
def test_addisjon():

assert addisjon (2, 5) == 7
assert addisjon (10, 20) == 30
assert addisjon (1000, 3000) == 4000

def test_subtraksjon():

assert subtraksjon (5, 2) == 3
assert subtraksjon (20, 10) == 10
assert subtraksjon (3000, 1000) == 2000

def test_multiplikasjon():

assert multiplikasjon (2, 5) == 10
assert multiplikasjon (10, 20) == 200
assert multiplikasjon (1000, 3000) == 3000000
    
def test_addisjon_feil_input(): 
with pytest.raises(TypeError): 
addisjon(4, "a") 
subtraksjon(3, "a")
multiplikasjon(2, "a")

#   Oppgave 3:
#   applikasjon.py: 
def division(a, b):
    return a / b
#   test_applikasjon.py: 
import pytest 

from applikasjon import division

def test_division():
   assert division(10, 0) == 5

def test_addisjon_feil_input(): 
    with pytest.raises(TypeError): 
        division(0, "a")

#   Oppgave 4:
#   applikasjon.py: 

    
