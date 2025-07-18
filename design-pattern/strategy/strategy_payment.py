from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Type, Optional, Any
import inspect
from importlib import import_module
import threading


# ==================== 基础模型定义 ====================

class PaymentType(Enum):
    """支付类型枚举，定义系统支持的支付方式"""
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    CRYPTO = "crypto"
    BANK_TRANSFER = "bank_transfer"
    WECHAT_PAY = "wechat_pay"  # 扩展的新支付方式


@dataclass
class PaymentRequest:
    """支付请求数据模型"""
    amount: float  # 支付金额
    currency: str  # 货币类型
    reference: str  # 交易参考号
    metadata: Dict[str, Any] = None  # 附加元数据

    def __post_init__(self):
        """数据校验"""
        if self.amount <= 0:
            raise ValueError("Payment amount must be positive")
        if not self.reference:
            raise ValueError("Reference cannot be empty")


@dataclass
class PaymentResult:
    """支付结果数据模型"""
    success: bool  # 是否成功
    message: str  # 结果消息
    transaction_id: Optional[str] = None  # 交易ID
    fee: Optional[float] = None  # 手续费
    processing_time: Optional[float] = None  # 处理时间(毫秒)


# ==================== 策略接口和实现 ====================

class IPaymentStrategy(ABC):
    """支付策略接口（抽象基类）"""

    @abstractmethod
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """
        处理支付请求的抽象方法
        :param request: 支付请求对象
        :return: 支付结果对象
        """
        pass

    @property
    def strategy_name(self) -> str:
        """返回策略名称"""
        return self.__class__.__name__


# ----- 具体策略实现 -----

class CreditCardStrategy(IPaymentStrategy):
    """信用卡支付策略"""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        # 模拟信用卡支付处理
        print(f"[CreditCard] Processing payment of {request.amount} {request.currency}")

        # 模拟网络请求延迟
        import time
        start_time = time.time()
        time.sleep(0.5)

        return PaymentResult(
            success=True,
            message="Credit card payment processed successfully",
            transaction_id=f"CC-{request.reference}",
            fee=request.amount * 0.02,  # 2%手续费
            processing_time=(time.time() - start_time) * 1000
        )


class PayPalStrategy(IPaymentStrategy):
    """PayPal支付策略"""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[PayPal] Processing payment of {request.amount} {request.currency}")

        import time
        start_time = time.time()
        time.sleep(0.3)

        return PaymentResult(
            success=True,
            message="PayPal payment processed successfully",
            transaction_id=f"PP-{request.reference}",
            fee=request.amount * 0.03,  # 3%手续费
            processing_time=(time.time() - start_time) * 1000
        )


class CryptoStrategy(IPaymentStrategy):
    """加密货币支付策略"""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[Crypto] Processing payment of {request.amount} {request.currency}")

        import time
        start_time = time.time()
        time.sleep(1.0)  # 模拟区块链确认时间较长

        return PaymentResult(
            success=True,
            message="Crypto payment processed (pending blockchain confirmation)",
            transaction_id=f"CR-{request.reference}",
            fee=0.0,  # 假设无手续费
            processing_time=(time.time() - start_time) * 1000
        )


class BankTransferStrategy(IPaymentStrategy):
    """银行转账策略"""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[BankTransfer] Processing payment of {request.amount} {request.currency}")

        import time
        start_time = time.time()
        time.sleep(0.8)

        return PaymentResult(
            success=True,
            message="Bank transfer initiated",
            transaction_id=f"BT-{request.reference}",
            fee=5.0,  # 固定手续费5元
            processing_time=(time.time() - start_time) * 1000
        )


# ==================== 高级策略实现 ====================

class WeChatPayStrategy(IPaymentStrategy):
    """微信支付策略（扩展的新策略）"""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[WeChatPay] Processing payment of {request.amount} {request.currency}")

        import time
        start_time = time.time()
        time.sleep(0.2)  # 微信支付通常较快

        # 检查元数据中是否包含openid
        if request.metadata and 'wechat_openid' in request.metadata:
            openid = request.metadata['wechat_openid']
        else:
            return PaymentResult(
                success=False,
                message="WeChat OpenID is required",
                processing_time=(time.time() - start_time) * 1000
            )

        return PaymentResult(
            success=True,
            message="WeChat Pay processed successfully",
            transaction_id=f"WX-{request.reference}",
            fee=request.amount * 0.01,  # 1%手续费
            processing_time=(time.time() - start_time) * 1000
        )


class RetryablePaymentStrategy(IPaymentStrategy):
    """可重试的支付策略装饰器"""

    def __init__(self, wrapped_strategy: IPaymentStrategy, max_retries: int = 3):
        self._wrapped = wrapped_strategy
        self._max_retries = max_retries

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        last_error = None
        for attempt in range(1, self._max_retries + 1):
            print(f"Attempt {attempt} of {self._max_retries} with {self._wrapped.strategy_name}")
            result = self._wrapped.process_payment(request)
            if result.success:
                return result
            last_error = result.message
            # 模拟指数退避
            import time
            time.sleep(2 ** attempt)

        return PaymentResult(
            success=False,
            message=f"Failed after {self._max_retries} attempts. Last error: {last_error}",
            processing_time=0
        )


# ==================== 工厂模式实现 ====================

