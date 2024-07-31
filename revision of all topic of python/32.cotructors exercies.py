class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("good morning")


raj = Person('raj Kumar')

print(raj.name)
raj.talk()


rahul = Person("rahul patil")
print(rahul.name)
rahul.talk()
