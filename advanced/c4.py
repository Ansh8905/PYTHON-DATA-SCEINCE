class shape:

    def __init__(self ,side):
        self.side = side

    def info (self):
        return f'shape with {self.side} shapes'


class rectangle(shape):

    def __init__(self, l, w):
        super().__init__(l)
        self.w = w

def area(self):
    return self.side * self.w #side is taken AS length

#overidden function
def info(self):
    return f'rectangle with l = {self.side} & w = {self.w}'


ob1 = shape(4)
print(ob1.info())

ob2 = rectangle(4,5)
print(ob1.info())
print(ob2.info())


