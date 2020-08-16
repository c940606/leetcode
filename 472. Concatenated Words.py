from typing import List


class Solution:
    def findAllConcatenatedWordsInADict1(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            if not word: continue
            cur = trie
            for w in word:
                cur = cur.setdefault(w, {})
            cur["#"] = "#"  # 结束标志
        res = []

        def dfs(word, idx, cnt, cur):
            if idx == len(word):
                # 组成个数 > 2, 并且以#结束的
                if cnt >= 1 and "#" in cur:
                    return True
                return False
            if "#" in cur:
                if dfs(word, idx, cnt + 1, trie):
                    return True
            if word[idx] not in cur:
                return False
            if dfs(word, idx + 1, cnt, cur[word[idx]]):
                return True
            return False

        for word in words:
            # 参数分别为, 单词word, 位置idx, 目前为止有几个单词组成了cnt, 字典树trie
            if dfs(word, 0, 0, trie):
                res.append(word)
        return res

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words.sort(key=len)
        min_len = max(1, len(words[0]))
        prev = set()
        res = []

        # def check(word, prev):
        #     if not prev: return False
        #     n = len(word)
        #     dp = [False] * (n + 1)
        #     dp[0] = True
        #     for i in range(1, n + 1):
        #         for j in range(i):
        #             if not dp[j]: continue
        #             if word[j:i] in prev:
        #                 dp[i] = True
        #                 break
        #     return dp[-1]

        # def check(word):
        #     if not prev: return False
        #     if not word: return True
        #     for i in range(1, len(word) + 1):
        #         if word[:i] in prev and check(word[i:]):
        #             return True
        #     return False
        def check(word):
            print(word)
            # if not prev: return False
            if  word in prev: return True
            for i in range(min_len, len(word) - min_len + 1):
                if word[:i] in prev and check(word[i:]):
                    return True
            return False



        for word in words:
            if check(word):
                res.append(word)
            prev.add(word)
        return res


a = Solution()
# print(a.findAllConcatenatedWordsInADict(
#     ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
# print(a.findAllConcatenatedWordsInADict([""]))
print(a.findAllConcatenatedWordsInADict(
    ["cat", "dog", "catdog"]))
# print(a.findAllConcatenatedWordsInADict(["a", "b", "ab", "abc"]))
b = ["rfkqyuqfjkx", "", "vnrtysfrzrmzl", "gfve", "qfpd", "lqdqrrcrwdnxeuo", "q", "klaitgdphcspij", "hbsfyfv",
     "adzpbfudkklrw", "aozmixr", "ife", "feclhbvfuk", "yeqfqojwtw", "sileeztxwjl", "ngbqqmbxqcqp", "khhqr",
     "dwfcayssyoqc", "omwufbdfxu", "zhift", "kczvhsybloet", "crfhpxprbsshsjxd", "ilebxwbcto", "yaxzfbjbkrxi",
     "imqpzwmshlpj", "ta", "hbuxhwadlpto", "eziwkmg", "ovqzgdixrpddzp", "c", "wnqwqecyjyib", "jy", "mjfqwltvzk",
     "tpvo", "phckcyufdqml", "lim", "lfz", "tgygdt", "nhcvpf", "fbrpzlk", "shwywshtdgmb", "bkkxcvg",
     "monmwvytby", "nuqhmfj", "qtg", "cwkuzyamnerp", "fmwevhwlezo", "ye", "hbrcewjxvcezi", "tiq", "tfsrptug",
     "iznorvonzjfea", "gama", "apwlmbzit", "s", "hzkosvn", "nberblt", "kggdgpljfisylt", "mf", "h",
     "bljvkypcflsaqe", "cijcyrgmqirz", "iaxakholawoydvch", "e", "gttxwpuk", "jf", "xbrtspfttota", "sngqvoijxuv",
     "bztvaal", "zxbshnrvbykjql", "zz", "mlvyoshiktodnsjj", "qplci", "lzqrxl", "qxru", "ygjtyzleizme", "inx",
     "lwhhjwsl", "endjvxjyghrveu", "phknqtsdtwxcktmw", "wsdthzmlmbhjkm", "u", "pbqurqfxgqlojmws",
     "mowsjvpvhznbsi", "hdkbdxqg", "ge", "pzchrgef", "ukmcowoe", "nwhpiid", "xdnnl", "n", "yjyssbsoc",
     "cdzcuunkrf", "uvouaghhcyvmlk", "aajpfpyljt", "jpyntsefxi", "wjute", "y", "pbcnmhf", "qmmidmvkn",
     "xmywegmtuno", "vuzygv", "uxtrdsdfzfssmel", "odjgdgzfmrazvnd", "a", "rdkugsbdpawxi", "ivd",
     "bbqeonycaegxfj", "lrfkraoheucsvpi", "eqrswgkaaaohxx", "hqjtkqaqh", "berbpmglbjipnuj", "wogwczlkyrde",
     "aqufowbig", "snjniegvdvotu", "ocedkt", "bbufnxorixibbd", "rzuqsyr", "qghoy", "evcuanuujszitaoa", "wsx",
     "glafbwzdd", "znrvjqeyqi", "npitruijvyllsi", "objltu", "ryp", "nvybsfrxtlfmp", "id", "zoolzslgd",
     "owijatklvjzscizr", "upmsoxftumyxifyu", "xucubv", "fctkqlroq", "zjv", "wzi", "ppvs", "mflvioemycnphfjt",
     "nwedtubynsb", "repgcx", "gsfomhvpmy", "kdohe", "tyycsibbeaxn", "wjkfvabn", "llkmagl", "thkglauzgkeuly",
     "paeurdvexqlw", "akdt", "ihmfrj", "janxk", "rqdll", "cyhbsuxnlftmjc", "yybwsjmajbwtuhkk", "ovytgaufpjl",
     "iwbnzhybsx", "mumbh", "jqmdabmyu", "br", "lwstjkoxbczkj", "vhsgzvwiixxaob", "fso", "qnebmfl", "ooetjiz",
     "lq", "msxphqdgz", "mqhoggvrvjqrp", "xbhkkfg", "zxjegsyovdrmw", "jav", "mshoj", "ax", "biztkfomz",
     "hujdmcyxdqteqja", "gqgsomonv", "reqqzzpw", "lihdnvud", "lznfhbaokxvce", "fhxbldylqqewdnj", "rlbskqgfvn",
     "lfvobeyolyy", "v", "iwh", "fpbuiujlolnjl", "gvwxljbo", "ypaotdzjxxrsc", "mwrvel", "umzpnoiei",
     "ogwilaswn", "yw", "egdgye", "hsrznlzrf", "mwdgxaigmxpy", "yaqgault", "dtlg", "cyvfiykmkllf",
     "zxqyhvizqmamj", "lvvgoifltzywueyp", "abinmy", "ppzaecvmx", "qsmzc", "iddymnl", "uskihek", "evxtehxtbthq",
     "jvtfzddlgch", "czohpyewf", "ufzazyxtqxcu", "brxpfymuvfvs", "xrrcfuusicc", "aqhlswbzievij", "rv",
     "udvmara", "upityz", "fecd", "suxteeitxtg", "dfuydrtbfypbn", "cypqodxr", "wikfuxwjht", "jrliuaifpp",
     "vkmxys", "wvpfyfpkvgthq", "rmajxis", "jncxgviyu", "av", "nmhskodmidaj", "lkfrimprrhen", "uip",
     "hstyopbvuiqc", "p", "vwduwmjpblqo", "fnxwgqtvwztje", "xwnbcuggl", "iehimvoymyjasin", "spsqiu", "flhyfac",
     "mqrbq", "pstsxhplrrmbeddv", "hnegtuxx", "alsyxezjwtlwmxv", "jtxytykkcku", "bhhlovgcx", "xhhivxnutkx",
     "had", "aysulvk", "m", "anhsyxli", "jdkgfc", "potn", "lcibpxkidmwexp", "gwoxjicdkv", "tltienw",
     "ngiutnuqbzi", "o", "tzlyb", "vumnwehj", "os", "np", "lhv", "uzvgyeette", "ipfvr", "lpprjjalchhhcmh", "k",
     "pciulccqssaqgd", "tp", "dmzdzveslyjad", "wtsbhgkd", "eouxbldsxzm", "vhtonlampljgzyve", "xhnlcrldtfthul",
     "xhflc", "upgei", "rlaks", "yfqvnvtnqspyjbxr", "phouoyhvls", "voibuvbhhjcdflvl", "rgorfbjrofokggaf",
     "dqhqats", "zchpicyuawpovm", "yzwfor", "koat", "pybf", "fhdzsbiyjld", "gznfnqydisn", "xz", "po", "tcjup",
     "wygsnxk", "kqlima", "fgxnuohrnhg", "publurhztntgmimc", "zuufzphd", "iucrmmmjqtcey", "wnnbq", "rghzyz",
     "ukjqsjbmp", "mdtrgv", "vyeikgjdnml", "kxwldnmi", "apzuhsbssaxj", "tkbkoljyodlipof", "nkq", "ktwtj",
     "vgmkgjwle", "t", "agylw", "vomtuy", "jbtvitkqn", "vtdxwrclpspcn", "rdrls", "yxfeoh", "upj", "myctacn",
     "fdnor", "ahqghzhoqprgkym", "phiuvdv", "jp", "fdgpouzjwbq", "hqoyefmugjvewhxu", "qfzwuwe",
     "fnsbijkeepyxry", "oja", "qthkcij", "zpmqfbmnr", "ybaibmzonzqlnmd", "svo", "gjftyfehik",
     "jfrfgznuaytvaegm", "aljhrx", "odjq", "ogwaxrssjxgvnka", "zaqswwofedxj", "lugpktauixp", "dc", "odknlbvxrs",
     "jeobu", "vqythyvzxbcgrlbg", "hwc", "erpbaxq", "ujxcxck", "rrklkb", "wlrwyuy", "zmg", "yyhga", "xwdbycdu",
     "htedgvsrhchox", "wr", "suhesetv", "jonqwhkwezjvjgg", "sqqyrxtjkcalswq", "hvyimhe", "pjzdkmoue",
     "zbphmgoxq", "lbdlcumdgixjbcq", "ztzdjqmadthtdmv", "qcagsyqggcf", "if", "jpjxcjyi", "chyicqibxdgkqtg",
     "iwpdklhum", "wljmg", "micmun", "npdbamofynykqv", "ijsnfkpfy", "lmq", "oyjmeqvhcrvgm", "mqopusqktdthpvz",
     "fz", "r", "qbsqtipq", "nxtsnason", "xbpipyhh", "topsuqomfjrd", "islif", "gbndakaq", "bwnkxnwpzeoohlx",
     "hrtbfnq", "fguvomeepxoffg", "mat", "dzfpfnwbfuj", "onlvy", "cwcchvsasdylb", "rxfcztzqopdi", "ybrhodjn",
     "oqkijy", "ncvrjo", "dphbfaal", "xgtpdtkz", "sebevsopjvciwljf", "rcumyacqdapwczen", "mabkapuoud",
     "pbozezeygljfftvy", "bvazmzbndl", "vl", "qiaixdtbhqvlzd", "ffjfb", "svthrfmkoxbho", "cvet",
     "ucgqyvopafyttrh", "lbgihet", "naiqyufxffdw", "vruh", "uz", "ukffmudygjavem", "dccamymhp", "wofwgjkykm",
     "fbuujzxhln", "kmm", "lzandlltowjpwsal", "fapfvrmezbsjxs", "wiw", "sc", "soqlh", "hzaplclkwl",
     "gcdqbcdwbwa", "gadgt", "pgowefka", "juffuguqepwnfh", "nbuinl", "cpdxf", "sox", "fq", "lfnrhgsxkhx",
     "xrcorfygjxpi", "mwtqjwbhgh", "loc", "fkglorkkvx", "nlzdhucvayrz", "azefobxutitrf", "rlrstkcbtikklmh",
     "ggk", "sbphcejuylh", "nraoenhd", "zngyodiqlchxyycx", "rrbhfwohfv", "krzolrglgn", "cpjesdzy", "yoifoyg",
     "hqqevqjugi", "ahmv", "xgaujnyclcjq", "evhyfnlohavrj", "byyvhgh", "hyw", "kedhvwy", "ysljsqminajfipds",
     "rglnpxfqwu", "cibpynkxg", "su", "mbntqrlwyampdg", "nig", "ldhlhqdyjcfhu", "jfymrbafmyoc", "tyjmnhlfnrtz",
     "dlazixtlxyvm", "fbiguhsfuqo", "rhymsno", "rkbdlchs", "ocbbwwd", "astaiamnepwkya", "mplirup", "edkxjq",
     "g", "exlwulswtvot", "tlnc", "vnrrzerz", "ygeraoozbtt", "yyifkin", "eo", "ua", "qgztvqdolf",
     "rlzddjzcshvd", "khxkdxflwxme", "kk", "zylbhoaac", "cw", "iizic", "gcdxstpz", "kjwdqeg", "earjrncmmkdel",
     "kbesuhquepj", "nrzbllldgdmyrpgl", "hllwnqozf", "djpchowhwevbqvjj", "zsmhylnjpktb", "pxnktxkm", "fxwiaqqb",
     "qjwufmwresfsfaok", "aa", "d", "iobioqm", "svjgzk", "khbzp", "euexyudhrioi", "yqsj", "ngrwqpoh", "rwuvd",
     "eruffmlg", "bxzovyew", "faz", "pmvfvyguqdi", "jlxnoixsy", "hyfrdngjf", "ly", "eibcapetpmeaid", "tpnwwiif",
     "pfgsp", "kvhhwkzvtvlhhb", "pjxurgqbtldims", "rncplkeweoirje", "akyprzzphew", "wyvfpjyglzrmhfqp",
     "ubheeqt", "rmbxlcmn", "taqakgim", "apsbu", "khwnykughmwrlk", "vtdlzwpbhcsbvjno", "tffmjggrmyil",
     "schgwrrzt", "mvndmua", "nlwpw", "glvbtkegzjs", "piwllpgnlpcnezqs", "xkelind", "urtxsezrwz", "zechoc",
     "vfaimxrqnyiq", "ybugjsblhzfravzn", "btgcpqwovwp", "zgxgodlhmix", "sfzdknoxzassc", "wgzvqkxuqrsqxs",
     "dwneyqisozq", "fg", "vhfsf", "uspujvqhydw", "eadosqafyxbmzgr", "tyff", "blolplosqnfcwx", "uwkl",
     "puenodlvotb", "iizudxqjvfnky", "cjcywjkfvukvveq", "jrxd", "igwb", "dftdyelydzyummmt", "uvfmaicednym",
     "oai", "higfkfavgeemcgo", "naefganqo", "iqebfibigljbc", "ulicojzjfrc", "igxprunj", "cymbrl",
     "fqmwciqtynca", "zjyagi", "mzuejrttefhdwqc", "zyiurxvf", "wrjxffzbjexsh", "wrxw", "mhrbdxjwi", "htknfa",
     "wfrvxqdkhbwwef", "vqsghhhutdget", "cwupzrts", "hbjnb", "wpccoa", "nx", "howbzhaoscgyk", "bilt", "wqqatye",
     "zceuuwg", "jxzon", "kkfj", "bwsezd", "ifdegsyjtswselk", "xweimxlnzoh", "tqthlftjblnpht", "ww", "ss", "b",
     "jmruuqscwjp", "nxbk", "wd", "cqkrtbxgzg", "xhppcjnq", "cfq", "tkkolzcfi", "wblxki", "ijeglxsvc",
     "kcqjjwcwuhvzydm", "gubqavlqffhrzz", "hiwxrgftittd", "caybc", "ncsyjlzlxyyklc", "poxcgnexmaajzuha",
     "dhaccuualacyl", "mtkewbprs", "oncggqvr", "sqqoffmwkplsgbrp", "ioajuppvqluhbdet", "dzwwzaelmo",
     "afumtqugec", "wglucmugwqi", "zveswrjevfz", "nxlbkak", "pzcejvxzeoybb", "fd", "vewj", "ivws",
     "zjhudtpqsfc", "zcmukotirrxx", "zksmx", "umofzhhowyftz", "zbotrokaxaryxlk", "ueolqk", "dxmzhoq", "zvu",
     "cjl", "esfmqgvxwfy", "npbep", "vbgjtbv", "poeugoqynkbfiv", "fewjjscjrei", "yqssxzsydgllfzmo",
     "urxkwcypctjkabi", "wqtldwhjouas", "tovdtkr", "onzgeyddkqwuhnim", "ffxviyvsktqrfa", "qujhd", "pvcz",
     "hiyjlkxmeplnrvxg", "hdykehkefp", "vepcxhozpjxtreyn", "liguhuxudbnh", "f", "ordxzm", "klgohcmmbukz",
     "yrmooliaobbnlap", "dutnbetocxylcey", "ywdsjegd", "cr", "blbxhjsgcuoxmqft", "ngzdc", "srfyjjumcbxole",
     "dazwzwtdjoyuqeqj", "xazjarqgfm", "fxyfqbeoktcc", "qrsjchxp", "iltaqzawhgu", "sgenjcfxr", "yfikp",
     "dvwhbyumthkiktb", "walsx", "jyajrkcvysicisab", "brdeumb", "tviihjwxdcz", "dnrrgmem", "ydgxlrjzucxyid",
     "cdvdpvjlagwmg", "ngnpxjkxims", "gvyhnchlimsxc", "w", "jtizpezjl", "qe", "rjzv", "vhnqvi", "qm",
     "iedzqswrsnfmnn", "lt", "utqfcqyrrwm", "wtelvsqrru", "fjwrhjcrtbcytn", "qmqxceuohpiffaq", "rmoybqjjgdyo",
     "pmxttqftypfexlv", "tg", "qa", "iqbqjlnpbf", "kgaynkddbzllecd", "tccvslp", "curkxfoimnw", "fvnyqkzlheruxr",
     "iiygnzfov", "coqs", "oa", "eiu", "vzemmxtklis", "lxu", "nrwsjaxzwmh", "tdayz", "oxbbemejgosgcynf",
     "ykbcn", "hesvnctfvdsp", "ku", "rjhykpadahbhj", "at", "sxlngbtxmqr", "wqrom", "qzyabzrco", "rbbyklndcqdj",
     "cnsmgmwmpbgjq", "krvnaf", "qrwfajnfahyqocdb", "fnlaozmff", "vmoymbmytjvfcgt", "cijyy", "jdgwjbztl",
     "swmalgbgpaplqgz", "hfl", "typttkrpfvx", "tkzpzrscwbx", "bwfqqvjcukjbsg", "nxqmxr", "x", "eyavnz", "il",
     "dhthp", "eyelg", "npsoqsw", "reogbmveofvusdsx", "jvdrjkhxkq", "qzjbrpljwuzpl", "czqeevvbvcwh",
     "vzuszqvhlmapty", "yu", "yldwwgezlqur", "vorxwgdtgjilgydq", "pknt", "bgihl", "ckorgrm", "ixylxjmlfv",
     "bpoaboylced", "zea", "igfagitkrext", "ipvqq", "dmoerc", "oqxbypihdv", "dtjrrkxro", "rexuhucxpi",
     "bvmuyarjwqpcoywa", "qwdmfpwvamisns", "bhopoqdsref", "tmnm", "cre", "ktrniqwoofoeenbz", "vlrfcsftapyujmw",
     "updqikocrdyex", "bcxw", "eaum", "oklsqebuzeziisw", "fzgyhvnwjcns", "dybjywyaodsyw", "lmu", "eocfru",
     "ztlbggsuzctoc", "ilfzpszgrgj", "imqypqo", "fump", "sjvmsbrcfwretbie", "oxpmplpcg", "wmqigymr", "qevdyd",
     "gmuyytguexnyc", "hwialkbjgzc", "lmg", "gijjy", "lplrsxznfkoklxlv", "xrbasbznvxas", "twn", "bhqultkyfq",
     "saeq", "xbuw", "zd", "kng", "uoay", "kfykd", "armuwp", "gtghfxf", "gpucqwbihemixqmy", "jedyedimaa",
     "pbdrx", "toxmxzimgfao", "zlteob", "adoshnx", "ufgmypupei", "rqyex", "ljhqsaneicvaerqx", "ng", "sid",
     "zagpiuiia", "re", "oadojxmvgqgdodw", "jszyeruwnupqgmy", "jxigaskpj", "zpsbhgokwtfcisj", "vep",
     "ebwrcpafxzhb", "gjykhz", "mfomgxjphcscuxj", "iwbdvusywqlsc", "opvrnx", "mkgiwfvqfkotpdz", "inpobubzbvstk",
     "vubuucilxyh", "bci", "dibmye", "rlcnvnuuqfvhw", "oorbyyiigppuft", "swpksfdxicemjbf", "goabwrqdoudf",
     "yjutkeqakoarru", "wuznnlyd", "vfelxvtggkkk", "mxlwbkbklbwfsvr", "advraqovan", "smkln", "jxxvzdjlpyurxpj",
     "ssebtpznwoytjefo", "dynaiukctgrzjx", "irzosjuncvh", "hcnhhrajahitn", "vwtifcoqepqyzwya", "kddxywvgqxo",
     "syxngevs", "batvzmziq", "mjewiyo", "pzsupxoflq", "byzhtvvpj", "cqnlvlzr", "akvmxzbaei", "mwo", "vg",
     "ekfkuajjogbxhjii", "isdbplotyak", "jvkmxhtmyznha", "lqjnqzrwrmgt", "mbbhfli", "bpeohsufree", "ajrcsfogh",
     "lucidbnlysamvy", "tutjdfnvhahxy", "urbrmmadea", "hghv", "acnjx", "athltizloasimp", "gu",
     "rjfozvgmdakdhao", "iephs", "uztnpqhdl", "rfuyp", "crcszmgplszwfn", "zihegt", "xbspa", "cjbmsamjyqqrasz",
     "ghzlgnfoas", "ljxl", "cnumquohlcgt", "jm", "mfccj", "hfedli", "vtpieworwhyiucs", "tdtuquartspkotm",
     "pnkeluekvelj", "ugrloq", "zljmwt", "fkyvqguqq", "tpjidglpxqfxv", "l", "tvvimvroz", "yy", "opwyfovdz",
     "pwlumocnyuoume", "vjqpzkcfc", "ihicd", "dtttiixlhpikbv", "goblttgvmndkqgg", "gwsibcqahmyyeagk", "prtvoju",
     "lcblwidhjpu", "kbu", "pey", "gkzrpc", "bqajopjjlfthe", "bc", "lqs", "zkndgojnjnxqsoqi", "zyesldujjlp",
     "drswybwlfyzph", "xzluwbtmoxokk", "bedrqfui", "opajzeahv", "lehdfnr", "mnlpimduzgmwszc", "velbhj", "miwdn",
     "wruqc", "kscfodjxg", "wcbm"]
# print(a.findAllConcatenatedWordsInADict(b))
