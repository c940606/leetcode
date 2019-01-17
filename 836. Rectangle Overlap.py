class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        一维重叠必要充分条件
        一个坐标的横坐标一定要小于另一个坐标纵坐标
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

a = Solution()
print(a.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))