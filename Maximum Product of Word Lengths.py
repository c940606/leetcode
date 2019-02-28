class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        if n == 0: return 0
        max_num = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not (set(words[i]) & set(words[j])):
                    max_num = max(max_num, len(words[i]) * len(words[j]))
        return max_num

    def maxProduct1(self, words):
        if not words:
            return 0
        n = len(words)
        flag = [0] * n
        for idx, word in enumerate(words):
            for alp in word:
                flag[idx] |= 1 << ord(alp) - 97
        # print(flag)
        max_num = 0
        for i in range(n):
            for j in range(i + 1, n):
                if flag[i] & flag[j] == 0:
                    max_num = max(max_num, len(words[i]) * len(words[j]))
        return max_num

    def maxProduct2(self, words):
        from collections import defaultdict
        lookup = defaultdict(int)
        for word in words:
            flag = 0
            for alp in word:
                flag |= 1 << ord(alp) - 97
            lookup[flag] = max(lookup[flag], len(word))
        return max([lookup[x] * lookup[y] for x in lookup for y in lookup if x & y == 0] or [0])


a = Solution()
print(a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(a.maxProduct(["a", "aa", "aaa", "aaaa"]))
print(a.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(a.maxProduct2(
    ["ecbdiogjomkpnkplkk", "jidiekhgdmdccfbegfacjphcniecdckpgop", "lgjihbjojpacehcljpfjhcccionkfdb", "epghehiiffig",
     "mbaoooafmlidimgjgpcpohlchddc", "hgohbogfbodpianbfpgojldldkchgomdjpml", "pbemfnbkdlhp", "iipjlcmodcieac",
     "nodkaebdhnned", "chbkkjflgchpinmhgaolhec", "fdnmflpmdjne", "lmhmddljeal",
     "eccnojmgojbfeljggmpaeepcpboeiokfbaplkgd", "kfgjdbickiblfnebiimedamickepclg", "hailabmidnnamledlpipofmadlm", "dm",
     "oif", "jlcmdfmgfdcdocgk", "eibbmneckkfebmimpiekklainafnjgkjgp", "dimkicpfcjejcp", "ib",
     "jbjfhikhfeolcbojediomkgeikbmmhehlebnklebgjjgocm", "ioeiijkp", "opeilpblcjcfbfigahmekbacjgnbfebnpc",
     "jijebminedcogdpgiipocngikflbahioighaginepcbpjibeh", "ingbmobcpdiogep",
     "ndcfjgbpoahlfkikafinhkmmohemjmbeminnpjahlf", "pgp", "hpmnhfjoffmahjjekgmccpddencm", "heckoampi",
     "cihnigfehmoegckjo", "lfjgadfdgfoee", "ckfmgbhecpikhnpoafnchinmablpkkpjlfahlnjlkhjpf", "pdcojjcmcccgnnpnnjpjacaj",
     "amfmpmfmghmoopcmiocheojhfhmfoglekmjpe", "magdmalmgobanhpnfpndbecegmiiof", "lidicekdafiokffcjbdhgifmngejjcmipb",
     "fidmfm", "hlmnhbjoagdfeokfnfki", "glogigobijmkdpaneg", "ihjopo", "ahaijnjiihad", "gibnn", "ghnfgjpiel",
     "moooagpobnfffiinbfhndjnjoinddniolmdkhbhmggdpgedlloj", "ekiojapmhkdpponmpehj", "jiogddbodgpjgincpcoc",
     "cjpmhkbknjfigjnkbnggfhieahobhkecojd", "oilkcpakbnllhipckocgmaghfdenpchcbgioecpdiokhlgigim", "amkaphkjfoajbkgfg",
     "oklffbmnndfofmcokpbjbblnmenfifdngehj", "nfgnkaeocdfmdlbpmhbke", "eoidofplgjemnbjjiekipbcfjkbhdjbeoeoofbnnmo",
     "ijcooajeibnieoljfp", "hoegckpnckbofkdmelcbfdlignaaapadn", "fdepdkecbifohaolecemojocehhmld",
     "bbdknelmlihahnegiokebinaldnahmakockf", "afclfbfmfinlbgn", "ejpbhdoacnmggfm", "deljnejiackahlciboggpgfeahn", "pc",
     "eokbbkojcebngfidbonnogbfipoajnkcgifdblfjnmkjhcob", "ehjpelnm", "ngikelohpldahcc", "lpehmpnchdaheimnokmebpa",
     "bgncagjeemcbckcflohcbidknlgdkkcnhlnnj", "kegn", "hkkkcijkiahapilonla",
     "hpahglhpbfffnhgdohchanfgnacbhalgdcaibhbgbmcmbbo", "kfboibcfcgnphpgnhaplnkcepoccgoadeigpdebcjagnhb", "bai", "blci",
     "kaklcbjimbchmdoihmjamkifogaemjndgfb", "picclcpggmbgpbphkpjceojccmepfdfegigiheladbhfoehbo",
     "idaemhmdnibdgdihhnickgpkc", "aphnhfpgdjggpcedbfaggekbhlhnagchlajkpjnfoiidba", "nbjgofjpcmieppgbomgnahlmbbnaipdhe",
     "jnpmgfffaidheecgfl", "gaagcgcipdgkklmnljogageimabfnl", "cdniacgpjk", "cnjmedkp", "galfmammpjadjnaolhmdpcickj",
     "ecbefngalcmahfoggbpihgcccaihmfnlgpcidmiciklkg", "hhcgaakljbggibmielll", "jlgibjmeeplbblmnnil",
     "lkfbenmgkcgkjbojgjmnn", "jepememofjeedmnlhphinopmekgdbkaoci", "hidpfpfadgljjgkagepidlbj", "ajedkdmoikhnad",
     "ajbidhheimfiiknipodljfgggnjpennjmlaapcbbe", "ggknebjmhpikfpe", "bhajpgooamgialhklaaniednhki",
     "ajocokfnhpbghgmcmjadanhkjhhidkjcahmfdgbjhi", "njkegfagfdjjoeimghkpohglahfmmamomanlddjalbnenfh",
     "eaminioepipaldkadmcidbbhdoaamleojkkjfadnji", "pcdofohkkmpmiakfndaagbjacbichocgcalfndcfblhngbiei",
     "bbmpobnjdbidkmbihopndfigfombmligmnffcobmjfjbgdbhgd", "foebhanoplaffhihjkiopcapfomgdgjededi", "keb",
     "dijjmcmpajdcebjincdijhgnojejomnbomconcb", "fjicjdglmbnbfmc", "bciebodikkihhidllpfgjcffkacigbipb", "ffbbidjo",
     "omgmcd", "kic", "illalcfohkahgiggdpijcfhfidhpenpoagpglmkalbdiliakckh", "opafjmgfjojffdikgebnhfgngpkaffkcpoapdll",
     "lmdhacnpncflalmdhjlodfniennkennhbcjkjbjookeajoik", "hfhpgaajkoib", "acnlabngalcohnllcalchahmbnkmppmpddemnigoleap",
     "biliibi", "kjhjbibmbcfdhbfdehagnclljjnoa", "blkkiodmmflgeegappjdmmdfenpka", "pjmgbnfikfopjhdhboenambhdhmfifl",
     "nffbmfleieanj", "fpggfabkgbkmlgkaokodkhdbjmojhgipeejajpecncp", "pg",
     "dlabfgoeaajolgdpeflfkmfefoilfpegbfhbbgacbphpnhihi", "dnmceloljh", "lemohgmgplaegpmgiiomgohpndgc", "hmbgcpkldlad",
     "hmcenopbccaohpjilcjkfopfenbpoohbkhaledj"]))
