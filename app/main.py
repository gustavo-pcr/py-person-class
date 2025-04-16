class Person:

    people = {}
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def create_person_list(self, people_dict: list):
        person_list = []
        for person_dict in people_dict:
            name = person_dict["name"]
            age = person_dict["age"]
            person = Person(name, age)
            person_list.append(person)   
            if "wife" in person_dict and person_dict["wife"]:
                wife_name = person_dict["wife"]
                person.wife = Person.people[wife_name]
                
            if "husband" in person_dict and person_dict["husband"]:
                husband_name = person_dict["husband"]
                person.husband = Person.people[husband_name]

        return person_list
