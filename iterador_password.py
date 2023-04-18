from random import choice
from typing import Dict, List

class IteradorPasswordCreate:
    """
    Iterador creado para generar una contraseña aleatoria utilizando
    el nombre y el apellido del usuario.
    El metodo constructor deberá llevar 3 paramentros:
    IteradorPasswordCreate(var: List[str], var:List[str], var:int)
    """
    def __init__(self,login_name,login_lastname,limit):
        self.login_name = login_name
        self.login_lastname = login_lastname
        self.limit = limit
        self.counter = 0
        self.alphanumeric = ["@","#","%","$","&"]
        self.numeric = ["1","2","3","4","5","6","7","8","9"]
        self.suggestions_for_you = ""


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            self.suggestions_for_you = (choice(self.alphanumeric)+self.login_name.upper()+self.login_lastname+(choice(self.numeric)*3))
            self.counter += 1
            return self.suggestions_for_you
        else:
            raise StopIteration

