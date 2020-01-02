from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.queue = deque([(0, 0)])
        self.num = 0
        self.food = food
        self.n = len(food)

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.queue[-1]
        lookup = {
            "U": [-1, 0],
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1]
        }

        def helper(dirs):
            nonlocal x, y
            if x + dirs[0] < 0 or x + dirs[0] >= self.height or y + dirs[1] < 0 or y + dirs[1] >= self.width or (
                    (x + dirs[0], y + dirs[1]) in self.queue and (x + dirs[0], y + dirs[1]) != self.queue[0]): return -1
            if self.num >= self.n or [x + dirs[0], y + dirs[1]] != self.food[self.num]:
                self.queue.popleft()
                self.queue.append((x + dirs[0], y + dirs[1]))
                return self.num
            else:
                self.queue.append((x + dirs[0], y + dirs[1]))
                self.num += 1
                return self.num

        return helper(lookup[direction])

        # if direction == "U":
        #     if x - 1 < 0 or ((x - 1, y) in self.queue and (x - 1, y) != self.queue[0]): return -1
        #     if self.num >= self.n or [x - 1, y] != self.food[self.num]:
        #         self.queue.popleft()
        #         self.queue.append((x - 1, y))
        #         return self.num
        #     else:
        #         self.queue.append((x - 1, y))
        #         self.num += 1
        #         return self.num
        # elif direction == "D":
        #     if x + 1 >= self.height or ((x + 1, y) in self.queue and (x + 1, y) != self.queue[0]): return -1
        #     if self.num >= self.n or [x + 1, y] != self.food[self.num]:
        #         self.queue.popleft()
        #         self.queue.append((x + 1, y))
        #         return self.num
        #     else:
        #         self.queue.append((x + 1, y))
        #         self.num += 1
        #         return self.num
        # elif direction == "L":
        #     if y - 1 < 0 or ((x, y - 1) in self.queue and (x, y - 1) != self.queue[0]): return -1
        #     if self.num >= self.n or [x, y - 1] != self.food[self.num]:
        #         self.queue.popleft()
        #         self.queue.append((x, y - 1))
        #         return self.num
        #     else:
        #         self.queue.append((x, y - 1))
        #         self.num += 1
        #         return self.num
        # elif direction == "R":
        #     if y + 1 >= self.width or ((x, y + 1) in self.queue and (x, y + 1) != self.queue[0]): return -1
        #     if self.num >= self.n or [x, y + 1] != self.food[self.num]:
        #         self.queue.popleft()
        #         self.queue.append((x, y + 1))
        #         return self.num
        #     else:
        #         self.queue.append((x, y + 1))
        #         self.num += 1
        #         return self.num

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
