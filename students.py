class Student:
    # class property
    counter=0
    def __init__(self,name,grade):
        # instance property
        self.name=name
        self.grade=grade
        # Student.counter+=1
        Student.conter()
        self.id=Student.counter
    # class method
    @classmethod
    def conter(cls):
        cls.counter+=1
    # instant methods
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,n):
        if not n:
            raise ValueError("error")
        self._name=n
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,g):
        if not g:
            raise ValueError("error")
        self._grade=g
    def __str__(self):
        return f"id:{self.id} name: {self.name} ,grade:{self.grade}"
stu_1=Student("ahmed",4)
stu_2=Student("omar",7)
stu_3=Student("aly",3)
print(stu_3)