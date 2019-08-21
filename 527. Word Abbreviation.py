class Solution:
    def wordsAbbreviation(self, dict):
        from collections import defaultdict
        lookup = defaultdict(list)
        # print(sorted(dict))
        res = [None] * len(dict)

        def abbreviate(word, k):
            n = len(word)
            if n <= 3: return word
            tmp_word = word[:k] + str(n - k - 1) + word[-1]
            if len(tmp_word) < n:
                return tmp_word
            return word

        pre = 1
        for idx, word in enumerate(dict):
            # print(idx,word)
            lookup[abbreviate(word, 1)].append([word, idx])
        pre += 1
        #print(lookup)
        while lookup:
            # print(lookup)
            next_lookup = defaultdict(list)
            for key, item in lookup.items():
                if len(item) == 1:
                    res[item[0][1]] = key
                else:
                    # print(item)
                    for w, idx in item:
                        abb = abbreviate(w, pre)
                        # print(abb)
                        next_lookup[abb].append([w, idx])

            pre += 1
            lookup = next_lookup

        return res

        # lookup = next_lookup


a = Solution()
# print(a.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
print(a.wordsAbbreviation(["abcdefg", "abccefg", "abcckkg"]))
# print(a.wordsAbbreviation(["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intrusion"]))
# print(a.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
print(a.wordsAbbreviation(["bbbbab", "bbbaab", "baaaab"]))
print(a.wordsAbbreviation(
    ["bbadabadccdabdadccdd", "aacbbbacccacaadabcdc", "ccdcccdcbccadadbdcdd", "abdbcaacbaacabccadaa",
     "cbaaabddbbddcbbcbddb", "addaadcdaabcccbddada", "aaaabcbbcadabdaccdda", "dbcabacdacdaaccdccdc",
     "acdabbcdcabaaccdbbac", "abbadcabdabcadcdccbc", "ddbddbadacacacbcbaaa", "dabaaababccaddbaacad",
     "dbbdbcdcabbaacdccbdc", "dcdcbbcccadbacdaddad", "dacdbcdbaddabbbabbac", "bdddacdcabbcccdbcdaa",
     "abaababcccadabadbcdd", "bbbccdbadcbaacadcacb", "abddadccaaccccaacccd", "dbbababacaacdbdbcdcb",
     "cdadccadbdaaacbabbbc", "adaaabbcabddadcacabb", "bdbbbaadaddbbbddbabd", "ddaccbdccadcaccabcbd",
     "dbdacbbbacdbbddddbbd", "bbaaadcccdbacdccdddd", "cbdbbcddaacabcabbabd", "bbacccdbdbddbabbbaba",
     "cacabbaaaaaaabadbddc", "daddaaccbadcacaadabc", "adcdbddadabbdabcabdb", "aabdacbdbacdddcbbbdc",
     "bbcdbdbdcbacbccbbdaa", "daadacbcbcbcddcdcbcc", "daccabbdbddcddacbdcb", "cbccacacabbcdbbcabac",
     "bbdbcbbdbacabddbcbcb", "acbbbcdbbdcddbccbbba", "cbdabcdaccdbcddbbbcb", "dabdbbcdcccdbdacbcca",
     "cdccbdddbbdcadbcbcbd", "cacccbccdcacdcbddcbd", "bbcddabcdbcadcbcdaac", "adddbcbdaacbabcddbcc",
     "ccbbbbcaabccadbcdacd", "cbbbbdaadaccdadccbad", "caabaddbbacccaddcdcd", "bbbcdbcddadabddcccbd",
     "ccdadbcacdadbdbbacdb", "cbcaddcadadcbcdabbdc", "dcadcdbaabcacdddaaba", "ccaadddcabdcbbdacdad",
     "dacdadcbbbdddaabacaa", "addbaddaabbddacbdbaa", "adcabccccbaccdccadaa", "cbaabdabdddcaaaabdac",
     "dbcababcaaddbdacbdcc", "bdaaaadcdbcacccccdac", "baccadcdaabcbcdbabba", "badccccddaabacdbcdac",
     "dabcabbdadcdcadbcddb", "abcdcbbaccdddadcaaba", "aaaccabacbdbcadbabcb", "ddbccbbbaccdabaacacb",
     "bdacababadbadadbccbc", "aacacadccabbcadbabac", "bcbcddadaddbdbddddad", "bcabddacadbaadcaddaa",
     "ccdcbdcadacddaaacbab", "ddcbdbabaddcacdadcaa", "bcabddcdbbdabdbccbac", "cbddcbccbcadacdaccbb",
     "ddbcaddcdabccbbdcccd", "cbadbbcacdccdddabadd", "cdcbdcbddddcbccbadad", "dcdacdbaacddbaaccaba",
     "cccbddbbaddbcababcdb", "dcbdbaddaabcdadcaaad", "ddccbadacbdbcbccadcd", "dcaccbddaccdabccbccb",
     "bdcbddcbddcbbbbdabca", "dcbddbbbacaacdacdbbc", "abdbabbddbdacccbdbdd", "cbaddbabdcbbbaadcdbb",
     "dbacdbdcdcacaccbbabb", "acdaccdababbbcdddbbd", "badcccdabacadbdaabad", "cdabbadbaccbadcbaacd",
     "bdcaddbdccdcadaaabba", "bccaaddbaabcbcacdcab", "abaabacbcdcdbcadaacb", "abbccddcbadaaaaadcdd",
     "badbccdddbbbdcbdbddd", "bcdbddcdcccbaabccbbd", "bacabcdbcbabacdddddc", "cbaabcbacdbcbdabcacb",
     "ddbdadacadcaccbdbcdd", "ccabbbbbdbcacbaacbbc", "bccabcacdccccbdabcad", "babbadcaddadabdbdcbc",
     "ddcaacdcccbdbdadcaac", "aacccddcbaddbacbaccc", "adabadbcbdbcdaacbbdd", "bbacaddcbaccbcbadcdb",
     "badddadbddbbdbcaacda", "aaccddddbddddaacbcaa", "aabbcbdadcdcabcccadc", "dacbdaabdccccbdddacd",
     "dccbdddccdaacadbaabc", "abacddbabdacacadbadc", "abcbbddddbbdccacbabb", "aacaacdaadcadaaccbcc",
     "addbacdbcdabcadccdac", "cbababbdccdbdbdacadb", "babdbcbacdbadbadccaa", "aaabcddbcdbacbdaabbd",
     "dabcadaaabdbcaaacbbb", "dcdcdacbcccbcabccdca", "abbddccccdaaaabaccad", "bcabbdacbcaaccdddddd",
     "dacddcabcaddacbbbcaa", "aabcbbbddabdbaabddbc", "abcbdddbccbaaaaadcdb", "cbabbdacdadaddbccaca",
     "bcddbbdcdddbadbdbabc", "bbdbdadbbbaccbadbdda", "cccbbdbcadbbdccbdaaa", "bbcbababbcdbadbaacda",
     "adcdcddbcccbbbaaacdc", "bbbdccdccdcdaacbdacb", "bcbbacbccdadabddaada", "dadadadaacaaccccbdac",
     "abbbcddaaadbbcbcbdcd", "dababccbbdadbadcaaad", "bbcdccbdbdbbddcbacba", "ccdaaababbbbdcaaabda",
     "daaadaabaacaabdabbbd", "abbbbbbcdbcddbacddcb", "adddbdbbcbdbbcdaccca", "ccbddabbdcdcaabbbdbb",
     "dcddabddbaacbbbcbaca", "bccaccadcabbaabaadaa", "baadcbdcabcbbbcddccd", "cbddcdcbddbccbaacabc",
     "ddacabdbacbbabccadbd", "daaddcadaccdbbdcdccd", "abdaabcdbabbdbbcdcba", "ccdbbcaabbdadbbdccdb",
     "cadcddbbccadcdbdabcb", "dcdcddbaabbddcbdaddb", "cbcdbadcdcdaddcbcddd", "ddadaadcbddadbbadccd",
     "acdacaadcddbadbcdbdd", "bbaadccddabcdadddbbb", "caabadcbcdacdcbacbbd", "badcbddccbdcdccbbbcd",
     "aabcbddbdbcbacdaaada", "abccdcbbacbbbacddcbd", "cccbbbdabcbadcabaaab", "acccbcbcbbbbaaddaccb",
     "abdddbdaadcbcdcbbccc", "abcdadacdcabdacddbdd", "cdddcadadbddbcbbcdba", "abdbadcacbcdaaabbacd",
     "ccdaddabbacbbbcccaba", "dddaacbddcbbbddacdbc", "ddbbbdcdbddaaabcdaab", "dbdabddacaadccaabbac",
     "badddacadbdbacbddbcb", "cdadcddaaacdaaaabdab", "bccbadaccdbbdabddbab", "ddaadabbddacacbdbcdb",
     "addcbdbdbddbdaadcdaa", "bbcabccadcdcbcdadcdd", "bbaccccdbdacbcddacac", "dbbaadabacabbbdcaddb",
     "bcdbbaacbccaacdbaaaa", "aaabcdadbaacbabdacbc", "dbccbdacdbcbacdadaba", "bdadcdcdbbcdcabdbbcc",
     "cdbbbdaabddbccabdaac", "baacabdccdcdccbcbdcc", "bcbbbaaaddabdcddddcd", "dcddacdddacccddacbdb",
     "dcacdcbddccbbcaacbda", "cbadbbbacabcddddcacc", "dabbbdddbcddbccbabda", "bbcacaaddbbabddbbdaa",
     "cbaddabdabbcddadbaab", "bbadcbbdbabddbabbcca", "adbdcdddbabdaacdacab", "bdaccaaddbaddbaabdcc",
     "cbdcbacacdbbcbbccbbd", "cdcabcccddbbcddccbdc", "bddddcabbaabcbdbbabd", "cdbcbabacacbcbcdbcbc",
     "aadbacacbaadbbbcbdba", "caadbbaddcddccbbabdb", "aacbddbbbadddacdbdaa", "bcadabdaadcacbcccbaa"]))
