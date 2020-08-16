class Solution:
    def isConvex1(self, points):
        n = len(points)
        pre = 0
        for i in range(n):
            x1 = points[(i + 1) % n][0] - points[i][0]
            x2 = points[(i + 2) % n][0] - points[i][0]
            y1 = points[(i + 1) % n][1] - points[i][1]
            y2 = points[(i + 2) % n][1] - points[i][1]
            cur = x1 * y2 - x2 * y1
            if cur != 0:
                if cur * pre < 0:
                    return False
                else:
                    pre = cur
        return True

    def isConvex(self, points: List[List[int]]) -> bool:

        """:arg
        叉乘
        设A(x1,y1),B(x2,y2),C(x3,y3),则三角形两边的矢量分别是： 
        AB=(x2-x1,y2-y1), AC=(x3-x1,y3-y1)   
       则AB和AC的叉积为：(2*2的行列式)    
        |x2-x1, y2-y1|    
        |x3-x1, y3-y1|   
        值为：(x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)   
        利用右手法则进行判断：  
        如果AB*AC>0,则三角形ABC是逆时针的
        如果AB*AC<0,则三角形ABC是顺时针的
        """

        def cal_cross_product(A, B, C):
            AB = [B[0] - A[0], B[1] - A[1]]
            AC = [C[0] - A[0], C[1] - A[1]]
            return AB[0] * AC[1] - AB[1] * AC[0]

        flag = 0
        n = len(points)
        for i in range(n):
            # cur > 0 表示points是按逆时针输出的;cur < 0,顺时针
            cur = cal_cross_product(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if cur != 0:
                # 说明异号, 说明有个角大于180度
                if cur * flag < 0:
                    return False
                else:
                    flag = cur
        return True
