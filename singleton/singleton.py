import threading


class Singleton:
    """使用类"""
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton()

        return Singleton._instance


class Singleton2:
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton2._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton2._instance = super().__new__(cls)

        return Singleton2._instance
