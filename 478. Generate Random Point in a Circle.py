import math
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        l = self.radius * math.sqrt(random.random())
        deg = random.random() * math.pi * 2
        x = l * math.cos(deg) + self.x_center
        y = l * math.sin(deg) + self.y_center
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
