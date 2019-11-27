# 数量
# 库存 id quality count
# 个数
# 查询
def totalItem(numOfItems, stockDetails, numOfQueries, queries):
    res = []
    for item in queries:
        if item[0] == 1:
            # id
            _id = item[1]
            quality = item[2]
            cnt = item[3]
            if stockDetails[_id][1] <= quality:
                stockDetails[_id][2] += cnt
        elif item[0] == 2:
            _id = item[1]
            det_cnt = item[2]
            stockDetails[_id][2] -= det_cnt
        else:
            left = item[1]
            right = item[2]
            tmp = 0
            for i in range(left, right):
                tmp += stockDetails[i][2]
            res.append(tmp)
        return res


