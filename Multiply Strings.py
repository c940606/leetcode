class Solution(object):
    def multiply(self, num1, num2):
        """
        给定两个以字符串形式表示的非负整数 num1 和 num2，
        返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
        ---
        输入: num1 = "2", num2 = "3"
        输出: "6"
        ---
        输入: num1 = "123", num2 = "456"
        输出: "56088"
        ---
        思路:
        用乘法公式
        1. 相乘的位数最大是6位
        2. 先用一个数组 表示个个数相乘记录
        3. 超过10，向前进位
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        lookup = {"0": 0,
                  "1": 1,
                  "2": 2,
                  "3": 3,
                  "4": 4,
                  "5": 5,
                  "6": 6,
                  "7": 7,
                  "8": 8,
                  "9": 9
                  }
        n1 = len(num1)
        n2 = len(num2)
        # print(n1+n2)
        temp = [0] * (n1 + n2)
        # print(temp)
        f = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in num1:
            k = 0
            for j in num2:
                temp[f + k] += lookup[i] * lookup[j]
                k += 1
            f += 1
        # print(temp)
        # res = [0]*(n1+n2)
        i = 0
        while True:
            q, r = divmod(temp[i], 10)
            if i < n1 + n2 - 1:
                temp[i] = r
                temp[i + 1] += q
                i += 1
            else:
                temp[i] = r
                break
        temp = temp[::-1]
        return "".join(map(str, temp)).lstrip("0")

    def multiply1(self, num1, num2):
        if num1 == "0" or num2 == "0": return "0"
        i = len(num1) - 1

        def one_str_mul(a, b):
            return str(int(a) * int(b))

        def add_str(a, b):
            i = len(a) - 1
            j = len(b) - 1
            carry_digit = 0
            tmp_res = ""
            while i >= 0 or j >= 0 or carry_digit:
                tmp_a = 0
                tmp_b = 0
                if i >= 0:
                    tmp_a = int(a[i])
                if j >= 0:
                    tmp_b = int(b[j])
                all_a_b = tmp_a + tmp_b + carry_digit
                tmp_res += str(all_a_b % 10)
                carry_digit = all_a_b // 10
                i -= 1
                j -= 1
            return tmp_res[::-1]

        all_add = []
        num_zeros = 0
        while i >= 0:
            tmp = one_str_mul(num1[i], num2)
            tmp += "0" * num_zeros
            all_add.append(tmp)
            num_zeros += 1
            i -= 1
        ans = ""
        for t in all_add:
            ans = add_str(ans, t)
        return ans


a = Solution()
print(a.multiply1("123", "456"))
