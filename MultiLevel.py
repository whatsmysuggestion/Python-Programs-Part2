class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20

class Derived(Base):
    def sum(self):
        return(self.geta()+self.getb())

class LastDerived(Derived):
        def avg(self):
            print(self.sum()/2)

ld=LastDerived()
ld.avg()
