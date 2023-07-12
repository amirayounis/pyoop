class SuperHero:
    def __init__(self,n,p,c,team=None):
        self.name=n
        self.power=p
        self.color=c
        self.team=team
    # instant method
    def __str__(self):
        return f"name:{self.name},color:{self.color},power:{self.power}"
    # getter
    @property
    def name(self):
        print("in getter")
        return self._name
    #setter
    @name.setter
    def name(self,name):
        print("in setter")
        if not name:
            raise ValueError("name is required in super hero data type")
        self._name=name
# ------------instances
iron=SuperHero("tonny","fly","red","Avangers")
thor=SuperHero("thor","hammer","grey","Avangers")
spiderman=SuperHero("dany","spider","red")            
print(iron)
        
    
    

