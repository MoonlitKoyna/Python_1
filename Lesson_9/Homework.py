
class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def introduce(self):
        print(f"Hello! I am {self.name}. ")
        print(f"I am a {self.model} model, built in {self.year}.")


tom = Robot("Tom", "A12345", 2024)
jerry = Robot("Jerry", "A210", 2023)

tom.introduce()
jerry.introduce()
