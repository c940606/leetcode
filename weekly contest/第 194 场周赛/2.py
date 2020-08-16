from typing import List
import collections


class Solution:
	def getFolderNames(self, names: List[str]) -> List[str]:
		dp = collections.defaultdict(int)