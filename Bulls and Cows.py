class Solution(object):
	def getHint(self, secret, guess):
		"""
		你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，
		告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），
		有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。
		请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
		请注意秘密数字和朋友的猜测数都可能含有重复数字。
		---
		输入: secret = "1807", guess = "7810"
		输出: "1A3B"
		解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
		---
		思路：
		1. 把secret用哈希表表示，key 为 值 val 为索引的列表
		2. 循环 guess
			如果 键 和 索引 都是一样的就是公牛 ，然后把索引去除
			如果 键 但 索引 不一样 就是奶牛 ，然后把索引去除

		:type secret: str
		:type guess: str
		:rtype: str
		"""
		lookup1 = {}
		lookup2 = {}
		bulls = 0
		cows = 0
		for index,key in enumerate(secret):
			if key in lookup1:
				lookup1[key].append(index)
			else:
				lookup1[key] = [index]
		for index, key in enumerate(guess):
			if key in lookup2:
				lookup2[key].append(index)
			else:
				lookup2[key] = [index]
		for key,val in lookup2.items():
			if key in lookup1:
				secret_temp = set(lookup1[key])
				guess_temp = set(val)
				temp1 = secret_temp&guess_temp
				bulls += len(temp1)

				temp =min( len(guess_temp-temp1) , len(secret_temp-temp1))

				cows += temp
		return str(bulls)+"A"+str(cows)+"B"


a = Solution()
print(a.getHint("1123","0111"))
