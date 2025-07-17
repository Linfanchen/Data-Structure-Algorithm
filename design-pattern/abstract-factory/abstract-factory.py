from abc import ABC, abstractmethod

"""
实现步骤：
 - 定义抽象产品接口（如 Button、Textbox）。
 - 为每个平台实现具体产品类（如 WinButton、MacButton）。
 - 定义抽象工厂接口，声明创建产品的方法。
 - 为每个平台实现具体工厂类（如 WindowsFactory、MacOSFactory）。
 - 客户端通过抽象工厂接口创建产品，运行时选择具体工厂。
"""

class Button(ABC):
    """ 抽象产品 - 按钮 """
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    """ 抽象产品 - 复选框 """
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    """ 具体产品 - Windows - 按钮 """
    def render(self):
        print("渲染一个Windows风格的按钮")

class WindowsCheckBox(CheckBox):
    """ 具体产品 - Windows - 复选框 """
    def render(self):
        print("渲染一个Windows风格的复选框")

class MacButton(Button):
    """ 具体产品 - Mac - 按钮 """
    def render(self):
        print("渲染一个Mac风格的按钮")

class MacCheckBox(CheckBox):
    """ 具体产品 - Mac - 复选框 """
    def render(self):
        print("渲染一个Mac风格的复选框")

class GUIFactory(ABC):
    """ 抽象工厂 """
    @abstractmethod
    def create_button(self) -> Button:
        """ 创建按钮 """
        pass

    def create_checkbox(self) -> CheckBox:
        """ 创建复选框 """
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()

def client_gui(factory: GUIFactory):
    """ 渲染客户端 """
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

if __name__ == '__main__':
    print("客户端: 使用Windows工厂")
    client_gui(WindowsFactory())

    print("\n客户端: 使用Mac工厂")
    client_gui(MacFactory())
