from abc import ABC, abstractmethod

""" 
实现步骤:
（以构建一台电脑为例）
- 定义产品类 Computer，包含多个可选部件。
- 定义抽象建造者接口 ComputerBuilder，声明构建各部件的方法。
- 实现具体建造者 GamingComputerBuilder、OfficeComputerBuilder。
- 可选：定义指挥者 Director，封装构建流程。
- 客户端通过建造者或 Director 构建对象。
"""

class Computer:
    """ 产品类 """
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.disk = None
        self.gpu = None

    def __str__(self):
        return f"Computer配置:\nCPU: {self.cpu}\n内存: {self.memory}\n硬盘: {self.disk}\n显卡: {self.gpu}"

class ComputerBuilder(ABC):
    """ 抽象建造者 """
    @abstractmethod
    def add_cpu(self, cpu: str):
        pass

    @abstractmethod
    def add_memory(self, memory: str):
        pass

    @abstractmethod
    def add_disk(self, disk: str):
        pass

    @abstractmethod
    def add_gpu(self, gpu: str):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass

class GamingComputerBuilder(ComputerBuilder):
    """ 具体建造者 - 游戏 """
    def __init__(self):
        # 创建对象，下面为其添加属性
        self.computer = Computer()

    def add_cpu(self, cpu: str):
        self.computer.cpu = f"⚡超频版 {cpu}"

    def add_memory(self, memory: str):
        self.computer.memory = f"🔥高频 {memory}"

    def add_disk(self, disk: str):
        self.computer.disk = f"🚀极速 {disk}"

    def add_gpu(self, gpu: str):
        self.computer.gpu = f"🎮游戏级 {gpu}"

    def get_computer(self) -> Computer:
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    """ 具体建造者 - 办公 """
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu: str):
        self.computer.cpu = f"🖥️ 节能版 {cpu}"

    def add_memory(self, memory: str):
        self.computer.memory = f"📊标准 {memory}"

    def add_disk(self, disk: str):
        self.computer.disk = f"💾普通 {disk}"

    def add_gpu(self, gpu: str):
        self.computer.gpu = f"📈集成 {gpu}"

    def get_computer(self) -> Computer:
        return self.computer

class Director:
    """ 指挥者 """
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_gaming_computer(self):
        """构建高性能游戏电脑"""
        self.builder.add_cpu("Intel i9-12900K")
        self.builder.add_memory("32GB DDR5")
        self.builder.add_disk("2TB NVMe SSD")
        self.builder.add_gpu("NVIDIA RTX 4090")
        return self.builder.get_computer()

    def construct_office_computer(self):
        """构建标准办公电脑"""
        self.builder.add_cpu("Intel i5-12400")
        self.builder.add_memory("16GB DDR4")
        self.builder.add_disk("512GB SSD")
        self.builder.add_gpu("Intel UHD Graphics 730")
        return self.builder.get_computer()

    def construct_custom_computer(self, cpu, memory, disk, gpu):
        """构建自定义配置电脑"""
        self.builder.add_cpu(cpu)
        self.builder.add_memory(memory)
        self.builder.add_disk(disk)
        self.builder.add_gpu(gpu)
        return self.builder.get_computer()


if __name__ == '__main__':
    print("=== 游戏电脑 ===")
    gaming_builder = GamingComputerBuilder()
    director = Director(gaming_builder)
    gaming_pc = director.construct_gaming_computer()
    print(gaming_pc)

    print("\n=== 办公电脑 ===")
    office_builder = OfficeComputerBuilder()
    director = Director(office_builder)
    office_pc = director.construct_office_computer()
    print(office_pc)

    print("\n=== 自定义配置 ===")
    custom_builder = GamingComputerBuilder()
    director = Director(custom_builder)
    custom_pc = director.construct_custom_computer(
        "AMD Ryzen 9 7950X",
        "64GB DDR5",
        "4TB SSD",
        "AMD Radeon RX 7900 XTX"
    )
    print(custom_pc)
