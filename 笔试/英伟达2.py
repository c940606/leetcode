# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def __init__(self):
        self.c = None

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        cnt = Counter(self.c)
        for a in c:
            if cnt[a] == 1:
                return a
        return "#"

    def Insert(self, char):
        # write code here
        self.c = char
