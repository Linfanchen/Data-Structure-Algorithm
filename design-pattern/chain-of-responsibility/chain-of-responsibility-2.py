from abc import ABC, abstractmethod
from typing import Optional

class PurchaseRequest:
    """购买请求类"""

    def __init__(self, amount: float, purpose: str):
        self.amount = amount
        self.purpose = purpose


class Approver(ABC):
    """审批者抽象类"""

    def __init__(self, name: str, approval_limit: float):
        self.name = name
        self.approval_limit = approval_limit
        self._next_approver: Optional['Approver'] = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        self._next_approver = approver
        return approver

    def process_request(self, request: PurchaseRequest) -> bool:
        if request.amount <= self.approval_limit:
            self._approve(request)
            return True
        elif self._next_approver is not None:
            return self._next_approver.process_request(request)
        else:
            self._reject(request)
            return False

    def _approve(self, request: PurchaseRequest) -> None:
        print(f"{self.name} approved purchase of {request.purpose} for ${request.amount}")

    def _reject(self, request: PurchaseRequest) -> None:
        print(f"Request for {request.purpose} (${request.amount}) was rejected")


class Manager(Approver):
    """经理审批者"""
    pass


class Director(Approver):
    """总监审批者"""
    pass


class VP(Approver):
    """副总裁审批者"""
    pass


def purchase_example():
    # 创建审批链
    manager = Manager("Manager John", 1000)
    director = Director("Director Lisa", 5000)
    vp = VP("VP Mike", 10000)

    manager.set_next(director).set_next(vp)

    # 处理购买请求
    requests = [
        PurchaseRequest(800, "Office supplies"),
        PurchaseRequest(3500, "Conference tickets"),
        PurchaseRequest(9000, "New server"),
        PurchaseRequest(12000, "Company retreat")
    ]

    for request in requests:
        print(f"\nProcessing request: {request.purpose} (${request.amount})")
        if not manager.process_request(request):
            print("No one was able to approve this purchase.")


if __name__ == "__main__":
    purchase_example()