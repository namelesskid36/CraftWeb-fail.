class person:
    def person_info(self, name, age):
        print('Inside Person Class')
        self.name = name
        print('Name: ', name, 'Age :', age)

class company:
    def company_info(self, company_name, location):
        print('Inside company Class')
        print('Name: ', company_name, 'Location ', location)

class employee(person, company):
    def employee_info(self, salary, skill):
        super().person_info('Name', 20)
        print('Inside employee class')
        print('Salary: ', salary, 'Skill : ', skill)

emp = employee()
emp.person_info('Jessica', 28)
emp.employee_info('Machine', 1200)