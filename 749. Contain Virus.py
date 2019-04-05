class Solution:
    def containVirus(self, grid):
        import heapq
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])
        visited = set()
        visited1 = set()

        def count_num(res):
            cou = 0
            for i, j in res:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                        cou += 1
            return cou

        def helper1(i, j):

            visited.add((i, j))
            res = []

            def helper2(i, j):
                res.append((i, j))
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and grid[tmp_i][
                        tmp_j] == 1:
                        visited.add((tmp_i, tmp_j))
                        helper2(tmp_i, tmp_j)

            helper2(i, j)
            count = count_num(res)
            return -count, res

        def helper2(tmp):
            shuc = []
            for i, j in tmp:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                        visited.add((tmp_i, tmp_j))
                        grid[tmp_i][tmp_j] = 1
                        shuc.append((tmp_i, tmp_j))

            return shuc + tmp

        cur = []
        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == 1:
                    tmp = helper1(i, j)
                    cur.append(tmp)
        print(cur)
        ans = 0
        while cur:
            num, res = heapq.heappop(cur)
            visited1.update(res)
            ans += (-num)
            next_time = []
            # print(num, ans, cur)
            for _, tmp in cur:
                t = helper2(tmp)
                c = count_num(t)
                next_time.append((-c, t))

            cur = next_time
            print(next_time)
        return ans

        # 找到传染最大

    def containVirus1(self, grid):
        row = len(grid)
        col = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 已访问的
        visited = set()
        isolation_zone = set()
        all_virus_area = []

        def find_virus_area(i, j, area):
            area.append((i, j))
            visited.add((i, j))
            for x, y in dirs:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and \
                        (tmp_i, tmp_j) not in visited and (tmp_i, tmp_j) not in isolation_zone and grid[tmp_i][
                    tmp_j] == 1:
                    find_virus_area(tmp_i, tmp_j, area)

        def circu(area):
            cou = 0
            # tmp_visited = set()
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col \
                            and (tmp_i, tmp_j) not in isolation_zone and grid[tmp_i][tmp_j] == 0:
                        # tmp_visited.add((tmp_i, tmp_j))
                        cou += 1
            return cou

        def sprea_area(area):

            cou = 0
            tmp_visited = set()
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col \
                            and (tmp_i, tmp_j) not in tmp_visited and (tmp_i, tmp_j) not in isolation_zone and \
                            grid[tmp_i][tmp_j] == 0:
                        tmp_visited.add((tmp_i, tmp_j))
                        cou += 1
            return cou

        def spread(area):
            res = []
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                        grid[tmp_i][tmp_j] = 1
                        res.append((tmp_i, tmp_j))
            return res

        for i in range(row):
            for j in range(col):
                area = []
                if (i, j) not in visited and grid[i][j] == 1:
                    find_virus_area(i, j, area)
                    all_virus_area.append(area)
        # print(all_virus_area)
        # print(list(map(circu, all_virus_area)))
        res = 0
        while all_virus_area:
            all_area = list(map(sprea_area, all_virus_area))
            all_circu = list(map(circu, all_virus_area))
            # print(all_virus_area,all_area,all_circu)
            max_loc = all_area.index(max(all_area))
            res += all_circu[max_loc]
            isolation_zone.update(all_virus_area[max_loc])
            all_virus_area.pop(max_loc)

            next_time = []
            visited = set()
            for area in all_virus_area:
                spread(area)

            for i in range(row):
                for j in range(col):
                    area = []
                    if (i, j) not in isolation_zone and (i, j) not in visited and grid[i][j] == 1:
                        find_virus_area(i, j, area)
                        next_time.append(area)

            all_virus_area = next_time
        return res

    def containVirus2(self, grid):
        """
        流程:
        找到感染区域 -- > 这些感染区域污染的面积大小 -- > 需要的隔离带长度 --> 蔓延 -- > 找到感染区域 -- > ....
        :param grid:
        :return:
        """
        row = len(grid)
        col = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find_all_virus_area(grid):
            visited = set()
            all_virus_area = []

            def helper(i, j, one_virus_area):
                visited.add((i, j))
                one_virus_area.append((i, j))
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and grid[tmp_i][
                        tmp_j] == 1:
                        helper(tmp_i, tmp_j, one_virus_area)

            for i in range(row):
                for j in range(col):
                    one_virus_area = []
                    if (i, j) not in visited and grid[i][j] == 1:
                        helper(i, j, one_virus_area)
                        all_virus_area.append(one_virus_area)
            return all_virus_area

        def sprea_area(area):

            a = 0
            tmp_visited = set()
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col \
                            and (tmp_i, tmp_j) not in tmp_visited and grid[tmp_i][tmp_j] == 0:
                        tmp_visited.add((tmp_i, tmp_j))
                        a += 1
            return a

        def circu(area):
            cou = 0
            # tmp_visited = set()
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                        # tmp_visited.add((tmp_i, tmp_j))
                        cou += 1
            return cou

        def sprea(area):
            for i, j in area:
                for x, y in dirs:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                        grid[tmp_i][tmp_j] = 1

        # print(find_all_virus_area(grid))
        cur = find_all_virus_area(grid)
        res = 0
        while cur:
            all_virus_area = list(map(sprea_area, cur))
            # print(all_virus_area)
            max_loc = all_virus_area.index(max(all_virus_area))
            res += circu(cur[max_loc])
            #
            for i, j in cur[max_loc]:
                grid[i][j] = -1
            cur.pop(max_loc)
            for area in cur:
                sprea(area)
            cur = find_all_virus_area(grid)
        return res


a = Solution()
print(a.containVirus2([[0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0]]))
print(a.containVirus2([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]]))
print(a.containVirus2([[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]))
print(a.containVirus2([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
print(a.containVirus2([[0, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
                       [0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
                       [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]))
