class Test():
    class_attr = 5

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def hello():
        print('hello')
        return True

    @staticmethod
    def hi():
        Test.hello()
        print('hii')
        return

    @classmethod
    def method_test(cls):
        cls.hello()
        cls.class_attr = 0
        return True

    def manger(self):
        self.class_attr = 10



hello = Test(['poivre', 'sel'])
hello2 = Test('tomatoes')

Test.hi()