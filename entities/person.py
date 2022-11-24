
class Person:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        
    def saludar(self):
        print(f'Hola {self.__name}, como estas?')
    
    def __str__(self):
        return f'["id": {self.__id}, "name":{self.__name}]'

        
