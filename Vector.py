class vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def getlength(self):
        return (self.x + self.y)
    
    def normalize(self):
        length = self.getlength()
        return vector(self.x / length, self.y / length)
    
    def distance(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.Y
        return (diff_x + diff_y)
    
vector1 = vector(3,3)
vector2 = vector(5,2)


result = vector.getlength(vector1)
print(result)

