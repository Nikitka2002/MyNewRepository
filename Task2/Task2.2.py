class Human:
    def getName(self):
        return self.name * 3
    def setName(self, name):
        self.name  = name.reverse()
    def delName(self):
        del self.name
    name = property(getName, setName, delName, "Nikita")

Man = Human()
Man.name = "Nikita"
print(Man.name)
del Man.name
