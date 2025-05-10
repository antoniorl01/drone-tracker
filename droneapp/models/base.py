class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('No previous instances, creating a new one...')
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)