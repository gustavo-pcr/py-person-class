class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dict: list):
    person_list = []

    # Step 1: Create all Person instances first
    for person_data in people_dict:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    # Step 2: Assign relationships
    for person_data in people_dict:
        person = Person.people[person_data["name"]]

        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return person_list
