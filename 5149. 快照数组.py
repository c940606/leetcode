import bisect


class SnapshotArray:

    def __init__(self, length: int):
        # 每一个位置的历史改变
        self.his = [[[-1, 0]] for _ in range(length)]
        # 第几次拍摄
        self.s = 0

    def set(self, index: int, val: int) -> None:
        # 添加历史记录
        self.his[index].append([self.s, val])

    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.his[index], snap_id) - 1
        return self[index][i][1]
    
