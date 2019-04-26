class Solution:
    def longestRepeatingSubstring(self, S) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        n = len(S)
        k = n
        while k > 0:
            for i in range(0, n - k + 1):
                tmp = S[i:i + k]
                if lookup[tmp] == 1:
                    return k
                else:
                    lookup[tmp] = 1
            k -= 1
        return 0


a = Solution()
# print(a.longestRepeatingSubstring("abcd"))
# print(a.longestRepeatingSubstring("abbaba"))
# print(a.longestRepeatingSubstring("aabcaabdaab"))
print(a.longestRepeatingSubstring("aaaaa"))
print(a.longestRepeatingSubstring(
    "bbwfowdeauwderbddpwzrfowybhpvfoyvfdrsgjiytfxxawkctyfvrywxqwwoculuoiqzmsbaonhtswpmachjaademrwznqbkrravioseyibmqeuuayrnxzyptpuwlblkpvhgkufnjhprgsecqzpgfdjdgagjgiifjiftyiimgegotdylcxhdakzwgicnbzefvmdbhbbgbvxbdueewyzrpvxfcbigaprdudvbxreavzgwpcxldwcfnqrbbfvcmeiyafbhtixegibfnugfytiqczwqclfsksameergvxljtxeranlnozzhpdexkfwysuzeavvzqoxogxsixiczwrwrefqnefkumlzdzknqwizvqzyginiakjxllvpttdrhorinzhkxirfkryymvqezvdifjbndxdlflzsbigypltvuyocbudqidyxfknoslylcwwvidlrfjntfkgmzpvkkzscspslrnypbgziknzawqpfvmarzjwdwbezcudhmedfcmdwutehzeayufgmkbnuxaozypkakonotapbzeambrileusrfzhijejuggvtakwsnxuzubdojfgkzwrvsetjvmwqobtagebxgicsgrtgzmrzjnzitxknocptmayabfwrupscpwmclknwqlhkyejhyfxuiunasfbiuttrfotckztxozawqgqwswvwfdnozbmocmdmlyupaoayxnzwrvapputncymzpefiozqimezggqvwlhtpdaseputojdrjxfueemvzdjhhwhfvsauvhpkhldwvwuvonpginysnltfgqawamilcpxdreyjwnmlxcbdurpeasxnabftirkappyrbwsuccrkrzsvlwrwyivctvdmrmdrrxipbqusmicdbqasklcadkianuctcxkewctdrdllodyrpskipsybwrldbsvpjuxmgdbxwhuweizihgiulzrsjsdesdodhmqzwtayfpdtbhnjyjvsilfspghnwytnhoqpcaaawsvxvuotfjkqismsjvevloccfzyubzbucdorgasyhnmemaetpgjruhrbvzdqdjycgybrfxlviqjosqamighivronqyguaunuoxyxnlvysuitxeibyhndoarjbcxxvovleuygweqbsmqtsgvvnwcyooikmeqjjeypfcomywiuyxuwcvlpnypqmaqeuckjgkmhofvbjqubrybeovxtyvgxoodyfjkiicqxfrwhqhnrgfuxtcxyswwluiwpmfdoqsuijjauophmzyyydleuaipsnfpswjfgmaqdigiuzyxtbsgxabbrxlcprzamzwzljbyqnnfhfitnmmruidqcuudwtqstloatznninzmezliprpkzxgoahevghjpwbodqmgcywwanykmijimsdbohmhrgxvkuevuqrlxhgzasmcycwzijwxklmiyfcvyycmfrilqowhsqpqcyexjuhpmcveyipnljcbroiuzizwdclcsbqxzeg"))
