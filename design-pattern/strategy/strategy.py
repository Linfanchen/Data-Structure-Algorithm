from abc import ABC, abstractmethod
from typing import List


# 策略接口
class SortStrategy(ABC):
    """排序策略抽象类"""

    @abstractmethod
    def sort(self, data: List) -> List:
        pass


# 具体策略
class BubbleSortStrategy(SortStrategy):
    """冒泡排序策略"""

    def sort(self, data: List) -> List:
        print("使用冒泡排序")
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortStrategy(SortStrategy):
    """快速排序策略"""

    def sort(self, data: List) -> List:
        print("使用快速排序")
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class MergeSortStrategy(SortStrategy):
    """归并排序策略"""

    def sort(self, data: List) -> List:
        print("使用归并排序")
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        return self._merge(left, right)

    def _merge(self, left: List, right: List) -> List:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


# 上下文
class Sorter:
    """排序上下文"""

    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy or QuickSortStrategy()  # 默认使用快速排序

    def set_strategy(self, strategy: SortStrategy):
        """设置排序策略"""
        self._strategy = strategy

    def perform_sort(self, data: List) -> List:
        """执行排序"""
        if not data:
            return data
        return self._strategy.sort(data.copy())


# 客户端代码
def main():
    data = [9, 2, 5, 1, 7, 3, 8, 6, 4]
    sorter = Sorter()

    print("原始数据:", data)

    # 使用冒泡排序
    sorter.set_strategy(BubbleSortStrategy())
    print("排序结果:", sorter.perform_sort(data))

    # 使用归并排序
    sorter.set_strategy(MergeSortStrategy())
    print("排序结果:", sorter.perform_sort(data))

    # 使用快速排序
    sorter.set_strategy(QuickSortStrategy())
    print("排序结果:", sorter.perform_sort(data))


if __name__ == "__main__":
    main()