from abc import ABC, abstractmethod

""" 
实现流程：

1. 定义抽象产品接口
  - 使用ABC和@abstractmethod创建抽象基类
  - 定义产品必须实现的接口方法
2. 实现具体产品类
  - 每个具体产品必须实现抽象产品定义的接口
  - 可以添加产品特有的方法和属性
3. 定义抽象工厂接口
  - 工厂方法通常返回抽象产品类型
  - 工厂方法可以有参数，用于决定创建哪种具体产品
4. 实现具体工厂类
  - 每个具体工厂负责创建一种具体产品
  - 工厂方法返回具体产品实例
5. 客户端使用
  - 客户端只依赖抽象工厂和抽象产品
  - 通过传入不同的工厂来创建不同的产品
  - 客户端代码不需要知道具体产品类
"""

class Payment(ABC):
    """ 抽象产品 """
    @abstractmethod
    def pay(self, amount):
        pass

class Alipay(Payment):
    """ 具体产品 - 支付宝支付 """
    def pay(self, amount):
        print(f"使用支付宝支付了{amount}元")

class WechatPay(Payment):
    """ 具体产品 - 微信支付 """
    def pay(self, amount):
        print(f"使用微信支付了{amount}元")

class BankPay(Payment):
    """ 具体产品 - 银行卡支付 """
    def pay(self, amount):
        print(f"使用银行卡支付了{amount}元")

class PaymentFactory(ABC):
    """ 抽象工厂 """
    def create_payment(self):
        pass

class AliPayFactory(PaymentFactory):
    """ 具体工厂 - 支付宝支付工厂 """
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory):
    """ 具体工厂 - 微信支付工厂 """
    def create_payment(self):
        return WechatPay()

class BankPayFactory(PaymentFactory):
    """ 具体工厂 - 银行卡支付工厂 """
    def create_payment(self):
        return BankPay()

def client_pay(factory: PaymentFactory, amount):
    """ 支付客户端 """
    payment = factory.create_payment()
    payment.pay(amount)

if __name__ == '__main__':
    # 使用支付宝支付
    alipay_factory = AliPayFactory()
    client_pay(alipay_factory, 100)

    # 使用微信支付
    wechat_factory = WechatPayFactory()
    client_pay(wechat_factory, 200)

    # 使用银行卡支付
    bank_factory = BankPayFactory()
    client_pay(bank_factory, 300)
