class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My name is {self.fullname},{self.age} years,family status:{self.is_married}')


class Students(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) / marks)


class Teacher(Person):
    salary = 12000

    def __init__(self, fullname, age, experience):
        super().__init__(self, fullname, age)
        self.experience = experience

    def reward(self):
        if self.experience >= 3:
            new_salary = (self.salary + (self.salary / 100 * 5) * (self.salary - 3))
            return new_salary

    def info_teachers(self):
        print(f'Teachers name:{self.fullname},age:{self.age},work experience:{self.experience},'
              f'Чеканных монет:{self.salary}')


def create_students():
    student1 = Students('Azat', 21, 'single', marks={
        'math': 65,
        'Dota': 10,
        'Chemistry': 80,
    })
    student2 = Students('Nuria', 23, 'married', marks={
        'math': 99,
        'Dota': 1,
        'Chemistry': 35,
        'Physics': 11,
    })
    student3 = Students('Aleksei', 35, 'married', marks={
        'math': 101,
        'Dota': 45,
        'Chemistry': 19,
        'Physics': 70,
        'minecraft': 1,
    })

    geektech = [student1, student2, student3]
    return geektech


create_students()
for i in create_students():
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name:{i.fullname}\n'
          f'age:{i.age}\n'
          f'Family status:{i.is_married}\n'
          f'marks:{i.marks}\n'
          f'average mark:{sum(list)/len(list)}\n')


