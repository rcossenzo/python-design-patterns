class SingletonMeta(type):
    
    _instances = {}

    def __call__(cls, *args, **kwargs) -> None:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        # here goes any kind of business logic
        print('my business logic')


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.some_business_logic()
    s2.some_business_logic()
    if id(s1) == id(s2):
        print("singleton works")
    else:
        print("singleton is not working")