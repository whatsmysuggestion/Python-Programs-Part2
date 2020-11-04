class Map:
    def __init__(self, iterate):
        self.list = []
        self.__kkar(iterate)

    def kkar(self, iterate):
        for item in iterate:
            self.list.append(item)
        print(self.list)

    __kkar = kkar

s=Map([1,2,3,4,5,6,7])

