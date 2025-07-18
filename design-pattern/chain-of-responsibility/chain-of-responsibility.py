from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """抽象处理者"""

    def __init__(self):
        self._next_handler: Optional[Handler] = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        """设置下一个处理者"""
        self._next_handler = handler
        return handler  # 返回handler以便链式调用

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        """处理请求的方法"""
        pass

    def _pass_to_next(self, request) -> Optional[str]:
        """将请求传递给下一个处理者"""
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandlerA(Handler):
    """具体处理者A"""

    def handle(self, request) -> Optional[str]:
        if request == "A":
            return f"Handler A processed request {request}"
        else:
            print("Handler A can't process, passing to next")
            return self._pass_to_next(request)


class ConcreteHandlerB(Handler):
    """具体处理者B"""

    def handle(self, request) -> Optional[str]:
        if request == "B":
            return f"Handler B processed request {request}"
        else:
            print("Handler B can't process, passing to next")
            return self._pass_to_next(request)


class ConcreteHandlerC(Handler):
    """具体处理者C"""

    def handle(self, request) -> Optional[str]:
        if request == "C":
            return f"Handler C processed request {request}"
        else:
            print("Handler C can't process, passing to next")
            return self._pass_to_next(request)


def client_code(handler: Handler) -> None:
    """客户端代码"""
    for request in ["A", "B", "C", "D"]:
        print(f"\nClient: Who wants to handle '{request}'?")
        result = handler.handle(request)
        if result:
            print(result)
        else:
            print(f"Request {request} was left unhandled.")


if __name__ == "__main__":
    # 构建责任链
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()

    handler_a.set_next(handler_b).set_next(handler_c)

    # 客户端调用
    print("Chain: A > B > C")
    client_code(handler_a)