class Employee:
    # _name,_salray
    def __init__(self,name,salary):
            self.name=name
            self._salary=salary
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("error")
        self._name=value
        
e1=Employee("ahmed",5000)
# ---->setter
print(e1.name)
# e1.setter_name("omar")
# print(e1.getter_name())
        
         