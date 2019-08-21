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
            # print(tmp_str)
            if len(tmp_str) < maxWidth:
                tmp_str += " " * (maxWidth - len(tmp_str))
            else:
                tmp_str = tmp_str[:maxWidth]
            res.append(tmp_str)
            # print(i)
            # break

        return res

    def fullJustify1(self, words, maxWidth):
        res = []
        n = len(words)
        i = 0

        def one_row_words(i):
            # 至少 一行能放下一个单词, cur_row_len
            left = i
            cur_row_len = len(words[i])
            i += 1
            while i < n:
                # 当目前行 加上一个单词长度 再加一个空格
                if cur_row_len + len(words[i]) + 1 > maxWidth:
                    break
                cur_row_len += len(words[i]) + 1
                i += 1
            return left, i

        while i < n:
            left, i = one_row_words(i)
            # 该行几个单词获取
            one_row = words[left:i]
            # 如果是最后一行了
            if i == n :
                res.append(" ".join(one_row).ljust(maxWidth," "))
                break
            # 所有单词的长度
            all_word_len = sum(len(i) for i in one_row)
            # 至少空格个数
            space_num = i - left - 1
            # 可以为空格的位置
            remain_space = maxWidth - all_word_len
            # 单词之间至少几个空格,还剩几个空格没用
            if space_num:
                a, b = divmod(remain_space, space_num)
            # print(a,b)
            # 该行字符串拼接
            tmp = ""
            for word in one_row:
                if tmp:
                    tmp += " " * a
                    if b:
                        tmp += " "
                        b -= 1
                tmp += word
            print(tmp, len(tmp))
            res.append(tmp.ljust(maxWidth, " "))
        return res


a = Solution()
print(a.fullJustify1(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(a.fullJustify1(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(a.fullJustify1(
    words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
           "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
