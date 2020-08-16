class LFUCache1:

    def __init__(self, capacity: int):
        from collections import OrderedDict, defaultdict
        self.freq = defaultdict(OrderedDict)
        self.key_to_freq = defaultdict(int)
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        res = self.freq[key_freq].pop(key)
        if not self.freq[key_freq] and key_freq == self.min_freq:
            self.min_freq += 1
        self.freq[key_freq + 1][key] = res
        self.key_to_freq[key] = key_freq + 1
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_to_freq:
            key_freq = self.key_to_freq[key]
            self.freq[key_freq].pop(key)
            if not self.freq[key_freq] and key_freq == self.min_freq:
                self.min_freq += 1
            self.freq[key_freq + 1][key] = value
            self.key_to_freq[key] = key_freq + 1
        else:
            if len(self.key_to_freq) == self.capacity:
                k, v = self.freq[self.min_freq].popitem(last=False)
                self.key_to_freq.pop(k)
            self.key_to_freq[key] = 1
            self.freq[1][key] = value
            self.min_freq = 1


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self.dummy = Node(None, None)
        # 成环
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.size = 0

    def append(self, node: Node):
        # 尾插入, 加到双向链表尾部
        node.prev = self.dummy.prev
        node.next = self.dummy
        node.prev.next = node
        self.dummy.prev = node
        self.size += 1

    def pop(self, node: Node = None):
        if self.size == 0:
            return
            # 删除头部
        if node is None:
            node = self.dummy.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        from collections import defaultdict
        self.key_to_node = {}
        self.freq = defaultdict(DLinkedList)
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node_freq = node.freq
        self.freq[node_freq].pop(node)
        if self.min_freq == node_freq and self.freq[node_freq].size != 0:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node_freq = node.freq
            self.freq[node_freq].pop(node)
            if self.min_freq == node_freq and self.freq[node_freq].size != 0:
                self.min_freq += 1
            node.freq += 1
            node.val = value
            self.freq[node.freq].append(node)
        else:
            if len(self.key_to_node) == self.capacity:
                node = self.freq[self.min_freq].pop()
                self.key_to_node.pop(node.key)
            node = Node(key, value)
            self.key_to_node[key] = node
            self.freq[1].append(node)
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
