class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("person created")
    def who_am_i(self):
        print("ı am a person")
    def eat(self):
        print("ı am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        self.studentNumber = number
        Person.__init__(self, fname, lname)
        print("student created")

    # override
    def who_am_i(self):
        print("ı am a student")

    def sayHello(self):
        print(f"Hello, my name is {self.firstName}")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        self.branch = branch
        super().__init__(fname, lname)

    def who_am_i(self):
        print(f"ı am a {self.branch} teacher")


p1 = Person('Ahmet', 'Ada')
s1 = Student('Yasin','Ada', 1405)
t1 = Teacher('Yasemin', 'Baslanti', 'classroom')
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
print(t1.firstName + ' ' + t1.lastName)

p1.who_am_i()
p1.eat()
s1.who_am_i()
s1.eat()
s1.sayHello()
t1.who_am_i()