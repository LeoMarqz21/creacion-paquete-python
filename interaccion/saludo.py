
def saludo():
    print('Hola, que tal como estas ?')

def despedida():
    print('Adios!!, cuidate mucho y bendiciones')

def bendiciones(name: str = None) -> None:
    if name is None:
        raise Exception('La funcion "bendiciones" requiere un parametro llamado "name"')
    print(f'Dios te bendigaaa {name} !!!...')

def dar_buenos_dias():
    print('Holaaa!! Buenos dias amigo')

