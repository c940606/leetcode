from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        foods = set()
        tables = set()
        lookup = defaultdict(lambda :defaultdict(int))
        for x, y, z in orders:
            lookup[int(y)][z] += 1
            foods.add(z)
            tables.add(int(y))
        head = ["Table"] + list(sorted(foods))

        res = [head] + [[0] * len(head) for _ in range(len(tables))]
        # print(head, lookup, res)

        i = 1
        for k in sorted(lookup.keys()):

            res[i][0] = k
            for k1, v1 in lookup[k].items():
                loc = head.index(k1)
                res[i][loc] = str(v1)
            i += 1
        return res

a = Solution()
print(a.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))

print(a.displayTable(orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
print(a.displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))