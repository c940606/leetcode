# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()

        def helper(x, y, dir):
            robot.clean()
            visited.add((x, y))
            for i in range(4):
                cur = (i + dir) % 4
                tmp_x = x + dirs[cur][0]
                tmp_y = y + dirs[cur][1]
                if (tmp_x, tmp_y) not in visited and robot.move():
                    helper(tmp_x, tmp_y, cur)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnRight()

        helper(robot.row, robot.col, 0)
