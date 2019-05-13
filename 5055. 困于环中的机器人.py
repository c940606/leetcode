class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 方向 北 东 南 西
        loc = [0, 0]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        for cmd in instructions:
            if cmd == "L":
                i = (i - 1) % 4
            elif cmd == "R":
                i = (i + 1) % 4
            else:
                # print(loc, i)
                loc = [l + d for l, d in zip(loc, dirs[i])]
        return i != 0 or (loc[0] == 0 and loc[1] == 0)


a = Solution()
print(a.isRobotBounded("GRLLRLLLLGLLLGLLRGLLGRLLLRLLLLRLLGGGGGGLGLRRGLLGLG"))
print(a.isRobotBounded("GGLLGG"))
print(a.isRobotBounded("GG"))
