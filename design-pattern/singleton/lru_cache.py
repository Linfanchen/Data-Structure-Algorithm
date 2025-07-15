import functools, threading

class Singleton:
    """ 类 """
    pass

@functools.lru_cache()
def create_singleton():
    """ 创建单例
        多线程场景下只会调用一次
    """
    singleton = Singleton()
    print(f"\n Logger instance id: {id(singleton)} \n")

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_singleton)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()