from entity.employee import Employee

class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Team size: {self.team_size}")