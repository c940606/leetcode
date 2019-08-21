class Solution:
    def carPooling(self, trips, capacity):
        import heapq
        trips = sorted(trips, key=lambda x: x[1])
        heap = []
        cur_seat = 0
        for seat, start, end in trips:
            while heap and heap[0][0] <= start:
                t_start, t_seat = heapq.heappop(heap)
                cur_seat -= t_seat
            cur_seat += seat
            heapq.heappush(heap, [end, seat])
            if cur_seat > capacity:
                return False
        return True


a = Solution()
print(a.carPooling([[2, 1, 5], [3, 5, 7]], 3))
print(a.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11))
print(a.carPooling([[3, 2, 8], [4, 4, 6], [10, 8, 9]], 11))
