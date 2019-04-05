class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        # visited = set()
        graph = defaultdict(list)
        lookup = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # print(graph)
        def helper(i, visited, depth):
            for j in graph[i]:
                if j not in visited:
                    helper(j, visited | {j}, depth + 1)
                    lookup[j] = max(lookup[j], depth)
            lookup[i] = max(lookup[i], depth)

        leaves = [i for i in graph if len(graph[i]) == 1]
        for i in leaves:
            helper(i, {i}, 1)

        # print(lookup)
        min_num = min(lookup.values())
        return [i for i in lookup if lookup[i] == min_num]

    def findMinHeightTrees1(self, n, edges):
        from collections import defaultdict
        if not edges:
            return [0]
        graph = defaultdict(list)
        if not edges: return [0]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        leaves = {i for i in graph if len(graph[i]) == 1}
        while n > 2:
            n -= len(leaves)
            nxt = set()
            for leave in leaves:
                tmp = graph[leave].pop()
                graph[tmp].remove(leave)
                if len(graph[tmp]) == 1:
                    nxt.add(tmp)
            leaves = nxt
        return list(leaves)


a = Solution()
print(a.findMinHeightTrees1(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
print(a.findMinHeightTrees(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print(a.findMinHeightTrees(1717,
                           [[0, 1], [1, 2], [2, 3], [0, 4], [1, 5], [0, 6], [5, 7], [1, 8], [3, 9], [6, 10], [4, 11],
                            [2, 12], [7, 13], [7, 14], [14, 15], [15, 16], [5, 17], [11, 18], [16, 19], [2, 20],
                            [4, 21], [2, 22], [8, 23], [19, 24], [24, 25], [11, 26], [11, 27], [1, 28], [22, 29],
                            [13, 30], [6, 31], [12, 32], [17, 33], [7, 34], [18, 35], [16, 36], [13, 37], [11, 38],
                            [38, 39], [0, 40], [6, 41], [20, 42], [38, 43], [23, 44], [29, 45], [21, 46], [12, 47],
                            [20, 48], [39, 49], [7, 50], [34, 51], [48, 52], [8, 53], [20, 54], [52, 55], [26, 56],
                            [20, 57], [18, 58], [1, 59], [21, 60], [19, 61], [48, 62], [26, 63], [32, 64], [60, 65],
                            [65, 66], [40, 67], [61, 68], [47, 69], [39, 70], [3, 71], [60, 72], [23, 73], [32, 74],
                            [27, 75], [26, 76], [17, 77], [37, 78], [21, 79], [43, 80], [59, 81], [7, 82], [17, 83],
                            [49, 84], [40, 85], [24, 86], [61, 87], [12, 88], [79, 89], [59, 90], [29, 91], [52, 92],
                            [83, 93], [7, 94], [3, 95], [79, 96], [96, 97], [51, 98], [52, 99], [78, 100], [52, 101],
                            [51, 102], [43, 103], [84, 104], [18, 105], [1, 106], [65, 107], [46, 108], [6, 109],
                            [28, 110], [66, 111], [15, 112], [92, 113], [88, 114], [36, 115], [44, 116], [63, 117],
                            [65, 118], [94, 119], [117, 120], [65, 121], [75, 122], [85, 123], [98, 124], [32, 125],
                            [13, 126], [19, 127], [64, 128], [97, 129], [43, 130], [22, 131], [12, 132], [131, 133],
                            [39, 134], [58, 135], [70, 136], [42, 137], [35, 138], [90, 139], [36, 140], [43, 141],
                            [92, 142], [99, 143], [86, 144], [77, 145], [5, 146], [37, 147], [22, 148], [132, 149],
                            [105, 150], [20, 151], [144, 152], [48, 153], [76, 154], [149, 155], [36, 156], [99, 157],
                            [101, 158], [21, 159], [125, 160], [11, 161], [5, 162], [15, 163], [34, 164], [80, 165],
                            [46, 166], [129, 167], [44, 168], [40, 169], [101, 170], [12, 171], [135, 172], [136, 173],
                            [48, 174], [96, 175], [50, 176], [35, 177], [144, 178], [170, 179], [49, 180], [15, 181],
                            [98, 182], [50, 183], [162, 184], [20, 185], [37, 186], [0, 187], [69, 188], [108, 189],
                            [130, 190], [153, 191], [101, 192], [191, 193], [113, 194], [29, 195], [40, 196],
                            [152, 197], [61, 198], [114, 199], [107, 200], [10, 201], [162, 202], [25, 203], [31, 204],
                            [75, 205], [93, 206], [152, 207], [184, 208], [15, 209], [185, 210], [122, 211], [71, 212],
                            [205, 213], [207, 214], [153, 215], [111, 216], [93, 217], [18, 218], [110, 219],
                            [209, 220], [193, 221], [43, 222], [176, 223], [106, 224], [126, 225], [109, 226],
                            [171, 227], [143, 228], [189, 229], [219, 230], [207, 231], [39, 232], [219, 233],
                            [70, 234], [22, 235], [16, 236], [3, 237], [180, 238], [168, 239], [155, 240], [229, 241],
                            [146, 242], [57, 243], [56, 244], [132, 245], [5, 246], [57, 247], [35, 248], [10, 249],
                            [63, 250], [10, 251], [0, 252], [145, 253], [179, 254], [57, 255], [204, 256], [82, 257],
                            [115, 258], [81, 259], [174, 260], [210, 261], [257, 262], [183, 263], [220, 264],
                            [128, 265], [73, 266], [226, 267], [30, 268], [45, 269], [10, 270], [6, 271], [241, 272],
                            [180, 273], [57, 274], [200, 275], [202, 276], [144, 277], [221, 278], [24, 279], [2, 280],
                            [19, 281], [268, 282], [229, 283], [207, 284], [98, 285], [156, 286], [92, 287], [278, 288],
                            [125, 289], [161, 290], [211, 291], [225, 292], [250, 293], [192, 294], [150, 295],
                            [5, 296], [47, 297], [97, 298], [46, 299], [298, 300], [67, 301], [128, 302], [125, 303],
                            [12, 304], [81, 305], [185, 306], [267, 307], [159, 308], [277, 309], [261, 310],
                            [210, 311], [71, 312], [59, 313], [269, 314], [108, 315], [281, 316], [265, 317],
                            [213, 318], [259, 319], [261, 320], [317, 321], [311, 322], [292, 323], [64, 324],
                            [84, 325], [253, 326], [275, 327], [8, 328], [269, 329], [82, 330], [225, 331], [27, 332],
                            [80, 333], [325, 334], [258, 335], [97, 336], [149, 337], [273, 338], [292, 339],
                            [286, 340], [339, 341], [84, 342], [145, 343], [191, 344], [343, 345], [330, 346],
                            [160, 347], [34, 348], [186, 349], [48, 350], [139, 351], [1, 352], [247, 353], [235, 354],
                            [210, 355], [264, 356], [28, 357], [323, 358], [326, 359], [135, 360], [259, 361],
                            [182, 362], [62, 363], [154, 364], [67, 365], [62, 366], [199, 367], [36, 368], [302, 369],
                            [7, 370], [29, 371], [287, 372], [359, 373], [176, 374], [136, 375], [158, 376], [118, 377],
                            [101, 378], [38, 379], [87, 380], [113, 381], [180, 382], [56, 383], [236, 384], [281, 385],
                            [150, 386], [213, 387], [116, 388], [222, 389], [173, 390], [96, 391], [238, 392],
                            [113, 393], [315, 394], [320, 395], [305, 396], [326, 397], [314, 398], [12, 399],
                            [233, 400], [208, 401], [136, 402], [328, 403], [103, 404], [204, 405], [88, 406],
                            [264, 407], [80, 408], [352, 409], [64, 410], [241, 411], [287, 412], [319, 413],
                            [269, 414], [108, 415], [395, 416], [321, 417], [273, 418], [110, 419], [216, 420],
                            [350, 421], [192, 422], [416, 423], [203, 424], [121, 425], [347, 426], [33, 427],
                            [254, 428], [412, 429], [320, 430], [89, 431], [227, 432], [380, 433], [271, 434],
                            [213, 435], [409, 436], [436, 437], [292, 438], [232, 439], [72, 440], [171, 441],
                            [291, 442], [165, 443], [322, 444], [0, 445], [100, 446], [175, 447], [98, 448], [141, 449],
                            [330, 450], [318, 451], [17, 452], [105, 453], [205, 454], [405, 455], [424, 456],
                            [217, 457], [404, 458], [325, 459], [361, 460], [147, 461], [301, 462], [460, 463],
                            [199, 464], [88, 465], [464, 466], [131, 467], [341, 468], [198, 469], [413, 470],
                            [398, 471], [204, 472], [320, 473], [76, 474], [11, 475], [340, 476], [390, 477],
                            [240, 478], [327, 479], [308, 480], [307, 481], [330, 482], [80, 483], [178, 484],
                            [247, 485], [115, 486], [148, 487], [11, 488], [397, 489], [84, 490], [65, 491], [376, 492],
                            [130, 493], [235, 494], [38, 495], [281, 496], [464, 497], [360, 498], [208, 499],
                            [408, 500], [203, 501], [432, 502], [305, 503], [86, 504], [199, 505], [205, 506],
                            [354, 507], [278, 508], [450, 509], [64, 510], [219, 511], [338, 512], [162, 513],
                            [455, 514], [16, 515], [271, 516], [272, 517], [19, 518], [88, 519], [6, 520], [506, 521],
                            [325, 522], [48, 523], [249, 524], [248, 525], [69, 526], [336, 527], [285, 528],
                            [312, 529], [185, 530], [246, 531], [472, 532], [406, 533], [152, 534], [420, 535],
                            [347, 536], [324, 537], [450, 538], [74, 539], [447, 540], [535, 541], [145, 542],
                            [19, 543], [285, 544], [120, 545], [190, 546], [502, 547], [456, 548], [134, 549],
                            [443, 550], [120, 551], [493, 552], [243, 553], [22, 554], [501, 555], [395, 556],
                            [191, 557], [361, 558], [333, 559], [503, 560], [28, 561], [496, 562], [8, 563], [203, 564],
                            [338, 565], [202, 566], [427, 567], [294, 568], [374, 569], [148, 570], [409, 571],
                            [495, 572], [217, 573], [204, 574], [157, 575], [251, 576], [446, 577], [557, 578],
                            [100, 579], [138, 580], [440, 581], [278, 582], [172, 583], [174, 584], [442, 585],
                            [199, 586], [521, 587], [371, 588], [126, 589], [304, 590], [466, 591], [426, 592],
                            [427, 593], [123, 594], [366, 595], [301, 596], [131, 597], [175, 598], [446, 599],
                            [269, 600], [143, 601], [167, 602], [1, 603], [22, 604], [544, 605], [432, 606], [1, 607],
                            [229, 608], [88, 609], [507, 610], [73, 611], [528, 612], [298, 613], [320, 614],
                            [546, 615], [491, 616], [356, 617], [557, 618], [479, 619], [267, 620], [321, 621],
                            [572, 622], [554, 623], [187, 624], [133, 625], [403, 626], [494, 627], [428, 628],
                            [40, 629], [230, 630], [35, 631], [138, 632], [471, 633], [436, 634], [345, 635],
                            [185, 636], [352, 637], [108, 638], [603, 639], [350, 640], [458, 641], [18, 642],
                            [529, 643], [434, 644], [206, 645], [181, 646], [443, 647], [385, 648], [551, 649],
                            [150, 650], [47, 651], [461, 652], [301, 653], [254, 654], [603, 655], [462, 656],
                            [515, 657], [52, 658], [323, 659], [422, 660], [640, 661], [20, 662], [462, 663],
                            [298, 664], [73, 665], [400, 666], [438, 667], [283, 668], [546, 669], [295, 670],
                            [44, 671], [619, 672], [591, 673], [576, 674], [390, 675], [125, 676], [491, 677],
                            [416, 678], [229, 679], [572, 680], [348, 681], [459, 682], [314, 683], [132, 684],
                            [188, 685], [554, 686], [272, 687], [407, 688], [307, 689], [182, 690], [663, 691],
                            [650, 692], [639, 693], [294, 694], [469, 695], [104, 696], [203, 697], [105, 698],
                            [649, 699], [249, 700], [597, 701], [56, 702], [19, 703], [400, 704], [180, 705],
                            [691, 706], [611, 707], [336, 708], [363, 709], [157, 710], [67, 711], [48, 712],
                            [323, 713], [480, 714], [519, 715], [433, 716], [533, 717], [68, 718], [279, 719],
                            [329, 720], [392, 721], [687, 722], [582, 723], [381, 724], [467, 725], [308, 726],
                            [403, 727], [250, 728], [522, 729], [228, 730], [402, 731], [461, 732], [454, 733],
                            [104, 734], [194, 735], [273, 736], [730, 737], [645, 738], [615, 739], [619, 740],
                            [571, 741], [524, 742], [232, 743], [464, 744], [285, 745], [621, 746], [133, 747],
                            [699, 748], [317, 749], [511, 750], [571, 751], [25, 752], [496, 753], [113, 754],
                            [640, 755], [265, 756], [137, 757], [53, 758], [232, 759], [194, 760], [378, 761],
                            [58, 762], [676, 763], [33, 764], [380, 765], [157, 766], [473, 767], [306, 768],
                            [172, 769], [228, 770], [706, 771], [334, 772], [668, 773], [360, 774], [439, 775],
                            [529, 776], [445, 777], [374, 778], [284, 779], [122, 780], [369, 781], [317, 782],
                            [742, 783], [699, 784], [47, 785], [632, 786], [490, 787], [124, 788], [77, 789],
                            [509, 790], [686, 791], [757, 792], [736, 793], [793, 794], [316, 795], [116, 796],
                            [249, 797], [402, 798], [655, 799], [662, 800], [496, 801], [378, 802], [732, 803],
                            [286, 804], [397, 805], [248, 806], [287, 807], [687, 808], [214, 809], [235, 810],
                            [10, 811], [30, 812], [650, 813], [116, 814], [396, 815], [659, 816], [186, 817],
                            [196, 818], [214, 819], [650, 820], [46, 821], [257, 822], [805, 823], [455, 824],
                            [742, 825], [657, 826], [291, 827], [383, 828], [295, 829], [581, 830], [386, 831],
                            [226, 832], [193, 833], [621, 834], [104, 835], [350, 836], [267, 837], [13, 838],
                            [293, 839], [630, 840], [318, 841], [698, 842], [307, 843], [200, 844], [39, 845],
                            [441, 846], [277, 847], [501, 848], [729, 849], [651, 850], [305, 851], [661, 852],
                            [95, 853], [211, 854], [825, 855], [52, 856], [534, 857], [638, 858], [274, 859],
                            [273, 860], [194, 861], [255, 862], [526, 863], [346, 864], [546, 865], [439, 866],
                            [816, 867], [542, 868], [318, 869], [576, 870], [759, 871], [577, 872], [769, 873],
                            [53, 874], [486, 875], [179, 876], [793, 877], [399, 878], [411, 879], [356, 880],
                            [69, 881], [564, 882], [76, 883], [175, 884], [427, 885], [604, 886], [493, 887],
                            [855, 888], [826, 889], [426, 890], [469, 891], [382, 892], [504, 893], [294, 894],
                            [576, 895], [706, 896], [605, 897], [345, 898], [863, 899], [542, 900], [321, 901],
                            [174, 902], [657, 903], [798, 904], [41, 905], [790, 906], [835, 907], [523, 908],
                            [869, 909], [128, 910], [204, 911], [421, 912], [43, 913], [7, 914], [563, 915], [819, 916],
                            [112, 917], [696, 918], [418, 919], [229, 920], [168, 921], [183, 922], [386, 923],
                            [402, 924], [401, 925], [707, 926], [49, 927], [926, 928], [164, 929], [773, 930],
                            [626, 931], [819, 932], [486, 933], [650, 934], [6, 935], [407, 936], [113, 937],
                            [749, 938], [600, 939], [308, 940], [933, 941], [436, 942], [5, 943], [316, 944],
                            [133, 945], [169, 946], [565, 947], [750, 948], [526, 949], [868, 950], [298, 951],
                            [610, 952], [475, 953], [189, 954], [341, 955], [34, 956], [621, 957], [919, 958],
                            [565, 959], [689, 960], [407, 961], [250, 962], [453, 963], [20, 964], [196, 965],
                            [760, 966], [354, 967], [681, 968], [281, 969], [858, 970], [172, 971], [399, 972],
                            [565, 973], [174, 974], [336, 975], [829, 976], [330, 977], [770, 978], [154, 979],
                            [158, 980], [565, 981], [654, 982], [95, 983], [82, 984], [927, 985], [290, 986],
                            [699, 987], [373, 988], [858, 989], [355, 990], [317, 991], [160, 992], [720, 993],
                            [710, 994], [936, 995], [133, 996], [322, 997], [22, 998], [230, 999], [863, 1000],
                            [489, 1001], [701, 1002], [762, 1003], [815, 1004], [266, 1005], [556, 1006], [951, 1007],
                            [507, 1008], [935, 1009], [372, 1010], [411, 1011], [569, 1012], [175, 1013], [21, 1014],
                            [36, 1015], [881, 1016], [594, 1017], [546, 1018], [876, 1019], [643, 1020], [236, 1021],
                            [699, 1022], [720, 1023], [295, 1024], [159, 1025], [458, 1026], [406, 1027], [711, 1028],
                            [373, 1029], [143, 1030], [768, 1031], [623, 1032], [922, 1033], [528, 1034], [191, 1035],
                            [780, 1036], [506, 1037], [618, 1038], [349, 1039], [859, 1040], [445, 1041], [198, 1042],
                            [888, 1043], [487, 1044], [152, 1045], [208, 1046], [186, 1047], [242, 1048], [637, 1049],
                            [490, 1050], [841, 1051], [536, 1052], [71, 1053], [187, 1054], [392, 1055], [161, 1056],
                            [136, 1057], [276, 1058], [336, 1059], [745, 1060], [718, 1061], [903, 1062], [499, 1063],
                            [947, 1064], [688, 1065], [551, 1066], [270, 1067], [435, 1068], [623, 1069], [1031, 1070],
                            [894, 1071], [545, 1072], [834, 1073], [136, 1074], [442, 1075], [370, 1076], [713, 1077],
                            [950, 1078], [1013, 1079], [698, 1080], [1001, 1081], [94, 1082], [133, 1083], [193, 1084],
                            [613, 1085], [278, 1086], [343, 1087], [764, 1088], [98, 1089], [1089, 1090], [649, 1091],
                            [647, 1092], [949, 1093], [416, 1094], [1035, 1095], [816, 1096], [338, 1097], [957, 1098],
                            [853, 1099], [1063, 1100], [542, 1101], [963, 1102], [955, 1103], [353, 1104], [576, 1105],
                            [210, 1106], [1051, 1107], [720, 1108], [337, 1109], [970, 1110], [977, 1111], [981, 1112],
                            [917, 1113], [343, 1114], [344, 1115], [293, 1116], [1031, 1117], [15, 1118], [331, 1119],
                            [290, 1120], [1014, 1121], [502, 1122], [65, 1123], [454, 1124], [32, 1125], [1123, 1126],
                            [181, 1127], [914, 1128], [962, 1129], [34, 1130], [993, 1131], [656, 1132], [749, 1133],
                            [249, 1134], [943, 1135], [671, 1136], [495, 1137], [186, 1138], [2, 1139], [872, 1140],
                            [866, 1141], [461, 1142], [79, 1143], [711, 1144], [519, 1145], [61, 1146], [343, 1147],
                            [576, 1148], [379, 1149], [566, 1150], [97, 1151], [920, 1152], [508, 1153], [351, 1154],
                            [800, 1155], [196, 1156], [611, 1157], [356, 1158], [769, 1159], [1060, 1160], [533, 1161],
                            [609, 1162], [52, 1163], [354, 1164], [1023, 1165], [939, 1166], [1099, 1167], [894, 1168],
                            [134, 1169], [155, 1170], [221, 1171], [467, 1172], [208, 1173], [696, 1174], [964, 1175],
                            [235, 1176], [741, 1177], [479, 1178], [514, 1179], [1127, 1180], [322, 1181], [477, 1182],
                            [803, 1183], [1154, 1184], [582, 1185], [921, 1186], [1001, 1187], [27, 1188], [61, 1189],
                            [280, 1190], [1088, 1191], [716, 1192], [929, 1193], [143, 1194], [875, 1195], [506, 1196],
                            [514, 1197], [325, 1198], [667, 1199], [627, 1200], [146, 1201], [702, 1202], [312, 1203],
                            [703, 1204], [1098, 1205], [1033, 1206], [180, 1207], [1086, 1208], [1043, 1209],
                            [273, 1210], [325, 1211], [609, 1212], [1150, 1213], [191, 1214], [1210, 1215], [195, 1216],
                            [37, 1217], [285, 1218], [1039, 1219], [183, 1220], [203, 1221], [272, 1222], [734, 1223],
                            [660, 1224], [741, 1225], [968, 1226], [657, 1227], [1163, 1228], [139, 1229], [338, 1230],
                            [1227, 1231], [706, 1232], [10, 1233], [169, 1234], [1107, 1235], [106, 1236], [117, 1237],
                            [1130, 1238], [570, 1239], [228, 1240], [60, 1241], [1195, 1242], [1117, 1243], [446, 1244],
                            [22, 1245], [917, 1246], [296, 1247], [641, 1248], [631, 1249], [813, 1250], [705, 1251],
                            [1130, 1252], [1250, 1253], [1207, 1254], [116, 1255], [1225, 1256], [1204, 1257],
                            [667, 1258], [529, 1259], [413, 1260], [78, 1261], [302, 1262], [683, 1263], [1007, 1264],
                            [392, 1265], [542, 1266], [950, 1267], [339, 1268], [820, 1269], [274, 1270], [1241, 1271],
                            [457, 1272], [790, 1273], [603, 1274], [1070, 1275], [26, 1276], [493, 1277], [544, 1278],
                            [874, 1279], [1246, 1280], [842, 1281], [81, 1282], [339, 1283], [1110, 1284], [607, 1285],
                            [590, 1286], [873, 1287], [198, 1288], [1224, 1289], [643, 1290], [561, 1291], [977, 1292],
                            [797, 1293], [761, 1294], [948, 1295], [910, 1296], [876, 1297], [1065, 1298], [1037, 1299],
                            [719, 1300], [432, 1301], [31, 1302], [904, 1303], [977, 1304], [467, 1305], [1224, 1306],
                            [667, 1307], [34, 1308], [833, 1309], [558, 1310], [436, 1311], [1279, 1312], [447, 1313],
                            [554, 1314], [303, 1315], [558, 1316], [1139, 1317], [230, 1318], [824, 1319], [1241, 1320],
                            [736, 1321], [152, 1322], [521, 1323], [482, 1324], [42, 1325], [194, 1326], [114, 1327],
                            [1234, 1328], [1077, 1329], [612, 1330], [573, 1331], [1281, 1332], [693, 1333],
                            [987, 1334], [661, 1335], [1215, 1336], [842, 1337], [186, 1338], [675, 1339], [1049, 1340],
                            [10, 1341], [1268, 1342], [658, 1343], [1223, 1344], [998, 1345], [797, 1346], [3, 1347],
                            [1127, 1348], [1325, 1349], [818, 1350], [647, 1351], [628, 1352], [320, 1353], [246, 1354],
                            [880, 1355], [1100, 1356], [668, 1357], [424, 1358], [656, 1359], [1072, 1360], [979, 1361],
                            [514, 1362], [400, 1363], [637, 1364], [1143, 1365], [77, 1366], [415, 1367], [624, 1368],
                            [180, 1369], [774, 1370], [1213, 1371], [1159, 1372], [576, 1373], [798, 1374], [755, 1375],
                            [1244, 1376], [906, 1377], [94, 1378], [583, 1379], [991, 1380], [1302, 1381], [321, 1382],
                            [776, 1383], [508, 1384], [997, 1385], [1341, 1386], [465, 1387], [967, 1388], [685, 1389],
                            [712, 1390], [508, 1391], [460, 1392], [1236, 1393], [1282, 1394], [769, 1395], [459, 1396],
                            [39, 1397], [483, 1398], [139, 1399], [776, 1400], [288, 1401], [253, 1402], [783, 1403],
                            [261, 1404], [444, 1405], [933, 1406], [184, 1407], [224, 1408], [846, 1409], [1285, 1410],
                            [47, 1411], [1312, 1412], [821, 1413], [888, 1414], [950, 1415], [1149, 1416], [261, 1417],
                            [711, 1418], [438, 1419], [1352, 1420], [299, 1421], [495, 1422], [35, 1423], [1161, 1424],
                            [1347, 1425], [564, 1426], [453, 1427], [972, 1428], [1136, 1429], [1226, 1430],
                            [1081, 1431], [371, 1432], [1347, 1433], [1423, 1434], [964, 1435], [466, 1436],
                            [922, 1437], [407, 1438], [383, 1439], [1208, 1440], [38, 1441], [352, 1442], [766, 1443],
                            [54, 1444], [1185, 1445], [340, 1446], [883, 1447], [330, 1448], [248, 1449], [116, 1450],
                            [605, 1451], [1062, 1452], [7, 1453], [409, 1454], [1217, 1455], [189, 1456], [528, 1457],
                            [947, 1458], [158, 1459], [1199, 1460], [1165, 1461], [537, 1462], [539, 1463], [708, 1464],
                            [1435, 1465], [131, 1466], [1, 1467], [186, 1468], [1219, 1469], [1131, 1470], [1249, 1471],
                            [1352, 1472], [1142, 1473], [648, 1474], [771, 1475], [823, 1476], [264, 1477], [140, 1478],
                            [1231, 1479], [161, 1480], [1336, 1481], [576, 1482], [1315, 1483], [717, 1484],
                            [872, 1485], [694, 1486], [988, 1487], [618, 1488], [321, 1489], [1470, 1490], [1336, 1491],
                            [988, 1492], [1212, 1493], [993, 1494], [1491, 1495], [1385, 1496], [4, 1497], [1327, 1498],
                            [1044, 1499], [649, 1500], [1211, 1501], [1280, 1502], [1251, 1503], [1012, 1504],
                            [361, 1505], [871, 1506], [1089, 1507], [61, 1508], [1312, 1509], [791, 1510], [460, 1511],
                            [1188, 1512], [441, 1513], [32, 1514], [193, 1515], [242, 1516], [316, 1517], [1011, 1518],
                            [107, 1519], [165, 1520], [797, 1521], [1009, 1522], [1085, 1523], [23, 1524], [1152, 1525],
                            [513, 1526], [298, 1527], [172, 1528], [995, 1529], [451, 1530], [739, 1531], [224, 1532],
                            [1421, 1533], [1181, 1534], [1412, 1535], [287, 1536], [1227, 1537], [1018, 1538],
                            [58, 1539], [1235, 1540], [406, 1541], [360, 1542], [1361, 1543], [1384, 1544], [804, 1545],
                            [1435, 1546], [580, 1547], [448, 1548], [728, 1549], [1194, 1550], [102, 1551], [706, 1552],
                            [761, 1553], [1299, 1554], [1263, 1555], [1309, 1556], [1199, 1557], [1086, 1558],
                            [642, 1559], [1449, 1560], [1532, 1561], [231, 1562], [272, 1563], [882, 1564], [832, 1565],
                            [825, 1566], [1205, 1567], [1294, 1568], [759, 1569], [1259, 1570], [762, 1571],
                            [534, 1572], [556, 1573], [1317, 1574], [904, 1575], [1273, 1576], [1269, 1577],
                            [665, 1578], [1566, 1579], [487, 1580], [168, 1581], [1323, 1582], [861, 1583], [500, 1584],
                            [371, 1585], [38, 1586], [373, 1587], [17, 1588], [774, 1589], [1012, 1590], [371, 1591],
                            [1022, 1592], [572, 1593], [659, 1594], [430, 1595], [787, 1596], [151, 1597], [1265, 1598],
                            [1058, 1599], [1221, 1600], [228, 1601], [1531, 1602], [1494, 1603], [348, 1604],
                            [1414, 1605], [1109, 1606], [1114, 1607], [1386, 1608], [655, 1609], [737, 1610],
                            [741, 1611], [1507, 1612], [8, 1613], [743, 1614], [1091, 1615], [817, 1616], [1250, 1617],
                            [1366, 1618], [662, 1619], [1367, 1620], [601, 1621], [801, 1622], [1042, 1623],
                            [789, 1624], [589, 1625], [1440, 1626], [1422, 1627], [1011, 1628], [1132, 1629],
                            [1304, 1630], [178, 1631], [808, 1632], [564, 1633], [1384, 1634], [1191, 1635],
                            [1467, 1636], [1498, 1637], [1248, 1638], [253, 1639], [376, 1640], [390, 1641],
                            [465, 1642], [576, 1643], [677, 1644], [1079, 1645], [1106, 1646], [1541, 1647],
                            [1467, 1648], [36, 1649], [709, 1650], [841, 1651], [100, 1652], [817, 1653], [1017, 1654],
                            [685, 1655], [228, 1656], [1522, 1657], [1492, 1658], [697, 1659], [671, 1660], [533, 1661],
                            [1579, 1662], [572, 1663], [1434, 1664], [531, 1665], [280, 1666], [1533, 1667],
                            [594, 1668], [684, 1669], [1010, 1670], [1490, 1671], [271, 1672], [1500, 1673],
                            [970, 1674], [1085, 1675], [148, 1676], [10, 1677], [897, 1678], [1592, 1679], [871, 1680],
                            [1046, 1681], [1205, 1682], [1526, 1683], [603, 1684], [33, 1685], [80, 1686], [1355, 1687],
                            [597, 1688], [1192, 1689], [418, 1690], [979, 1691], [962, 1692], [1574, 1693], [645, 1694],
                            [613, 1695], [672, 1696], [1551, 1697], [1641, 1698], [1499, 1699], [478, 1700],
                            [1432, 1701], [826, 1702], [175, 1703], [1307, 1704], [1298, 1705], [1688, 1706],
                            [150, 1707], [96, 1708], [49, 1709], [121, 1710], [86, 1711], [360, 1712], [780, 1713],
                            [292, 1714], [867, 1715], [1324, 1716]]))
