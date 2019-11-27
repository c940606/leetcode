class FileSystem:

    def __init__(self):
        self.lookup = {}

    def create(self, path: str, value: int) -> bool:
        cur = self.lookup
        path = [i  for i in path.split("/") if i != ""]
        #print(path)
        if len(path) == 1:
            cur[path[0]] = [value, {}]
            return True
        else:
            for p in path[:-1]:
                if p not in cur:
                   # print(p, cur)
                    return False
                cur = cur[p][1]
        if path[-1] in cur:
            cur[path[-1]][0] = value
        else:
            cur[path[-1]] = [value, {}]
        return True

    def get(self, path: str) -> int:
        cur = self.lookup
        path = [i  for i in path.split("/") if i != ""]
        res = None
        for p in path:
            if p not in cur:
                return -1
            res = cur[p][0]
            cur = cur[p][1]
        return res
