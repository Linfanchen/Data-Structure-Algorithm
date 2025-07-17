import  copy
from abc import ABC, abstractmethod

"""
**实现步骤**

- 定义抽象原型接口：
  - 声明克隆方法
  - 定义对象的基本接口
- 实现具体原型类：
  - 实现克隆方法（深拷贝或浅拷贝）
  - 包含必要的初始化逻辑
- 创建原型管理器（可选）：
  - 存储常用原型
  - 提供克隆接口
- 客户端使用：
  - 从原型管理器获取原型
  - 克隆并修改新对象
"""

class DocumentPrototype(ABC):
    """ 抽象原型 """
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

class ReportDocument(DocumentPrototype):
    """ 具体文档 - 报告 """
    def __init__(self, title, content, charts):
        self.title = title
        self.content = content
        self.charts = charts
        self.load_resources()

    def load_resources(self):
        print(f"加载报表资源: {self.title}...")
        # 这里模拟耗时的资源加载过程

    def clone(self):
        """深拷贝实现克隆"""
        return copy.deepcopy(self)

    def display(self):
        print(f"=== {self.title} ===")
        print(self.content)
        print(f"包含图表: {self.charts}\n")

class LetterDocument(DocumentPrototype):
    """ 具体文档 - 信件 """
    def __init__(self, header, body, footer):
        self.header = header
        self.body = body
        self.footer = footer
        self.format_document()  # 模拟格式初始化

    def format_document(self):
        print("初始化信件格式...")
        # 这里模拟格式初始化过程

    def clone(self):
        """浅拷贝实现克隆"""
        return copy.copy(self)

    def display(self):
        print(f"信件头: {self.header}")
        print(f"信件内容: {self.body}")
        print(f"信件尾: {self.footer}\n")

class DocumentManager:
    """ 原型管理器 """
    def __init__(self):
        self.prototypes = {}

    def register(self, name, prototype):
        self.prototypes[name] = prototype

    def unregister(self, name):
        del self.prototypes[name]

    def clone_document(self, name, **attrs):
        prototype = self.prototypes.get(name)
        if not prototype:
            raise ValueError(f"未知文档类型: {name}")

        cloned = prototype.clone()
        # 更新克隆对象的属性
        for key, value in attrs.items():
            setattr(cloned, key, value)
        return cloned

if __name__ == "__main__":
    # 初始化原型管理器
    manager = DocumentManager()

    # 创建并注册原型
    annual_report = ReportDocument(
        "年度报告",
        "公司2023年度财务数据...",
        ["销售趋势图", "利润分布图"]
    )
    manager.register("report", annual_report)

    official_letter = LetterDocument(
        "尊敬的客户：",
        "感谢您一直以来的支持...",
        "此致敬礼"
    )
    manager.register("letter", official_letter)

    print("=== 使用原型创建文档 ===")
    # 克隆年度报告并修改
    report1 = manager.clone_document("report")
    report1.display()

    report2 = manager.clone_document(
        "report",
        title="季度报告",
        content="2023年Q4财务数据..."
    )
    report2.display()

    # 克隆信件并修改
    letter1 = manager.clone_document("letter")
    letter1.display()

    letter2 = manager.clone_document(
        "letter",
        body="您的账户即将到期，请及时续费..."
    )
    letter2.display()