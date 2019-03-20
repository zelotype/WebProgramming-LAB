class Cookie():
    def __init__(self, shape, size, cookie_type):
        self.shape = shape
        self.size = size
        self.cookie_type = cookie_type
        self.status = 'raw'

    def __str__(self):
        return 'My %s Cookie' % self.cookie_type

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size
    
    def __eq__(self, other):
        return self.size == other.size

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = 'Shape of cookie is ' + value

    def bake(self):
        self.status = 'BAKED!'
        print('The cookie is ' + self.status)

    @staticmethod
    def cut():
        print('The cookie is cut.')

cookie1 = Cookie('Star', 20, 'chocolate')
cookie2 = Cookie('Rectagular', 10, 'butter')
print(cookie1.shape)
print(cookie2.shape) 

cookie1.shape = 'round'
print(cookie1.shape)

cookie1.bake()
print(cookie1.status)

cookie1.cut()

print(cookie1)
print(cookie1 < cookie2)
print(cookie1 > cookie2)