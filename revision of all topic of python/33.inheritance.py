class animals:
    def walk(self):
        print("walk")


class Dog (animals):
    pass


class Cat(animals):
    def huggry(self):
        print("maowwww")


cat1 = Cat()
cat1.huggry()