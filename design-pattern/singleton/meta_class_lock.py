import threading

class SingletonType(type):
    """ 元类
        1. 定义类实例字典和锁
        2. 重写__call__
        3. 获取锁，并且调用父类的__call__
        4. 返回实例

    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonType):
    """ 实例类 """
    pass

def create_singleton():
    """ 创建单例 """
    singleton = Singleton()
    print(f"Logger instance id: {id(singleton)} \n")

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_singleton)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()