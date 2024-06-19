class INT :
    def __init__(self,nm,ag,gn):
        self.name = nm
        self.age = ag
        self.gender = gn


st1 = INT("pooja",20,'F')

print(st1.name,st1.age,st1.gender)

print(type(st1))