class PaymentStrategyFactory:
    """
    支付策略工厂类
    负责支付策略的注册、创建和管理
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        """实现单例模式"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """初始化工厂"""
        self._strategies: Dict[str, IPaymentStrategy] = {}
        self._register_default_strategies()

    def _register_default_strategies(self):
        """注册默认策略"""
        self.register_strategy(PaymentType.CREDIT_CARD, CreditCardStrategy())
        self.register_strategy(PaymentType.PAYPAL, PayPalStrategy())
        self.register_strategy(PaymentType.CRYPTO, CryptoStrategy())
        self.register_strategy(PaymentType.BANK_TRANSFER, BankTransferStrategy())

    def register_strategy(self, payment_type: PaymentType, strategy: IPaymentStrategy):
        """
        注册支付策略
        :param payment_type: 支付类型
        :param strategy: 策略实例
        """
        if not isinstance(strategy, IPaymentStrategy):
            raise ValueError("Strategy must implement IPaymentStrategy")

        self._strategies[payment_type.value] = strategy
        print(f"Registered strategy for {payment_type.value}: {strategy.strategy_name}")

    def get_strategy(self, payment_type: PaymentType) -> IPaymentStrategy:
        """
        获取支付策略实例
        :param payment_type: 支付类型
        :return: 支付策略实例
        """
        strategy = self._strategies.get(payment_type.value)
        if strategy is None:
            raise ValueError(f"No strategy registered for {payment_type.value}")
        return strategy

    def get_all_strategies(self) -> Dict[str, str]:
        """获取所有已注册策略信息"""
        return {k: v.strategy_name for k, v in self._strategies.items()}

    @classmethod
    def auto_register_strategies(cls, module_name: str):
        """
        自动发现并注册策略类
        :param module_name: 模块名（如'payment.strategies'）
        """
        try:
            module = import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and
                        issubclass(obj, IPaymentStrategy) and
                        obj != IPaymentStrategy):
                    # 从类名推断支付类型
                    type_name = name.replace("Strategy", "").upper()
                    try:
                        payment_type = PaymentType[type_name]
                        factory = cls()
                        factory.register_strategy(payment_type, obj())
                        print(f"Auto-registered {name} for {payment_type.value}")
                    except KeyError:
                        continue
        except ImportError:
            print(f"Warning: Could not import module {module_name} for auto-registration")


# ==================== 支付处理器 ====================

class PaymentProcessor:
    """
    支付处理器
    提供支付处理的统一接口
    """

    def __init__(self, factory: PaymentStrategyFactory = None):
        """
        初始化支付处理器
        :param factory: 策略工厂实例，如果为None则创建默认工厂
        """
        self._factory = factory or PaymentStrategyFactory()
        self._enable_retry = False
        self._max_retries = 3

    def enable_retry(self, max_retries: int = 3):
        """启用支付重试机制"""
        self._enable_retry = True
        self._max_retries = max_retries

    def disable_retry(self):
        """禁用支付重试机制"""
        self._enable_retry = False

    def process_payment(self, payment_type: PaymentType, request: PaymentRequest) -> PaymentResult:
        """
        处理支付请求
        :param payment_type: 支付类型
        :param request: 支付请求
        :return: 支付结果
        """
        try:
            # 获取基础策略
            strategy = self._factory.get_strategy(payment_type)

            # 应用重试装饰器（如果启用）
            if self._enable_retry:
                strategy = RetryablePaymentStrategy(strategy, self._max_retries)

            # 执行支付
            return strategy.process_payment(request)

        except Exception as e:
            return PaymentResult(
                success=False,
                message=f"Payment processing failed: {str(e)}",
                processing_time=0
            )

    def list_available_payment_methods(self) -> Dict[str, str]:
        """获取可用支付方式列表"""
        return self._factory.get_all_strategies()


# ==================== 客户端使用示例 ====================

if __name__ == "__main__":
    print("===== 支付策略工厂演示 =====")

    # 1. 创建支付处理器（自动初始化工厂）
    processor = PaymentProcessor()

    # 2. 查看可用支付方式
    print("\n可用支付方式:")
    for code, name in processor.list_available_payment_methods().items():
        print(f"- {code}: {name}")

    # 3. 创建支付请求
    payment_request = PaymentRequest(
        amount=150.75,
        currency="USD",
        reference="ORDER-2023-12345",
        metadata={
            "user_id": "user_789",
            "items": ["product_A", "service_B"],
            "wechat_openid": "oX8Z5Y1a2b3c4d5e6f7g8h9i0j"  # 微信支付需要
        }
    )

    # 4. 处理不同类型的支付
    print("\n处理信用卡支付:")
    result = processor.process_payment(PaymentType.CREDIT_CARD, payment_request)
    print(f"结果: {result}")

    print("\n处理PayPal支付:")
    result = processor.process_payment(PaymentType.PAYPAL, payment_request)
    print(f"结果: {result}")

    # 5. 动态注册新策略
    print("\n动态注册微信支付策略:")
    factory = PaymentStrategyFactory()
    factory.register_strategy(PaymentType.WECHAT_PAY, WeChatPayStrategy())

    print("\n处理微信支付:")
    result = processor.process_payment(PaymentType.WECHAT_PAY, payment_request)
    print(f"结果: {result}")

    # 6. 测试重试机制
    print("\n测试重试机制:")
    processor.enable_retry(max_retries=2)

    # 模拟一个会失败的支付请求（没有openid）
    bad_request = PaymentRequest(
        amount=200.0,
        currency="USD",
        reference="ORDER-2023-54321",
        metadata={"user_id": "user_123"}  # 缺少wechat_openid
    )

    print("\n处理会失败的微信支付（测试重试）:")
    result = processor.process_payment(PaymentType.WECHAT_PAY, bad_request)
    print(f"最终结果: {result}")

    # 7. 自动发现并注册策略
    print("\n尝试自动发现策略:")
    # 假设我们有一个payment_strategies模块包含策略类
    PaymentStrategyFactory.auto_register_strategies("payment_strategies")