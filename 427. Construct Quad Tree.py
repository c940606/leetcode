"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None
        if self.is_leaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node("*", False, self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    self.construct([row[n // 2:] for row in grid[n // 2:]])
                    )

    def is_leaf(grid):
        vals = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                vals.add(grid[i][j])
                if len(vals) > 1:
                    return False
        return True
