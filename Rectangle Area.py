class Solution(object):
    def computeArea1(self, A, B, C, D, E, F, G, H):
        """
        在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
        每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
        Rectangle Area
        示例:
        输入: -3, 0, 3, 4, 0, -1, 9, 2 输出: 45
        说明: 假设矩形面积不会超出 int 的范围。
        ----
        思路 x 轴的交集
            y 轴的交集
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        all_area = abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F)
        # print(all_area)
        length = [A, C, E, G]
        width = [B, D, F, H]
        max_length = max(length)
        length.remove(max_length)
        min_length = min(length)
        length.remove(min_length)
        max_width = max(width)
        width.remove(max_width)
        min_width = min(width)
        width.remove(min_width)
        if min(A, C) > max(E, G) or max(A, C) < min(E, G) or min(B, D) > max(F, H) or max(B, D) < min(F, H):
            return all_area
        rea = abs(length[0] - length[1]) * abs(width[0] - width[1])
        return all_area - rea

    def computeArea(self, A, B, C, D, E, F, G, H):
        # 调整两个矩形位置, 让第一个矩形靠最左边
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        # 没有重叠的情况
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 重叠情况
        # xia
        down = max(A, E)
        # shang
        up = min(C, G)
        # zuo
        left = max(B, F)
        # you
        right = min(D, H)
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)


a = Solution()
print(a.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
print(a.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))
print(a.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
