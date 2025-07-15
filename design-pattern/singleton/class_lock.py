import threading

class Singleton:
    """ 类实现
        1. 定义私有的实例变量和锁
        2. 重写 __new__ 方法
        3. 获取锁，判断实例是否已经创建
        4. 调用父类的__new__创建实例
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                # 双重检查
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

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