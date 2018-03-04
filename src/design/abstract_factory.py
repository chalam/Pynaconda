class Circle:
    def draw(self):
        print('Circle')
class Square:
    def draw(self):
        print('Square')
class Rectangle:
    def draw(self):
        print('Rectangle')
class Red:
    def fill(self):
        print('Red')
class Green:
    def fill(self):
        print('Green')
class Blue:
    def fill(self):
        print('Blue')

class ShapeFactory:
    types = {
        'circle': Circle,
        'square': Square,
        'rectangle': Rectangle,
    }
    @classmethod
    def create_shape(cls, type):
        return cls.types.get(type.lower())
class ColorFactory:
    types = {
        'red': Red,
        'green': Green,
        'blue': Blue,
    }
    @classmethod
    def create_color(cls, type):
        return cls.types.get(type.lower())

class DefaultFactoryProducer:
    @classmethod
    def create_shape(cls, type):
        return ShapeFactory.create_shape('circle')
    @classmethod
    def create_color(cls, type):
        return ColorFactory.create_color('red')


class AbstractFactory:
    factory = DefaultFactoryProducer
    def build(self, shape_type, color_type):
        self.shape = type(self).factory.create_shape(shape_type)
        self.color = type(self).factory.create_color(color_type)
        return self
    def do_work(self):
        print('{} in {}'.format(self.shape, self.color))

if __name__ == '__main__':
    thing = AbstractFactory().build(None, None)
    thing.do_work()
