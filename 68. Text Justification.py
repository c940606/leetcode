class Solution:
    def fullJustify(self, words, maxWidth):
        '''

        :param words:
        :param maxWidth:
        :return:
        '''
        res = []
        i = 0
        n = len(words)
        while i < n:
            left = i
            all_num = len(words[i])
            word_len = all_num
            i += 1
            while i < n and all_num + 1 + len(words[i]) <= maxWidth:
                all_num += (1 + len(words[i]))
                word_len += len(words[i])
                i += 1
            tmp = words[left:i]
            # print(tmp)
            # print(all_num)
            if i == n:
                tmp_str = " ".join(tmp)
                tmp_str += " " * (maxWidth - len(tmp_str))
                res.append(tmp_str)
                break

            # print(sum(map(len, tmp)))
            remain_space = maxWidth - word_len
            # print("num_word:", i - left - 1)
            if i - left - 1 == 0:
                a = 0
                b = 0
            else:
                a, b = divmod(remain_space, i - left - 1)
            j = 0
            # print(a, b, remain_space)
            tmp_str = ""
            while b:
                tmp_str += tmp[j] + " " * (a + 1)
                j += 1
                b -= 1
            while j < len(tmp):
                tmp_str += tmp[j] + " " * a
                j += 1
            #print(tmp_str)
            if len(tmp_str) < maxWidth:
                tmp_str += " " * (maxWidth - len(tmp_str))
            else:
                tmp_str = tmp_str[:maxWidth]
            res.append(tmp_str)
            #print(i)
            # break

        return res


a = Solution()
print(a.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(a.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(a.fullJustify(
    words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
           "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
