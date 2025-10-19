class student:
    grade=10
    name="Koyna"

    def introduction(self):
        print("Hi! I am a student!")

    def detailes(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob=student()
ob.introduction()
ob.detailes()