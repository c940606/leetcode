from typing import List
from pprint import pprint

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        lookup = {}

        folder = [item.split("/") for item in folder]
        folder.sort(key=len)

        res = []
        for item in folder:
            tree = lookup
            for a in item:
                # print(a, tree)
                if "#" in tree:
                    break
                if a not in tree:
                    tree[a] = {}
                tree = tree[a]
            else:
                tree["#"] = "#"
                res.append("/".join(item))

        return res


a = Solution()
print(a.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(a.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
print(a.removeSubfolders(folder = ["/a/b/c","/a/b/d","/a/b/ca"]))
