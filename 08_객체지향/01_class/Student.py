from Person import Person

class Student(Person):
    def study(self):
        print('study...')

lee = Person()
print(lee.mouth)
lee.talk()

kim = Student()
print(kim.mouth)
kim.talk()
kim.study()