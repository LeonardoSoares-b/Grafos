class Student:
    def __init__(self, name, grade, freq):
        self.name=name
        self.grade= grade
        self.freq=freq
    def approved(self):
        if self.grade>=6 and self.freq>=0.75:
            return True
        else:
            return False
s1 = Student("George", 9.3, 0.9)
print(s1.grade)
s2 = Student("Aline", 8.1, 0.8)
print(s2.grade)
s2.grade=10.0
print(s2.grade)
