class Solution:
    def findLonelyPixel(self, picture):
        if not picture: return 0
        from collections import defaultdict
        row = len(picture)
        col = len(picture[0])
        res = 0
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        for i in range(row):
            for j in range(col):
                if picture[i][j] == "B":
                    row_dict[i] += 1
                    col_dict[j] += 1

        for i in range(row):
            for j in range(col):
                if picture[i][j] == "B" and row_dict[i] == 1 and col_dict[j] == 1:
                    res += 1
        return res
