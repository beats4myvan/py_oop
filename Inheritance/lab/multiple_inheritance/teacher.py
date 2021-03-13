from Inheritance.multiple_inheritance.employee import Employee
from Inheritance.multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'


teacher = Teacher()

print(teacher.teach())
print(teacher.get_fired())
print(teacher.sleep())