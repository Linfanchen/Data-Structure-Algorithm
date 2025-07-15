import threading
from threading import Lock
import time


def singleton(cls):
    """ 设计要点：
        1. 定义空的实例变量
        2. 定义闭包函数
        3. 获取锁
        4. 没有则创建，有则返回 get_instance 闭包
    """
    instances = {}
    lock = Lock()

    def get_instance(*args, **kwargs):
        # 用于在嵌套函数中修改外层（非全局）作用域的变量。
        nonlocal instances
        if cls not in instances:
            with lock:
                # 双重检查
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        # 到这里，无论新建还是旧的，已经保证存在实例了
        return instances[cls]

    return get_instance


@singleton
class Logger:
    """ 日志类 """
    def __init__(self):
        time.sleep(0.1)  # 模拟初始化耗时

def create_logger():
    """ 创建日志实例 """
    logger = Logger()
    print(f"Logger instance id: {id(logger)} \n")


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_logger)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()