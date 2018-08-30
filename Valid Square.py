class Solution(object):
	def validSquare(self, p1, p2, p3, p4):
		"""
		给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
		一个点的坐标（x，y）由一个有两个整数的整数数组表示。
		---
		输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
		输出: True
		---
		思路：
		证明 四条边相等 加一个直角
		先 求 q1 与 其他点 的长度
		两个短的 和 一个长的
		短的 是 边长 长的 是 对角线
		找到 临近点 和 对角点
		:type p1: List[int]
		:type p2: List[int]
		:type p3: List[int]
		:type p4: List[int]
		:rtype: bool
		"""
		e12 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
		e13 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
		e14 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
		if e12 == 0 or e13 == 0 or e14 == 0:
			return False
		if e12 == e13:
			if e12 + e13 == e14:
				e24 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
				e34 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
				if e24 == e34 == e12:
					return True
				else:
					return False
			else:
				return False
		elif e12 == e14:
			if e12 + e14 == e13:
				e23 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
				e34 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
				if e23 == e34 == e12:
					return True
				else:
					return False
			else:
				return False
		elif e13 == e14:
			# print("kjdfk")
			if e13 + e14 == e12:
				e23 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
				e24 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
				if e23 == e24 == e13 :
					return True
				else:
					return False
			else:
				return False
		else:
			return False
a = Solution()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(a.validSquare(p1,p2,p3,p4))

