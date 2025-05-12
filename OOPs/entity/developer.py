from entity.employee import Employee

class Developer(Employee):

    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang

    def display(self):
        super().display()
        print(f"Programming Language: {self.prog_lang}")