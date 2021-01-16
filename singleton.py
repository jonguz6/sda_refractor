class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + self.val

    __instance = None

    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance

x = Singleton()
x.val = 'test01'
print(x)
y = Singleton()
print(y)
y.val = 'test02'
print(y)
print(x)
