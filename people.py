class Person:

    def __init__(self, name, last_name, age):   #added the person last name
        self.name = name
        self.last_name = last_name
        self.age = age


    def full_name(self):
        return (f'{self.name} {self.last_name}') #Putted together the name a last name in full name


    def say_hello(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old')
    

    def __len__(self): #changes to the dunder method __len__
        return len(self.full_name())


if __name__ == '__main__':
    person = Person('David', 'Aroesti', 34)
    print(person.full_name())
    person.say_hello()
    print(len(person))