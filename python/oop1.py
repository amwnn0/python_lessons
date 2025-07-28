class Point:
    color = "red"
    circle = 2

    def __new__(cls, *args, **kwargs):
        print("__new__ for" + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("__init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("__del__")

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


class DataBase:
    "singletone, существует только один объект класса DataBase"

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"connecting: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("closing")

    def read(self):
        return "data from DB"

    def write(self, data):
        print(f"writing {data}")


class Vector:
    "@classmethod and @staticmethod"

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x * x + y * y

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y


v = Vector(10, 20)
