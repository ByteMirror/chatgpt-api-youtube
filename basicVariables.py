name = "Sebastian"

age = 27

birthday = "1996-01-01"

def itsaMe(): # What happens if we add a name var inside the function?
    print(f"Hi, I am {name}, I am {age} years old and I was born on {birthday}")
    print("Hi, I am " + name + " I am a cool guy")


class Person:
    def __init__(self, name: str, age: int, birthday: str):
        self.name = name
        self.age = age
        self.birthday = birthday
    isMuscular = False
    def introduce(self):
        print(f"Hi, I am {self.name}, I am {self.age} years old and I was born on {self.birthday}")


person = Person("Lars", 21, "1996-01-05")


person.introduce()

class Doorman(Person):
    super.__init__()

    isMuscular = True

    def kickOut(person: Person):
        
