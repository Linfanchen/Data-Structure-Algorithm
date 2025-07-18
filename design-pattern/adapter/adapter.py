from abc import ABC, abstractmethod


# 目标接口
class Target(ABC):
    """客户期望的接口"""

    @abstractmethod
    def request(self) -> str:
        pass


# 适配者
class Adaptee:
    """需要被适配的现有类"""

    def specific_request(self) -> str:
        return "Adaptee's specific request"


# 适配器
class Adapter(Target):
    """将Adaptee接口转换为Target接口"""

    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()}"


# 客户端代码
def client_code(target: Target) -> None:
    """客户端代码只与Target接口交互"""
    print(target.request())


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
    # 输出: Adapter: (TRANSLATED) Adaptee's specific request