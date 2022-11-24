from entities.person import Person


names = ['leo', 'marqz', 'arg', 'elm']

def get_list_people(people: list = None) ->list :
    list_people = []
    if people is None:
        return []
    for index,name in enumerate(names, 1):
        list_people.append(Person(id=index, name=name))
    return list_people

    

if __name__ == '__main__':
    print(__name__)
    people = get_list_people(names)
    people[0].saludar()
    data = people[1]
    print(data)