# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from typing import List
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = startUrl.split("/")[2]
        visited = set()

        def check(url: str):
            return domain == url.split("/")[2]

        def dfs(url):
            visited.add(url)
            for nxt_url in htmlParser.getUrls(url):
                if nxt_url not in visited and check(nxt_url):
                    dfs(nxt_url)

        return list(visited)


