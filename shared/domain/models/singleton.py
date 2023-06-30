
class Singleton:
    instances = {}

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            if cls not in self.instances:
                self.instances[cls] = cls(*args, **kwargs)
            return self.instances[cls]
        return wrapper

