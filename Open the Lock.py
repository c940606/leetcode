class Solution(object):
	def openLock(self, deadends, target):
		"""
		:type deadends: List[str]
		:type target: str
		:rtype: int
		"""
		from collections import deque
		q = deque() #定义队列
		visited = set() #定义一个记录已经访问的密码
		deadends = set(deadends) # 变成集合，集合查询时间复杂度O(1)
		# 如果“0000”在死亡数字，满足直接输出
		if "0000" in deadends: return -1
		# 先把”0000“加入相应的队列和在标记已访问
		q.appendleft("0000")
		visited.add("0000")
		# 记录拨动一位密码次数
		step = 0
		while q:
			# 队列长度
			n = len(q)
			while n:
				# 队头出
				s = q.pop()
				# 判断是否死亡密码和是否为目标密码
				if s in deadends:
					n -= 1
					continue
				if s in target:
					return step
				# 改变不同为的数字
				for i in range(4):
					# 把这位数加1，减1 当然当为0,9要特殊考虑，
					if s[i] == "0":
						temp1 = s[:i] + "9" + s[i+1:]
						temp2 = s[:i] + "1" + s[i+1:]
					elif s[i] == "9":
						temp1 = s[:i] + "8" + s[i+1:]
						temp2 = s[:i] + "0" + s[i+1:]
					else:
						temp1 = s[:i] + str(int(s[i])-1) + s[i+1:]
						temp2 = s[:i] + str(int(s[i])+1) + s[i+1:]
					# print(temp1,temp2)
					# 把得到的两个密码加入队列
					if temp1 not in visited and temp1 not in deadends:
						q.appendleft(temp1)
						visited.add(temp1)
					if temp2 not in visited and temp2 not in deadends:
						q.appendleft(temp2)
						visited.add(temp2)
				# 队列个数减一
				n -= 1
			#步数加1
			step += 1
		return -1
a = Solution()
print(a.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(a.openLock(["2663","7363","2311","8379","9055","0185","5250","2534","4197","1940","4551","5166","9904","1259","3930","7429","6117","1842","6544","1976","8241","8433","9614","9561","1928","4730","8660","7036","9008","2132","1479","6943","5551","3975","3396","7423","3404","8428","3100","7309","8641","4014","3851","2194","7987","6565","6721","8584","7144","4587","9259","2664","9882","6002","7244","3472","1667","2084","3993","9940","2734","3075","6145","7772","3284","9481","2194","3990","6307","8925","3358","3980","6850","4361","3102","0541","7084","1767","3693","4513","7833","5181","5954","1283","0414","3661","2615","0114","5616","6679","2475","7564","7184","4389","7860","3964","3752","4476","9622","8862","7185","3709","9115","8230","0255","8755","4522","4186","2664","8789","6132","8375","1850","9777","3624","1025","5941","1604","0954","0641","7910","7807","0483","3616","1411","4587","5386","2258","0807","7362","7559","1397","2166","3574","6056","2702","4258","9914","3546","3367","1551","5791","5763","2354","4568","4316","5755","4516","0278","7413","2906","6914","0392","6854","6336","3559","9596","7579","1445","1646","7395","4359","8801","5487","4553","1144","2754","8675","3082","6056","9580","2903","6941","2944","9160","3749","3064","4588","9808","2539","6390","6953","0051","9972","5911","0671","4810","3896","9486","8412","9286","4067","7349","9938","0658","7719","6027","2519","9184","0033","5781","5867","1083","3262","7983","5441","7150","8944","8543","0252","2296","4780","0060","1408","4610","8213","5111","9817","1465","0787","5145","5780","0398","4089","5997","1837","2693","3769","5491","8576","1435","4610","3575","7778","7882","0995","2530","4080","9121","2883","2288","4038","4696","3088","9969","0319","3695","9068","2996","3706","4514","1997","9416","8519","7593","6144","9204","7276","7454","1911","7241","6848","3437","2575","0182","1035","9870","3126","1444","7577","7107","6910","1786","3762","6602","4867","8127","7572","3987","2933","1822","7119","2904","2312","8021","4550","5577","9951","8320","1090","3133","9068","5969","0148","4633","2948","3739","2202","8040","1023","0743","0785","7750","1560","5829","4422","8909","0425","5764","1665","8510","7969","1355","2054","7243","9763","6613","9556","3754","5298","7151","4893","0650","3156","8354","5402","5330","2933","7797","5211","9946","6790","6243","6905","1043","5964","9680","9755","4808","4042","5408","5167","0102","3095","3845","2437","4943","6936","5030","5733","0928","4513","7545","2749","8234","5167","6357","6007","4828","2466","8060","9782","6031","0396","5459","6029","8861","8122","2535","2950","4952","2103","9757","9438","0120","6905","4829","2355","3907","8874","1844","9059","3222","9640","9944","9949","3588","6333","8251","0870","5978","7930","5092","3374","0878","0812","2045","0371","3388","1263","0707","8966","5442","7232","6605","0994","3081","7716","1164","8876","1361","8576","2624","1209","5535","6751","9688","0944","7083","9524","9135","6330","7792","1964","7744","0367","1488","4668","7170","6968","0798","6768","0303","1811","5270","3137","0502","2239","3746","8902","1447","6048","3822","6007","8217","0430","1387","3421","9992","0204","1422","4696","1302","3162","5705","3889","5290","7864","3786","9341","3398","6967","3572","6372","6602","1678","4576","1164","2920","6201","7129","7526","6517","4989","2443","1106","5277","7082","3656","5817","8557","0457","2939","2257","3986","7223","2786","0423","7834","0571","0189","1861","2937","8069","6279","5643","2147","1970","7323","4413"],"1064"))