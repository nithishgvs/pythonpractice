class Items:
    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"Items(name={self.name!r}, age={self.age}, cash={self.cash})"


def test():
    obj = Items("sai", 11, 11.0)
    obj1 = Items("abc", 12, 18.0)
    obj2 = Items("kkk", 61, 22.0)

    items = [obj, obj1, obj2]

    items_name = sorted(items, key=lambda x: x.name)
    items_age = sorted(items, key=lambda x: x.age)
    items_cash = sorted(items, key=lambda x: x.cash, reverse=True)

    print(items_cash)
