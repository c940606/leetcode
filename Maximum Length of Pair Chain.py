class Solution(object):
	def findLongestChain(self, pairs):
		"""
		:type pairs: List[List[int]]
		:rtype: int
		"""
		if not pairs:
			return 0
		pairs.sort()
		n = len(pairs)
		dp = [1] * n
		for i in range(n):
			for j in range(i):
				if pairs[j][1] < pairs[i][0]:
					dp[i] = max(dp[i], dp[j] + 1, dp[j])
		return dp[-1]


	def findLongestChain1(self, pairs):
		pairs.sort(key=lambda x: x[1])
		cur = float("-inf")
		res = 0
		for pair in pairs:
			if cur < pair[0]:
				res += 1
				cur = pair[1]
		return res




a = Solution()
print(a.findLongestChain1([[1, 2], [2, 3], [3, 4]]))
print(a.findLongestChain1([[3, 4], [2, 3], [1, 2]]))
print(a.findLongestChain1([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]))
print(a.findLongestChain1(
	[[-836, 821], [922, 943], [-384, 91], [391, 455], [665, 979], [371, 978], [-704, 148], [902, 940], [300, 422],
	 [327, 830], [436, 883], [-369, 189], [215, 503], [185, 707], [46, 835], [-842, -266], [517, 712], [271, 479],
	 [508, 630], [561, 712], [835, 981], [149, 669], [-539, 543], [589, 708], [-800, -774], [-304, -114], [-498, 498],
	 [-389, 484], [-305, 126], [848, 962], [-441, 724], [636, 844], [-771, 17], [-809, -295], [65, 585], [183, 714],
	 [-159, 346], [-182, 867], [-421, 832], [428, 958], [-618, 89], [-337, 439], [-748, 880], [550, 999], [688, 797],
	 [-643, -76], [-305, 257], [-121, 792], [-49, 433], [705, 893], [-655, -395], [-379, 630], [763, 984], [-494, 545],
	 [-969, -431], [-284, -121], [868, 989], [-39, 863], [948, 979], [-51, 414], [-929, -624], [72, 83], [544, 941],
	 [363, 884], [-334, 393], [913, 951], [-750, 774], [66, 465], [87, 895], [-619, -576], [-851, 133], [-947, 260],
	 [-68, 67], [-659, 224], [817, 917], [-967, -485], [-304, 899], [321, 673], [363, 757], [630, 818], [794, 920],
	 [582, 757], [47, 507], [237, 619], [780, 859], [-540, 32], [-267, 970], [-174, 497], [-610, 567], [-945, 1000],
	 [-187, 660], [-724, 639], [521, 912], [-64, 21], [-915, 127], [222, 754], [579, 908], [983, 997], [-783, 120],
	 [-909, -755], [908, 990], [483, 984], [-133, 227], [314, 839], [18, 939], [665, 868], [-279, -122], [-506, 946],
	 [-195, 278], [-313, 191], [-260, -75], [24, 600], [-799, -759], [639, 833], [-126, 638], [309, 624], [170, 978],
	 [946, 983], [-650, 594], [433, 555], [713, 900], [665, 844], [801, 920], [-901, 102], [977, 981], [477, 891],
	 [402, 450], [-79, 963], [-115, 889], [-954, 870], [117, 540], [-846, 662], [422, 590], [674, 821], [-89, 394],
	 [-62, 262], [214, 279], [815, 920], [825, 897], [-269, 897], [-512, 681], [236, 911], [-973, 802], [995, 996],
	 [745, 790], [-56, 412], [-691, 445], [-945, 1000], [25, 536], [234, 909], [272, 806], [-145, -76], [829, 858],
	 [582, 923], [-398, 933], [921, 944], [-820, 202], [-66, 271], [787, 958], [398, 885], [666, 728], [527, 640],
	 [454, 518], [-835, 461], [941, 972], [-181, 450], [-491, 818], [969, 987], [530, 631], [317, 728], [576, 738],
	 [-286, 782], [946, 984], [-48, -12], [-72, 830], [715, 831], [499, 511], [4, 490], [502, 866], [423, 758],
	 [168, 867], [715, 840], [-798, -573], [-699, -470], [766, 797], [358, 937], [599, 728], [-289, -66], [-545, -46],
	 [-689, 285], [216, 376], [-704, 728], [926, 946], [385, 738], [558, 942], [663, 796], [538, 934], [96, 619],
	 [-264, 66], [-767, 90], [-209, 954], [-988, -930], [-436, 952], [-368, 895], [577, 760], [-111, 603], [933, 990],
	 [-865, 15], [502, 521], [760, 934], [-599, 638], [489, 546], [138, 888], [-508, 328], [-171, 442], [433, 626],
	 [-532, 828], [-317, 957], [-402, 607], [-685, -573], [146, 473], [660, 718], [767, 872], [-922, 244], [-876, 429],
	 [-814, -156], [8, 277], [-495, -406], [229, 368], [-170, 971], [433, 508], [527, 879], [867, 884], [5, 431],
	 [917, 950], [268, 460], [295, 534], [505, 679], [-392, 376], [-743, 302], [-713, 660], [-821, 276], [834, 980],
	 [-300, -119], [202, 358], [-190, 717], [-860, 698], [-389, 345], [-989, -718], [-296, 130], [-773, -643],
	 [-151, 776], [570, 951], [976, 982], [-871, 424], [-876, -784], [-471, 472], [659, 956], [616, 661], [349, 716],
	 [152, 627], [-503, 860], [337, 817], [-376, 383], [792, 945], [355, 803], [-24, -13], [14, 674], [-688, -375],
	 [-298, 913], [-523, 0], [-140, 742], [769, 971], [-987, 98], [-920, -196], [22, 455], [-895, 157], [-935, -912],
	 [-507, 552], [415, 435], [-959, -122], [-905, 757], [-489, -321], [-363, 390], [725, 996], [89, 100], [-115, 280],
	 [651, 932], [982, 1000], [150, 542], [-121, 446], [78, 722], [985, 998], [-685, -147], [158, 340], [764, 872],
	 [845, 870], [-590, -466], [-527, 566], [-11, 146], [-671, 499], [228, 773], [-183, 930], [-511, -273], [164, 640],
	 [-106, 898], [252, 848], [-197, 580], [-241, 813], [128, 501], [-656, 113], [-858, -491], [347, 507], [520, 618],
	 [-202, 913], [-782, -75], [105, 686], [-554, -200], [-157, 641], [198, 504], [653, 693], [173, 942], [-490, -14],
	 [-341, 747], [-18, 848], [-800, -750], [590, 831], [856, 986], [203, 938], [-910, 111], [146, 673], [78, 976],
	 [-47, 173], [13, 501], [-213, 67], [894, 979], [-775, -294], [-102, 910], [-415, 694], [-51, 396], [-964, -487],
	 [-758, 465], [-286, -26], [53, 837], [-263, 981], [431, 755], [-669, 279], [392, 869], [-136, 783], [-322, 297],
	 [874, 999], [888, 950], [510, 970], [-610, -74], [-22, 715], [410, 867], [-378, 370], [-77, 104], [-538, 624],
	 [416, 642], [486, 743], [868, 908], [-565, -307], [-948, -569], [-380, -200], [-433, -222], [-408, 88],
	 [-473, 170], [-823, 785], [-784, 82], [542, 892], [778, 931], [-690, 832], [-654, 225], [190, 903], [820, 881],
	 [629, 823], [-612, 456], [87, 524], [391, 811], [765, 908], [-884, 350], [-229, 953], [-137, 833], [816, 987],
	 [115, 408], [-775, -772], [-108, 632], [-171, 230], [385, 670], [-449, -194], [45, 594], [49, 517], [-173, 104],
	 [-871, 811], [58, 75], [396, 633], [745, 850], [887, 912], [530, 673], [171, 551], [-455, -30], [-999, 6],
	 [634, 885], [-650, -87], [-615, -139], [-816, -147], [-992, 310], [568, 748], [229, 238], [-712, -234],
	 [-707, -434], [-163, 511], [735, 954], [-757, -381], [763, 991], [25, 143], [-173, 58], [-8, 183], [-809, 619],
	 [-961, 148], [-744, -472], [623, 792], [-426, 360], [495, 770], [755, 860], [-332, -208], [951, 975], [838, 875],
	 [419, 933], [-608, 284], [-863, -34], [598, 753], [361, 671], [739, 791], [365, 509], [-618, 509], [632, 792],
	 [716, 969], [282, 807], [-248, 920], [-84, -64], [-194, 221], [187, 893], [614, 924], [797, 997], [177, 712],
	 [-851, 613], [374, 792], [-169, -4], [-393, -202], [819, 942], [341, 378], [307, 721], [-129, 149], [-559, -72],
	 [25, 313], [474, 574], [906, 953], [-283, -5], [696, 759], [862, 979], [-956, 454], [-52, 389], [-569, 31],
	 [-416, 844], [-931, -22], [309, 731], [321, 788], [752, 848], [-635, -146], [732, 865], [-420, 110], [393, 730],
	 [765, 895], [218, 784], [-399, -204], [-865, 797], [-188, 719], [-770, 291], [339, 939], [999, 1000], [941, 996],
	 [-112, 39], [-307, 755], [53, 973], [921, 953], [-377, 599], [804, 881], [519, 694], [-772, 68], [293, 448],
	 [-22, 947], [-796, -305], [104, 719], [-831, 940], [-438, 820], [-463, -16], [-2, 229], [-869, 129], [-843, 340],
	 [547, 673], [-842, 744], [-662, 283], [444, 807], [971, 978], [-85, 178], [-434, -92], [-319, -282], [-84, 580],
	 [399, 957], [463, 584], [-452, 394], [-347, 798], [-347, 37], [610, 715], [955, 956], [-987, 736], [977, 993],
	 [674, 894], [-657, -102], [306, 969], [-349, 916], [-210, 279], [-843, 196], [-521, 335], [-147, 115],
	 [-658, -531], [-490, 242], [-557, 245], [-74, -9], [716, 841], [-281, 66], [72, 662], [-839, -196], [406, 530],
	 [317, 776], [-172, 796], [188, 931], [-887, -330], [-913, -759], [957, 981], [224, 745], [-20, 305], [164, 310],
	 [-550, 551], [982, 985], [119, 196], [468, 777], [-653, 514], [232, 606], [792, 822], [323, 728], [-883, -495],
	 [468, 704], [-479, 449], [803, 960], [338, 535], [-33, 597], [352, 695], [607, 969], [-654, -155], [-128, -44],
	 [701, 809], [445, 887], [-891, -838], [-539, 812], [254, 376], [-824, 317], [-287, 303], [150, 880], [514, 743],
	 [492, 526], [783, 794], [85, 633], [-640, 442], [598, 993], [-257, -191], [721, 854], [-692, 648], [847, 920],
	 [816, 828], [285, 668], [427, 611], [-826, 881], [811, 881], [366, 547], [677, 822], [-920, 538], [-82, 569],
	 [-61, 254], [-292, 934], [42, 639], [988, 991], [-955, 848], [858, 970], [-725, -286], [-465, 324], [-663, -417],
	 [520, 823], [-993, 450], [-860, -580], [787, 976], [926, 990], [-459, -305], [655, 993], [119, 287], [933, 978],
	 [-844, 667], [-783, -372], [-564, -145], [-236, 251], [-901, -224], [143, 369], [883, 900], [-145, 148],
	 [251, 458], [647, 898], [-66, 989], [948, 985], [-738, -159], [-233, 116], [717, 881], [455, 533], [-470, 300],
	 [641, 966], [-110, 819], [-290, 873], [7, 782], [-500, 225], [-979, -718], [-471, -64], [-929, 148], [5, 988],
	 [-659, 208], [-477, 125], [-435, 195], [717, 736], [-745, -443], [157, 608], [-693, 903], [803, 956], [919, 927],
	 [158, 205], [-953, 555], [-694, 501], [-534, 513], [-612, -452], [-123, -24], [-332, 871], [145, 773], [-552, 774],
	 [-71, 877], [421, 893], [630, 739], [-184, 414], [-672, -545], [797, 816], [-927, -287], [-857, 425], [29, 490],
	 [359, 509], [63, 593], [631, 936], [320, 988], [-951, 222], [-413, 341], [-723, -21], [280, 402], [-386, 794],
	 [526, 951], [210, 880], [-565, 555], [367, 585], [-254, 760], [-615, 390], [54, 704], [-964, -587], [376, 452],
	 [370, 486], [8, 960], [541, 934], [-155, 646], [251, 885], [40, 820], [690, 798], [527, 547], [515, 613],
	 [-434, 654], [-1000, 417], [-988, -643], [-406, -103], [615, 979], [976, 990], [-125, -108], [838, 988],
	 [-979, -84], [-234, 899], [879, 890], [-745, -34], [-453, 790], [245, 855], [949, 973], [-536, 681], [-178, 40],
	 [276, 746], [669, 886], [493, 572], [810, 840], [214, 723], [-372, -253], [169, 278], [852, 925], [144, 873],
	 [-119, 164], [-391, -162], [719, 962], [752, 967], [718, 911], [-982, -46], [-126, 356], [716, 737], [-643, 666],
	 [26, 385], [499, 621], [61, 256], [-749, 544], [-211, 285], [-414, 305], [-953, 569], [-749, 62], [121, 459],
	 [-84, 857], [384, 412], [727, 875], [991, 1000], [-256, 123], [-710, -633], [-203, 45], [-241, 548], [-851, 5],
	 [450, 621], [-889, -669], [-111, 910], [61, 802], [-834, -276], [495, 519], [-799, -317], [867, 940], [-597, 378],
	 [862, 968], [-584, -200], [392, 937], [733, 996], [-711, 925], [-848, 72], [833, 965], [-83, 466], [481, 923],
	 [-896, 975], [897, 916], [-260, -47], [-981, 699], [670, 820], [-806, 84], [476, 881], [-974, -831], [-963, 645],
	 [-43, 464], [-153, 760], [-109, 130], [-128, 315], [-325, -197], [53, 90], [576, 997], [-542, 753], [200, 835],
	 [247, 417], [-12, 336], [-332, -295], [-247, 617], [721, 884], [68, 283], [938, 957], [-506, 20], [-413, 225],
	 [522, 646], [873, 982], [214, 629], [-877, -240], [-337, 153], [-948, -325], [109, 190], [602, 652], [738, 900],
	 [943, 971], [860, 979], [-254, -201], [-208, -30], [-431, -137], [-92, 394], [-876, -321], [154, 178], [66, 156],
	 [-462, -124], [617, 861], [188, 587], [-821, 135], [-821, 375], [-326, 482], [-310, 641], [340, 895], [735, 936],
	 [437, 508], [-526, 265], [15, 570], [-651, 210], [774, 846], [-457, 389], [-238, 487], [597, 744], [-315, 292],
	 [-435, -254], [-344, 6], [186, 546], [396, 558], [-120, 802], [-861, -567], [-568, -105], [375, 813], [471, 484],
	 [-224, -82], [-897, -329], [-540, -394], [-335, 540], [-959, 471], [-640, 644], [507, 836], [879, 995], [783, 910],
	 [-242, 659], [471, 813], [888, 910], [-779, 43], [251, 490], [317, 909], [964, 997], [843, 848], [-608, -244],
	 [-598, 609], [-686, -644], [-930, 761], [508, 944], [447, 605], [983, 984], [-964, 951], [586, 598], [541, 624],
	 [-541, -117], [-452, 361], [899, 959], [-611, -4], [599, 987], [318, 988], [-904, -488]]))
